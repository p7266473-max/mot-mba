import streamlit as st

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

/* Hide Streamlit bottom footer and bottom-right viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
.viewerBadge_container__16g3m {visibility: hidden !important; display: none !important;}
[class*="viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="styles_viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="ViewerBadge"] {visibility: hidden !important; display: none !important;}
.stActionButton {visibility: hidden !important; display: none !important;}
</style>
""", unsafe_allow_html=True)
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
