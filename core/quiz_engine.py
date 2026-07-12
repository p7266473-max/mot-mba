import streamlit as st
from typing import List, Dict, Any
from core.loader import QuestionModel
from core.scorer import calculate_score

def render_quiz_engine(week_key: str, questions: List[QuestionModel]):
    # Setup state
    state_key = f"quiz_state_{week_key}"
    if state_key not in st.session_state:
        st.session_state[state_key] = {
            "answers": {},
            "submitted": False
        }
    
    quiz_state = st.session_state[state_key]
    
    # Quiz Mode selection
    mode = st.radio(
        "Select Mode:",
        ["Study Mode (Instant Feedback)", "Exam Mode (Submit to Score)"],
        key=f"mode_{week_key}",
        horizontal=True
    )
    
    st.markdown("---")
    
    # Render Questions
    for idx, q in enumerate(questions):
        st.markdown(f"#### Q{idx + 1}: {q.question}")
        
        if q.type == "scenario" and q.scenario:
            st.warning(f"**📖 Case Context:**  \n{q.scenario}")
            
        if q.type in ["mcq", "tf", "scenario"]:
            # Render Radio choices
            choices = q.choices if q.choices else []
            prev_ans = quiz_state["answers"].get(q.id)
            selected = st.radio(
                "Options:",
                choices,
                index=choices.index(prev_ans) if prev_ans in choices else None,
                key=f"ans_{week_key}_{q.id}",
                label_visibility="collapsed"
            )
            if selected:
                quiz_state["answers"][q.id] = selected
                
            # Instant Feedback in Study Mode
            if mode.startswith("Study Mode") and selected is not None:
                correct_choice = choices[q.answer] if isinstance(q.answer, int) else q.answer
                if selected == correct_choice:
                    st.success("✅ **Correct!**")
                else:
                    st.error(f"❌ **Incorrect.** Correct answer: **{correct_choice}**")
                if q.explanation:
                    with st.expander("💡 View Explanation"):
                        st.info(q.explanation)
                        
        elif q.type == "fitb":
            prev_ans = quiz_state["answers"].get(q.id, "")
            text_val = st.text_input(
                "Your Answer:",
                value=prev_ans,
                key=f"ans_{week_key}_{q.id}",
                placeholder="Type your answer here..."
            )
            quiz_state["answers"][q.id] = text_val
            
            if mode.startswith("Study Mode") and text_val.strip():
                is_correct = (text_val.strip().lower() == str(q.answer).strip().lower())
                if is_correct:
                    st.success("✅ **Correct!**")
                else:
                    st.error(f"❌ **Incorrect.** Correct answer: **{q.answer}**")
                if q.explanation:
                    with st.expander("💡 View Explanation"):
                        st.info(q.explanation)
                        
        elif q.type == "match":
            st.markdown("*Select the matching item for each option below:*")
            left_items = q.left_items or []
            right_items = q.right_items or []
            
            if q.id not in quiz_state["answers"]:
                quiz_state["answers"][q.id] = {}
                
            col_l, col_r = st.columns([1, 1])
            with col_l:
                for item in left_items[:len(left_items)//2 + len(left_items)%2]:
                    prev_val = quiz_state["answers"][q.id].get(item, "-- Select --")
                    options = ["-- Select --"] + right_items
                    sel = st.selectbox(
                        f"Match: **{item}** ➔",
                        options,
                        index=options.index(prev_val) if prev_val in options else 0,
                        key=f"ans_{week_key}_{q.id}_{item}"
                    )
                    if sel != "-- Select --":
                        quiz_state["answers"][q.id][item] = sel
            with col_r:
                for item in left_items[len(left_items)//2 + len(left_items)%2:]:
                    prev_val = quiz_state["answers"][q.id].get(item, "-- Select --")
                    options = ["-- Select --"] + right_items
                    sel = st.selectbox(
                        f"Match: **{item}** ➔",
                        options,
                        index=options.index(prev_val) if prev_val in options else 0,
                        key=f"ans_{week_key}_{q.id}_{item}"
                    )
                    if sel != "-- Select --":
                        quiz_state["answers"][q.id][item] = sel
                        
            if mode.startswith("Study Mode") and all(k in quiz_state["answers"][q.id] for k in left_items):
                is_correct = True
                user_match = quiz_state["answers"][q.id]
                for l_key, r_val in q.answer.items():
                    if user_match.get(l_key) != r_val:
                        is_correct = False
                        break
                if is_correct:
                    st.success("✅ **Correct match!**")
                else:
                    st.error("❌ **Incorrect matches.**")
                    st.markdown("**Correct Matching Pairings:**")
                    for left_k, right_v in q.answer.items():
                        st.markdown(f"- *{left_k}* ➔ **{right_v}**")
                if q.explanation:
                    with st.expander("💡 View Explanation"):
                        st.info(q.explanation)
                        
        st.markdown("---")
        
    if mode.startswith("Exam Mode"):
        if not quiz_state["submitted"]:
            if st.button("Submit Exam", key=f"submit_{week_key}"):
                quiz_state["submitted"] = True
                st.rerun()
        else:
            result = calculate_score(questions, quiz_state["answers"])
            st.markdown(f"### 📊 Score Result: **{result['score']} / {result['total']}** ({result['percentage']:.1f}%)")
            
            # Export buttons
            try:
                from utils.exporter import export_score_to_csv, export_score_to_excel
                csv_data = export_score_to_csv(result)
                excel_data = export_score_to_excel(result)
                
                col_dl1, col_dl2 = st.columns(2)
                with col_dl1:
                    st.download_button(
                        label="📥 Download CSV Results",
                        data=csv_data,
                        file_name=f"quiz_results_{week_key}.csv",
                        mime="text/csv",
                        key=f"dl_csv_{week_key}"
                    )
                with col_dl2:
                    st.download_button(
                        label="📥 Download Excel Results",
                        data=excel_data,
                        file_name=f"quiz_results_{week_key}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        key=f"dl_excel_{week_key}"
                    )
            except Exception as e:
                st.warning(f"Could not load exporter utilities: {e}")
            
            if result['percentage'] >= 80.0:
                st.success("🎉 **Superb!** Outstanding performance. You have mastered this week's lesson.")
            elif result['percentage'] >= 50.0:
                st.warning("⚠️ **Pass.** Good effort. Review the explanations below.")
            else:
                st.error("❌ **Revision Needed.** Go over the weekly reading materials.")
                
            if st.button("Retake Exam", key=f"retake_{week_key}"):
                quiz_state["submitted"] = False
                quiz_state["answers"] = {}
                st.rerun()
                
            st.markdown("### 🔍 Exam Feedback Details:")
            for idx, q in enumerate(questions):
                fb = result["feedback"][q.id]
                if fb["is_correct"]:
                    st.markdown(f"🟢 **Q{idx+1}: Correct**")
                else:
                    st.markdown(f"🔴 **Q{idx+1}: Incorrect** (Correct: **{fb['correct_answer']}**)")
                if q.explanation:
                    with st.expander(f"See Explanation for Q{idx+1}"):
                        st.info(q.explanation)
