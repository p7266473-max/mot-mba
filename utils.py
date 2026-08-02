import streamlit as st

st.markdown("""
<style>
#MainMenu {visibility: hidden; display: none !important;}
header {visibility: hidden; display: none !important;}
footer {visibility: hidden; display: none !important;}
[data-testid="stHeader"] {visibility: hidden; display: none !important;}
[data-testid="stFooter"] {visibility: hidden; display: none !important;}
[data-testid="stToolbar"] {visibility: hidden; display: none !important;}
[data-testid="stDecoration"] {visibility: hidden; display: none !important;}
[data-testid="stStatusWidget"] {visibility: hidden; display: none !important;}
.stAppDeployButton {display: none !important;}
#stDecoration {display: none !important;}
</style>
""", unsafe_allow_html=True)

def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
        
        * {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        
        .title-text {
            font-family: 'Outfit', sans-serif;
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #0D9488 0%, #38BDF8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        
        .subtitle-text {
            font-size: 1.1rem;
            color: #94A3B8;
            margin-bottom: 2rem;
        }
        
        .card {
            background: #1E293B;
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 1.8rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .card:hover {
            border-color: #38BDF8;
            box-shadow: 0 10px 15px -3px rgba(56, 189, 248, 0.2);
        }
        
        .card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #334155;
            padding-bottom: 0.8rem;
            margin-bottom: 1.2rem;
        }
        
        .card-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #F8FAFC;
        }
        
        .badge {
            background: rgba(56, 189, 248, 0.15);
            color: #38BDF8;
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        
        .interactive-header {
            background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
            border-left: 5px solid #0D9488;
            padding: 1.2rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

def get_quiz_state(session_key, q_count):
    if "quiz_states" not in st.session_state:
        st.session_state.quiz_states = {}
    if session_key not in st.session_state.quiz_states:
        st.session_state.quiz_states[session_key] = {
            "answers": [None] * q_count,
            "submitted": False,
            "mode": "Study Mode"
        }
    return st.session_state.quiz_states[session_key]

def render_quiz(session_key, questions):
    q_state = get_quiz_state(session_key, len(questions))
    state_answers_key = f"ans_{session_key}"
    state_mode_key = f"mode_{session_key}"
    state_sub_key = f"sub_{session_key}"
        
    col_ctrl, col_info = st.columns([2, 3])
    with col_ctrl:
        q_state["mode"] = st.radio(
            f"Select Quiz Mode:",
            ["Study Mode (Instant Feedback & Reveal)", "Exam Mode (Submit to Score)"],
            key=state_mode_key
        )
    with col_info:
        st.info("💡 **Study Mode:** Select options to see correct/incorrect alerts instantly, with options to reveal explanation tabs. \n\n🔒 **Exam Mode:** Answer all questions fully and click 'Submit Quiz' at the bottom to calculate your final grade.")

    st.markdown("---")
    
    correct_count = 0
    
    for idx, q in enumerate(questions):
        st.markdown(f"##### ❓ Question {idx+1}: {q['text']}")
        
        # User answer input
        prev_ans = q_state["answers"][idx]
        selected_option = st.radio(
            "Select one of the options:",
            q["options"],
            index=q["options"].index(prev_ans) if prev_ans in q["options"] else None,
            key=f"{state_answers_key}_{idx}",
            label_visibility="collapsed"
        )
        
        q_state["answers"][idx] = selected_option
        
        is_correct = selected_option == q["correct"]
        if is_correct:
            correct_count += 1
            
        # UI Response based on mode
        if q_state["mode"] == "Study Mode (Instant Feedback & Reveal)" and selected_option is not None:
            if is_correct:
                st.success("✅ **Correct!**")
            else:
                st.error(f"❌ **Incorrect.** The correct answer is: **{q['correct']}**")
            
            exp_tabs = st.tabs(["💡 Reveal Explanation", "🔑 Correct Answer"])
            with exp_tabs[0]:
                st.write(q["explanation"])
            with exp_tabs[1]:
                st.markdown(f"The correct option is: **{q['correct']}**")
        
        st.markdown("---")
        
    if q_state["mode"] == "Exam Mode (Submit to Score)":
        if not q_state["submitted"]:
            if st.button("Submit Quiz", key=state_sub_key):
                q_state["submitted"] = True
                st.rerun()
        else:
            score_pct = (correct_count / len(questions)) * 100
            st.markdown(f"#### 📊 Final Score: **{correct_count} / {len(questions)}** ({score_pct:.1f}%)")
            if score_pct >= 80.0:
                st.success("🎉 Excellent! You have mastered this session's concepts.")
            elif score_pct >= 50.0:
                st.warning("⚡ Good effort. Review the slides and try again to improve your score.")
            else:
                st.error("❌ Need revision. Check the study slide summary logs above.")
                
            if st.button("Retake Quiz", key=f"retake_{state_sub_key}"):
                q_state["submitted"] = False
                q_state["answers"] = [None] * len(questions)
                st.rerun()
                
            # Render answers post-submission
            st.markdown("### 📋 Detailed Assessment Feedback:")
            for idx, q in enumerate(questions):
                user_ans = q_state["answers"][idx]
                if user_ans == q["correct"]:
                    st.write(f"🟢 **Q{idx+1}: Correct** — Your answer: *{user_ans}*")
                else:
                    st.write(f"🔴 **Q{idx+1}: Incorrect** — Your answer: *{user_ans}* (Correct: *{q['correct']}*)")
                with st.expander(f"See Q{idx+1} Explanation", expanded=False):
                    st.write(q["explanation"])
