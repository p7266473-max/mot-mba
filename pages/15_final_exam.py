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

/* Hide Streamlit bottom footer and viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
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
        '.stActionButton', 'button[title*="Streamlit"]', 'div[class*="StatusWidget"]'
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
import os
from core.loader import load_week_questions
from core.randomizer import get_random_sample
from core.quiz_engine import render_quiz_engine

st.markdown("## 🎓 Synthesis Final Examination")
st.markdown("This section generates a comprehensive exam combining random questions from all 14 sessions.")

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_questions = []

for week in range(1, 15):
    all_questions.extend(load_week_questions(base_path, week))

if not all_questions:
    st.error("No question banks found. Please run the generator first.")
else:
    exam_size = st.selectbox(
        "Select Exam Size:",
        [15, 30, 50, len(all_questions)],
        format_func=lambda x: f"{x} Questions" if x != len(all_questions) else f"All {x} Questions"
    )
    
    state_key = "final_exam_questions"
    if state_key not in st.session_state or len(st.session_state[state_key]) != exam_size:
        st.session_state[state_key] = get_random_sample(all_questions, exam_size)
        
    if st.button("🔄 Generate New Exam Set"):
        st.session_state[state_key] = get_random_sample(all_questions, exam_size)
        st.rerun()
        
    render_quiz_engine("final_exam", st.session_state[state_key])
