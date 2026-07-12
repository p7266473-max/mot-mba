import streamlit as st
import os
import random
from core.loader import load_week_quiz
from core.randomizer import randomize_questions
from core.quiz_engine import render_quiz_engine

st.markdown("## 🎓 Final Examination")
st.markdown("This section generates a comprehensive exam combining questions from all 7 sessions. Perfect for overall preparation.")

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
all_questions = []

for week in range(1, 8):
    quiz_path = os.path.join(base_path, "sessiondata", f"week{week}.json")
    try:
        quiz = load_week_quiz(quiz_path)
        all_questions.extend(quiz.questions)
    except Exception as e:
        pass

if not all_questions:
    st.error("No question banks found. Please run the generator first.")
else:
    # Option to select size
    exam_size = st.selectbox(
        "Select Exam Size:",
        [20, 40, len(all_questions)],
        format_func=lambda x: f"{x} Questions" if x != len(all_questions) else f"All {x} Questions"
    )
    
    # Store selected questions in session state so they don't randomize on every click
    state_key = "final_exam_questions"
    if state_key not in st.session_state or len(st.session_state[state_key]) != exam_size:
        # Shuffled sample
        shuffled = randomize_questions(all_questions)
        st.session_state[state_key] = shuffled[:exam_size]
        
    if st.button("🔄 Generate New Exam Set"):
        shuffled = randomize_questions(all_questions)
        st.session_state[state_key] = shuffled[:exam_size]
        st.rerun()
        
    render_quiz_engine("final_exam", st.session_state[state_key])
