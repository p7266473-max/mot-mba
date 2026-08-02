import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="MOT MBA Exam Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

import streamlit.components.v1 as components

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

/* Hide Streamlit bottom footer, bottom container, and viewer/host badges */
footer {visibility: hidden !important; display: none !important;}
[data-testid="stFooter"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottom"] {visibility: hidden !important; display: none !important;}
[data-testid="stBottomBlockContainer"] {visibility: hidden !important; display: none !important;}
.viewerBadge_container__16g3m {visibility: hidden !important; display: none !important;}
[class*="viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="styles_viewerBadge"] {visibility: hidden !important; display: none !important;}
[class*="ViewerBadge"] {visibility: hidden !important; display: none !important;}
.stActionButton {visibility: hidden !important; display: none !important;}
</style>
""", unsafe_allow_html=True)

components.html("""
<script>
function cleanupStreamlitUI() {
    const targetSelectors = [
        'footer', '[data-testid="stFooter"]', '[data-testid="stDecoration"]',
        '[data-testid="stStatusWidget"]', '[data-testid="stToolbar"]', '#MainMenu',
        'header', '.stAppDeployButton', '#stDecoration', '.viewerBadge_container__16g3m',
        '[class*="viewerBadge"]', '[class*="styles_viewerBadge"]', '[class*="ViewerBadge"]',
        '.stActionButton', '[data-testid="stBottom"]', '[data-testid="stBottomBlockContainer"]',
        'button[title*="Streamlit"]', 'div[class*="StatusWidget"]'
    ];

    [document, window.parent.document].forEach(doc => {
        try {
            targetSelectors.forEach(selector => {
                doc.querySelectorAll(selector).forEach(el => {
                    el.style.setProperty('display', 'none', 'important');
                    el.style.setProperty('visibility', 'hidden', 'important');
                    el.style.setProperty('opacity', '0', 'important');
                });
            });
        } catch (err) {}
    });
}
cleanupStreamlitUI();
setInterval(cleanupStreamlitUI, 250);
</script>
""", height=0, width=0)


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
