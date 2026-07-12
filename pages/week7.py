import streamlit as st
import os
from core.loader import load_week_quiz
from core.quiz_engine import render_quiz_engine

st.markdown("## 🪙 Session 7: E-Business Ecosystems & Cloud Governance")

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
quiz_path = os.path.join(base_path, "sessiondata", "week7.json")

try:
    quiz = load_week_quiz(quiz_path)
    render_quiz_engine("week7", quiz.questions)
except Exception as e:
    st.error(f"Failed to load quiz data: {e}")
