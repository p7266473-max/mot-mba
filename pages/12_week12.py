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

st.markdown("## 🕸️ Week 12: Managing E-Business Networks")

# Construct path relative to repo root
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load all 25 questions
all_questions = load_week_questions(base_path, 12)

if not all_questions:
    st.error("Failed to load questions. Make sure the database exists.")
else:
    # Sample 15 questions randomly for this attempt and cache them in session state
    state_key = "sampled_questions_week12"
    if state_key not in st.session_state:
        st.session_state[state_key] = get_random_sample(all_questions, 15)
        
    if st.button("🔄 Generate New Attempt Set"):
        st.session_state[state_key] = get_random_sample(all_questions, 15)
        st.rerun()
        
    render_quiz_engine("week12", st.session_state[state_key])
