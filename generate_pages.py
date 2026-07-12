import os

def main():
    base_dir = "/home/efar/mot-mba"
    pages_dir = os.path.join(base_dir, "pages")
    os.makedirs(pages_dir, exist_ok=True)
    
    # 14 weekly pages
    week_titles = {
        1: "🔄 Week 1: Systems Thinking & Control Systems",
        2: "📋 Week 2: Tech Planning & Digital Strategy",
        3: "🏗️ Week 3: Systems Design Methodologies",
        4: "🛡️ Week 4: Information Ethics & Privacy",
        5: "🔄 Week 5: Systems Development Life Cycles (SDLC)",
        6: "📊 Week 6: IT Frameworks & TPS",
        7: "📈 Week 7: Transaction Concepts & Data Decisions",
        8: "⚡ Week 8: Legislative Trends & Cloud Infrastructure",
        9: "💼 Week 9: Managing Application Portfolios",
        10: "🎯 Week 10: Agile Projects & Risk Analysis",
        11: "🤝 Week 11: Buy vs. Build & SaaS Alternatives",
        12: "🕸️ Week 12: Managing E-Business Networks",
        13: "📅 Week 13: Cloud Governance & Continuity Planning",
        14: "🎓 Week 14: Synthesis & Revision Review"
    }
    
    for week in range(1, 15):
        filename = f"{week:02d}_week{week:02d}.py"
        filepath = os.path.join(pages_dir, filename)
        
        content = f"""import streamlit as st
import os
from core.loader import load_week_questions
from core.randomizer import get_random_sample
from core.quiz_engine import render_quiz_engine

st.markdown("## {week_titles[week]}")

# Construct path relative to repo root
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load all 25 questions
all_questions = load_week_questions(base_path, {week})

if not all_questions:
    st.error("Failed to load questions. Make sure the database exists.")
else:
    # Sample 15 questions randomly for this attempt and cache them in session state
    state_key = "sampled_questions_week{week:02d}"
    if state_key not in st.session_state:
        st.session_state[state_key] = get_random_sample(all_questions, 15)
        
    if st.button("🔄 Generate New Attempt Set"):
        st.session_state[state_key] = get_random_sample(all_questions, 15)
        st.rerun()
        
    render_quiz_engine("week{week:02d}", st.session_state[state_key])
"""
        with open(filepath, "w") as f:
            f.write(content)
            
    # Save final_exam.py as 15_final_exam.py
    filename_exam = "15_final_exam.py"
    filepath_exam = os.path.join(pages_dir, filename_exam)
    
    exam_content = """import streamlit as st
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
"""
    with open(filepath_exam, "w") as f:
        f.write(exam_content)
        
    print("Successfully generated all 14 weekly pages and final exam page!")

if __name__ == "__main__":
    main()
