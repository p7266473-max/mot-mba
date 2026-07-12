import streamlit as st
from utils import inject_custom_css, render_quiz
from data_store import (
    SESSION_1_QUIZ,
    SESSION_2_QUIZ,
    SESSION_3_QUIZ,
    SESSION_4_QUIZ,
    SESSION_5_QUIZ,
    SESSION_6_QUIZ,
    SESSION_7_QUIZ,
)

# Page configuration
st.set_page_config(
    page_title="MOT MBA Practice Quizzes",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject CSS styling
inject_custom_css()

# Sidebar configurations
with st.sidebar:
    st.markdown("### 📋 Course Overview")
    st.markdown("""
    **Track:** MBA (Business Administration)  
    **Course:** Management of Technology (MOT)  
    **Lecturer:** Mr. Irfan  
    """)
    
    st.markdown("---")
    st.markdown("### 🧭 Portal Focus")
    st.info("🎓 **MBA - COM 573**\n\nManagement of Technology\n\n*Binary University*")
    
    st.markdown("---")
    st.markdown("### 📈 Course Progress")
    progress = st.slider("Mark Syllabus Completed (%):", 0, 100, 71)
    st.progress(progress / 100)
    st.caption(f"{progress}% of total syllabus covered")

# Main Application Title
st.markdown('<div class="title-text">🎓 Management of Technology (MOT)</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Practice Quizzes</div>', unsafe_allow_html=True)

# 7 Week Tabs
tab_titles = ["Week 1 Lesson Plan", "Week 2 Lesson Plan", "Week 3 Lesson Plan", "Week 4 Lesson Plan", "Week 5 Lesson Plan", "Week 6 Lesson Plan", "Week 7 Lesson Plan"]
tabs = st.tabs(tab_titles)

with tabs[0]:
    render_quiz("Week 1", SESSION_1_QUIZ)

with tabs[1]:
    render_quiz("Week 2", SESSION_2_QUIZ)

with tabs[2]:
    render_quiz("Week 3", SESSION_3_QUIZ)

with tabs[3]:
    render_quiz("Week 4", SESSION_4_QUIZ)

with tabs[4]:
    render_quiz("Week 5", SESSION_5_QUIZ)

with tabs[5]:
    render_quiz("Week 6", SESSION_6_QUIZ)

with tabs[6]:
    render_quiz("Week 7", SESSION_7_QUIZ)
