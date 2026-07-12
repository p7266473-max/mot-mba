import streamlit as st
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
