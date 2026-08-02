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
import os
from core.loader import load_week_questions
from core.randomizer import get_random_sample
from core.quiz_engine import render_quiz_engine

st.markdown("## 📋 Week 2: Tech Planning & Digital Strategy")

# Construct path relative to repo root
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load all 25 questions
all_questions = load_week_questions(base_path, 2)

if not all_questions:
    st.error("Failed to load questions. Make sure the database exists.")
else:
    # Sample 15 questions randomly for this attempt and cache them in session state
    state_key = "sampled_questions_week02"
    if state_key not in st.session_state:
        st.session_state[state_key] = get_random_sample(all_questions, 15)
        
    if st.button("🔄 Generate New Attempt Set"):
        st.session_state[state_key] = get_random_sample(all_questions, 15)
        st.rerun()
        
    render_quiz_engine("week02", st.session_state[state_key])
