import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="MOT MBA Exam Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Style Injection
css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# App Content
st.markdown('# 🎓 Management of Technology (MOT) MBA Portal')
st.markdown('### Interactive Practice Exams & Study Portal')

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Welcome to the **Binary University MBA - COM 573** portal. 
    This application hosts offline question banks and interactive quiz engines mapped to your 7 core sessions.
    
    ### 🧭 How to use this Portal
    1. Select a Session from the sidebar menu (e.g., Week 1, Week 2, etc.).
    2. Toggle between **Study Mode** (for instant feedback and explanations) and **Exam Mode** (for official testing).
    3. Complete the final synthesis check in the **Final Exam** page.
    4. Export your score logs using the CSV/Excel download buttons at the bottom of exams.
    """)

with col2:
    st.info("""
    **Track:** MBA (Business Administration)  
    **Lecturer:** Mr. Irfan  
    **Database engine:** JSON offline datastore  
    **Uptime status:** 100% Offline stable  
    """)
    st.progress(0.28)
    st.caption("Syllabus coverage progress tracker: 28% completed")
