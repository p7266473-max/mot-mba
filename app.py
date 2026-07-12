import streamlit as st
from utils import inject_custom_css
from pages_layout import (
    render_session_1,
    render_session_2,
    render_session_3,
    render_session_4,
    render_session_5,
    render_session_6,
    render_session_7,
)

# Page configuration
st.set_page_config(
    page_title="MOT MBA Lesson Plan & Interactive Portal",
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
st.markdown('<div class="subtitle-text">Curriculum Portal & Interactive Sandbox</div>', unsafe_allow_html=True)

# 7 Session Tabs
tab_titles = [
    "Session 1: Weeks 1 & 2",
    "Session 2: Weeks 3 & 4",
    "Session 3: Weeks 5 & 6",
    "Session 4: Weeks 7 & 8",
    "Session 5: Weeks 9 & 10",
    "Session 6: Weeks 11 & 12",
    "Session 7: Week 13"
]
tabs = st.tabs(tab_titles)

# Render each tab using modular page functions
with tabs[0]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Practice Quiz"])
    render_session_1(sub_tabs)

with tabs[1]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Practice Quiz"])
    render_session_2(sub_tabs)

with tabs[2]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Practice Quiz"])
    render_session_3(sub_tabs)

with tabs[3]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Practice Quiz"])
    render_session_4(sub_tabs)

with tabs[4]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Practice Quiz"])
    render_session_5(sub_tabs)

with tabs[5]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Practice Quiz"])
    render_session_6(sub_tabs)

with tabs[6]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Practice Quiz"])
    render_session_7(sub_tabs)
