import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MOT MBA Lesson Plan Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium styling
st.markdown("""
<style>
    /* Styling variables and fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .title-text {
        font-family: 'Outfit', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0D9488 0%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .subtitle-text {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    
    .week-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .week-card:hover {
        transform: translateY(-2px);
        border-color: #0D9488;
        box-shadow: 0 12px 20px -8px rgba(13, 148, 136, 0.3);
    }
    
    .week-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #334155;
        padding-bottom: 0.8rem;
        margin-bottom: 1.2rem;
    }
    
    .week-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #F8FAFC;
    }
    
    .hours-badge {
        background: rgba(13, 148, 136, 0.15);
        color: #2DD4BF;
        border: 1px solid rgba(13, 148, 136, 0.3);
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .topic-list {
        margin: 0;
        padding-left: 1.2rem;
    }
    
    .topic-item {
        color: #E2E8F0;
        font-size: 1.05rem;
        margin-bottom: 0.6rem;
        line-height: 1.5;
    }
    
    .sidebar-info {
        background: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 1.2rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main Application Title & Subtitle
st.markdown('<div class="title-text">🎓 Management of Technology (MOT)</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Curriculum Lesson Plan for the MBA (Business Administration) Track</div>', unsafe_allow_html=True)

# Sidebar with general info
with st.sidebar:
    st.markdown("### 📋 Course Overview")
    st.markdown("""
    **Track:** MBA (Business Administration)  
    **Course:** Management of Technology (MOT)  
    **Structure:** 7 Combined Sessions (6 Hours per Session / Week)  
    **Total Scope:** 13 Weeks of Core Syllabus  
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Learning Framework")
    st.markdown("""
    This digital portal maps out key systems theories, requirement strategies, software lifecycles, and governance paradigms essential for technology managers.
    """)
    
    st.markdown("---")
    st.markdown("### 🎯 Syllabus Coverage")
    coverage = st.slider("Select progress made:", 0, 100, 0)
    st.progress(coverage / 100)
    st.caption(f"{coverage}% of curriculum covered")

# 7 Tabs matching combined Weeks
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

# Content mapping for the sessions
sessions_data = {
    0: {
        "title": "Systems Thinking & Tech Strategy",
        "weeks": [
            {
                "num": "Week 1",
                "focus": "Understanding Systems Theories & Decisional Contexts",
                "topics": [
                    "Understanding systems theories",
                    "Control systems & organizational systems thinking",
                    "Feedback and control in management systems",
                    "Digital systems in organizations",
                    "Information as a strategic asset",
                    "Role of managers in digital decision environments"
                ]
            },
            {
                "num": "Week 2",
                "focus": "Digital Strategy & Technology Management Planning",
                "topics": [
                    "Developing a technology management plan",
                    "Digital strategy planning",
                    "Business capability and organizational needs alignment",
                    "Human-centered requirements engineering",
                    "Data-driven requirement gathering",
                    "Stakeholder involvement in technology planning"
                ]
            }
        ]
    },
    1: {
        "title": "Business Systems Design & Governance",
        "weeks": [
            {
                "num": "Week 3",
                "focus": "System Design Methodologies & Strategy Roadmaps",
                "topics": [
                    "System design methodologies & principle models",
                    "Business system design approaches",
                    "Enterprise systems (conceptual frameworks)",
                    "Business problem analysis prior to technology selection",
                    "Digital transformation roadmap design"
                ]
            },
            {
                "num": "Week 4",
                "focus": "Digital Regulation, Ethics & Workplace Compliance",
                "topics": [
                    "Data Protection Act provisions",
                    "Computer ethics & data protection/privacy standards",
                    "Digital ethics & regulatory frameworks",
                    "Legal and ethical decision-making matrix",
                    "Workplace monitoring policies & best practices",
                    "AI ethics awareness in enterprise administration"
                ]
            }
        ]
    },
    2: {
        "title": "SDLC Models & Business Integration",
        "weeks": [
            {
                "num": "Week 5",
                "focus": "Software Development Life Cycles (SDLC)",
                "topics": [
                    "System development lifecycle concepts",
                    "Various SDLC models & key benefits",
                    "Importance of adopting structured SDLC paths",
                    "SDLC as a framework for management processes",
                    "Waterfall model (strengths & limitations)",
                    "Prototyping model (strengths & limitations)",
                    "Introduction to agile thinking and methodologies"
                ]
            },
            {
                "num": "Week 6",
                "focus": "Frameworks & Integrated Processing",
                "topics": [
                    "Understanding computer systems concepts and methods",
                    "IT frameworks & decision frameworks",
                    "Business-technology integration & alignment",
                    "Technology management frameworks",
                    "Digital transformation planning",
                    "Transaction processing concepts"
                ]
            }
        ]
    },
    3: {
        "title": "Infrastructure, Trends & Integration",
        "weeks": [
            {
                "num": "Week 7",
                "focus": "Systems Concepts & Digital Transformation Planning",
                "topics": [
                    "Understanding computer systems concepts and methods",
                    "IT frameworks & decision frameworks",
                    "Business-technology integration & alignment",
                    "Technology management frameworks",
                    "Digital transformation planning",
                    "Transaction processing concepts"
                ]
            },
            {
                "num": "Week 8",
                "focus": "Infrastructure, Platforms & Legislative Shifts",
                "topics": [
                    "Legislative and industry trends",
                    "Semiconductor industry trends & resource shifts",
                    "Digital platforms & cloud infrastructure",
                    "Telecom regulation & network ecosystems",
                    "Industry transformation dynamics",
                    "Local vs. long-distance considerations"
                ]
            }
        ]
    },
    4: {
        "title": "Portfolio Governance & Application Management",
        "weeks": [
            {
                "num": "Week 9",
                "focus": "Managing Application Portfolios",
                "topics": [
                    "Managing application portfolios (APM)",
                    "Lifecycle analysis & technological obsolescence",
                    "Maintenance and enhancements strategy",
                    "Programming backlog management",
                    "Prioritization methodologies & cost of change estimation",
                    "Governance frameworks vs. typical ad hoc processes"
                ]
            },
            {
                "num": "Week 10",
                "focus": "Application Development & Project Management",
                "topics": [
                    "Managing application development",
                    "Agile project management concepts",
                    "Business case development for software systems",
                    "Stage-gate review systems & risk analysis",
                    "Programming process improvements",
                    "Successful application management keys"
                ]
            }
        ]
    },
    5: {
        "title": "Development Alternatives & E-Business Systems",
        "weeks": [
            {
                "num": "Week 11",
                "focus": "System Development & Acquisition Alternatives",
                "topics": [
                    "Development and acquisition alternatives",
                    "System development approaches",
                    "Outsourcing strategies",
                    "Buy vs. Build decisions",
                    "SaaS (Software-as-a-Service) vs. custom system design",
                    "Acquisition strategies & vendor assessment"
                ]
            },
            {
                "num": "Week 12",
                "focus": "E-Business Infrastructure & Cloud Governance",
                "topics": [
                    "Managing e-business applications",
                    "Digital ecosystems & Intranets/Extranets",
                    "Management issues in distributed environments",
                    "E-business systems planning",
                    "Cloud governance, change management & continuity planning"
                ]
            }
        ]
    },
    6: {
        "title": "Continuity & Enterprise Ecosystems",
        "weeks": [
            {
                "num": "Week 13",
                "focus": "E-Business Systems & Change Management",
                "topics": [
                    "Managing e-business applications",
                    "Digital ecosystems & Intranets/Extranets",
                    "Management issues in distributed environments",
                    "E-business systems planning",
                    "Cloud governance, change management & continuity planning"
                ]
            }
        ]
    }
}

# Render each tab
for tab_id, data in sessions_data.items():
    with tabs[tab_id]:
        st.subheader(data["title"])
        
        # Display each week in this session
        for week in data["weeks"]:
            st.markdown(f"""
            <div class="week-card">
                <div class="week-header">
                    <span class="week-title">📅 {week['num']} — {week['focus']}</span>
                    <span class="hours-badge">3 Hours</span>
                </div>
            <ul class="topic-list">
            """, unsafe_allow_html=True)
            
            for topic in week["topics"]:
                st.markdown(f'<li class="topic-item">🔹 {topic}</li>', unsafe_allow_html=True)
                
            st.markdown("""
            </ul>
            </div>
            """, unsafe_allow_html=True)
