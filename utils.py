import streamlit as st

import streamlit.components.v1 as components

st.markdown("""
<style>
/* Hide Streamlit top header, toolbar, GitHub fork badges, menu, and decoration */
#MainMenu {visibility: hidden !important; display: none !important;}
header {visibility: hidden !important; display: none !important;}
[data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
[data-testid="stDecoration"] {visibility: hidden !important; display: none !important;}
[data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
.stAppDeployButton {visibility: hidden !important; display: none !important;}
#stDecoration {visibility: hidden !important; display: none !important;}

/* Hide Streamlit bottom footer, bottom container, and viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottom"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottomBlockContainer"] {visibility: hidden !important; display: none !important;}
.viewerBadge_container__16g3m {visibility: hidden !important; display: none !important;}
[class*="viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="styles_viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="ViewerBadge"] {visibility: hidden !important; display: none !important;}
.stActionButton {visibility: hidden !important; display: none !important;}
</style>
""", unsafe_allow_html=True)

components.html("""
<script>
function cleanupStreamlitUI() {
    const targetSelectors = [
        'footer', '[data-testid="stFooter"]', '[data-testid="stDecoration"]',
        '[data-testid="stStatusWidget"]', '[data-testid="stToolbar"]', '#MainMenu',
        'header', '.stAppDeployButton', '#stDecoration', '.viewerBadge_container__16g3m',
        '[class*="viewerBadge"]', '[class*="styles_viewerBadge"]', '[class*="ViewerBadge"]',
        '.stActionButton', '[data-testid="stBottom"]', '[data-testid="stBottomBlockContainer"]',
        'button[title*="Streamlit"]', 'div[class*="StatusWidget"]'
    ];

    [document, window.parent.document].forEach(doc => {
        try {
            targetSelectors.forEach(selector => {
                doc.querySelectorAll(selector).forEach(el => {
                    el.style.setProperty('display', 'none', 'important');
                    el.style.setProperty('visibility', 'hidden', 'important');
                    el.style.setProperty('opacity', '0', 'important');
                });
            });
        } catch (err) {}
    });
}
cleanupStreamlitUI();
setInterval(cleanupStreamlitUI, 250);
</script>
""", height=0, width=0)

def inject_custom_css():
    import streamlit.components.v1 as components

st.markdown("""
<style>
/* Hide Streamlit top header, toolbar, GitHub fork badges, menu, and decoration */
#MainMenu {visibility: hidden !important; display: none !important;}
header {visibility: hidden !important; display: none !important;}
[data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
[data-testid="stDecoration"] {visibility: hidden !important; display: none !important;}
[data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
.stAppDeployButton {visibility: hidden !important; display: none !important;}
#stDecoration {visibility: hidden !important; display: none !important;}

/* Hide Streamlit bottom footer, bottom container, and viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottom"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottomBlockContainer"] {visibility: hidden !important; display: none !important;}
.viewerBadge_container__16g3m {visibility: hidden !important; display: none !important;}
[class*="viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="styles_viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="ViewerBadge"] {visibility: hidden !important; display: none !important;}
.stActionButton {visibility: hidden !important; display: none !important;}
</style>
""", unsafe_allow_html=True)

components.html("""
<script>
function cleanupStreamlitUI() {
    const targetSelectors = [
        'footer', '[data-testid="stFooter"]', '[data-testid="stDecoration"]',
        '[data-testid="stStatusWidget"]', '[data-testid="stToolbar"]', '#MainMenu',
        'header', '.stAppDeployButton', '#stDecoration', '.viewerBadge_container__16g3m',
        '[class*="viewerBadge"]', '[class*="styles_viewerBadge"]', '[class*="ViewerBadge"]',
        '.stActionButton', '[data-testid="stBottom"]', '[data-testid="stBottomBlockContainer"]',
        'button[title*="Streamlit"]', 'div[class*="StatusWidget"]'
    ];

    [document, window.parent.document].forEach(doc => {
        try {
            targetSelectors.forEach(selector => {
                doc.querySelectorAll(selector).forEach(el => {
                    el.style.setProperty('display', 'none', 'important');
                    el.style.setProperty('visibility', 'hidden', 'important');
                    el.style.setProperty('opacity', '0', 'important');
                });
            });
        } catch (err) {}
    });
}
cleanupStreamlitUI();
setInterval(cleanupStreamlitUI, 250);
</script>
""", height=0, width=0)

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
