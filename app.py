import sys
import subprocess

def install_missing_packages():
    required = ["streamlit", "google-genai", "google-generativeai", "pandas"]
    for pkg in required:
        try:
            if pkg == "google-genai":
                import google.genai
            elif pkg == "google-generativeai":
                import google.generativeai
            else:
                __import__(pkg)
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

install_missing_packages()

import streamlit as st
import pandas as pd
import hashlib
import json
import os


# Page configuration
st.set_page_config(
    page_title="MOT MBA Lesson Plan & Interactive Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium styling
st.markdown("""
<style>
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
        color: #94A3B8;
        margin-bottom: 2rem;
    }
    
    .card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        border-color: #38BDF8;
        box-shadow: 0 10px 15px -3px rgba(56, 189, 248, 0.2);
    }
    
    .card-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #334155;
        padding-bottom: 0.8rem;
        margin-bottom: 1.2rem;
    }
    
    .card-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #F8FAFC;
    }
    
    .badge {
        background: rgba(56, 189, 248, 0.15);
        color: #38BDF8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .interactive-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-left: 5px solid #0D9488;
        padding: 1.2rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session States
if "quiz_states" not in st.session_state:
    st.session_state.quiz_states = {}
if "dynamic_quizzes" not in st.session_state:
    st.session_state.dynamic_quizzes = {}
if "dynamic_quiz_states" not in st.session_state:
    st.session_state.dynamic_quiz_states = {}

def get_quiz_state(session_key, q_count):
    if session_key not in st.session_state.quiz_states:
        st.session_state.quiz_states[session_key] = {
            "answers": [None] * q_count,
            "submitted": False,
            "mode": "Study Mode"
        }
    return st.session_state.quiz_states[session_key]

def get_dynamic_quiz_state(session_key, q_count):
    state_key = f"dyn_{session_key}"
    if state_key not in st.session_state.dynamic_quiz_states:
        st.session_state.dynamic_quiz_states[state_key] = {
            "answers": [None] * q_count,
            "submitted": False,
            "mode": "Study Mode"
        }
    return st.session_state.dynamic_quiz_states[state_key]

# Slide Context Parser
def load_slides_context(session_index):
    try:
        filepath = os.path.join(os.path.dirname(__file__), "extracted_slides.txt")
        if not os.path.exists(filepath):
            return "Management of Technology curriculum syllabus context."
            
        with open(filepath, "r") as f:
            content = f.read()
            
        parts = content.split("========================================")
        clean_parts = [p.strip() for p in parts if p.strip()]
        
        if session_index == 0:
            w1_part = clean_parts[0] if len(clean_parts) > 0 else ""
            lines = w1_part.split("\n")
            w1_lines = []
            for line in lines:
                if "--- Slide 19 ---" in line:
                    break
                w1_lines.append(line)
            return "\n".join(w1_lines)
            
        elif session_index == 1:
            w1_part = clean_parts[0] if len(clean_parts) > 0 else ""
            lines = w1_part.split("\n")
            w2_lines = []
            capture = False
            for line in lines:
                if "--- Slide 19 ---" in line:
                    capture = True
                if "--- Slide 28 ---" in line:
                    break
                if capture:
                    w2_lines.append(line)
            return "\n".join(w2_lines)
            
        elif session_index == 2:
            return clean_parts[2] if len(clean_parts) > 2 else ""
            
        elif session_index == 3:
            return clean_parts[3] if len(clean_parts) > 3 else ""
            
        elif session_index == 4:
            return "Application Portfolio Management, software lifecycle, maintenance vs enhancement, programming backlog prioritization, cost of change, strategic business case reviews."
            
        elif session_index == 5:
            w5_part = clean_parts[4] if len(clean_parts) > 4 else ""
            lines = w5_part.split("\n")
            w6_lines = []
            for line in lines:
                if "TOPIC 8" in line:
                    break
                w6_lines.append(line)
            return "\n".join(w6_lines)
            
        elif session_index == 6:
            w5_part = clean_parts[4] if len(clean_parts) > 4 else ""
            lines = w5_part.split("\n")
            w7_lines = []
            capture = False
            for line in lines:
                if "TOPIC 8" in line:
                    capture = True
                if capture:
                    w7_lines.append(line)
            return "\n".join(w7_lines)
            
        return "Generic MOT MBA Lecture Context."
    except Exception:
        return "Management of Technology syllabus parameters."

# Gemini API Generator helper
def generate_questions_api(api_key, context, num_questions, session_title):
    prompt = f"""
    Generate exactly {num_questions} multiple-choice questions for the MBA Management of Technology class session: "{session_title}".
    Use the following verified slide syllabus context:
    ---
    {context}
    ---
    Requirements:
    1. Base the questions strictly on the slide content. Do not make up external facts.
    2. Format the response as a single valid JSON array. Each element should be an object with:
       - "text": The question string
       - "options": An array of 3-4 options
       - "correct": The correct option (must match one string in the options list exactly)
       - "explanation": Detailed explanation referencing slide guidelines
    3. Output raw JSON ONLY. Do not wrap in ```json code tags.
    """
    
    # Try google-genai SDK first
    try:
        from google import genai
        from google.genai import types
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.3
            )
        )
        return response.text
    except Exception:
        # Fallback to google-generativeai
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json", "temperature": 0.3}
            )
            return response.text
        except Exception as e:
            raise Exception(f"Failed to generate questions. Please verify your Gemini API key: {e}")

# Sidebar configurations
api_key_input = None
with st.sidebar:
    st.markdown("### 📋 Course Overview")
    st.markdown("""
    **Track:** MBA (Business Administration)  
    **Course:** Management of Technology (MOT)  
    **Lecturer:** Mr. Irfan  
    """)
    
    st.markdown("---")
    st.markdown("### 🔑 BYOK API Configurations")
    if "GEMINI_API_KEY" in st.secrets:
        st.success("🔒 Secure API Key loaded from Streamlit Secrets.")
    else:
        api_key_input = st.text_input("Gemini API Key:", type="password", help="Enter your Gemini API key to activate the AI Dynamic Practice Quiz generators.")
        
    st.markdown("---")
    st.markdown("### 🧭 Portal Focus")
    st.info("🎓 **MBA - COM 573**\n\nManagement of Technology\n\n*Binary University*")


    
    st.markdown("---")
    st.markdown("### 📈 Course Progress")
    progress = st.slider("Mark Syllabus Completed (%):", 0, 100, 71)
    st.progress(progress / 100)
    st.caption(f"{progress}% of total syllabus covered")

# Securely fetch API key from st.secrets or user input
api_key = None
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
if api_key_input:
    api_key = api_key_input

# Main Application Title
st.markdown('<div class="title-text">🎓 Management of Technology (MOT)</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Curriculum Portal & AI Practice Sandbox</div>', unsafe_allow_html=True)



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

# ─── QUIZ ENGINE RENDERER ───
def render_quiz(session_key, questions, is_dynamic=False):
    if is_dynamic:
        q_state = get_dynamic_quiz_state(session_key, len(questions))
        state_answers_key = f"dyn_ans_{session_key}"
        state_mode_key = f"dyn_mode_{session_key}"
        state_sub_key = f"dyn_sub_{session_key}"
    else:
        q_state = get_quiz_state(session_key, len(questions))
        state_answers_key = f"ans_{session_key}"
        state_mode_key = f"mode_{session_key}"
        state_sub_key = f"sub_{session_key}"
        
    col_ctrl, col_info = st.columns([2, 3])
    with col_ctrl:
        q_state["mode"] = st.radio(
            f"Select Quiz Mode:",
            ["Study Mode (Instant Feedback & Reveal)", "Exam Mode (Submit to Score)"],
            key=state_mode_key
        )
    with col_info:
        st.info("💡 **Study Mode:** Select options to see correct/incorrect alerts instantly, with options to reveal explanation tabs. \n\n🔒 **Exam Mode:** Answer all questions fully and click 'Submit Quiz' at the bottom to calculate your final grade.")

    st.markdown("---")
    
    correct_count = 0
    
    for idx, q in enumerate(questions):
        st.markdown(f"##### ❓ Question {idx+1}: {q['text']}")
        
        # User answer input
        prev_ans = q_state["answers"][idx]
        selected_option = st.radio(
            "Select one of the options:",
            q["options"],
            index=q["options"].index(prev_ans) if prev_ans in q["options"] else None,
            key=f"{state_answers_key}_{idx}",
            label_visibility="collapsed"
        )
        
        q_state["answers"][idx] = selected_option
        
        is_correct = selected_option == q["correct"]
        if is_correct:
            correct_count += 1
            
        # UI Response based on mode
        if q_state["mode"] == "Study Mode (Instant Feedback & Reveal)" and selected_option is not None:
            if is_correct:
                st.success("✅ **Correct!**")
            else:
                st.error(f"❌ **Incorrect.** The correct answer is: **{q['correct']}**")
            
            exp_tabs = st.tabs(["💡 Reveal Explanation", "🔑 Correct Answer"])
            with exp_tabs[0]:
                st.write(q["explanation"])
            with exp_tabs[1]:
                st.markdown(f"The correct option is: **{q['correct']}**")
        
        st.markdown("---")
        
    if q_state["mode"] == "Exam Mode (Submit to Score)":
        if not q_state["submitted"]:
            if st.button("Submit Quiz", key=state_sub_key):
                q_state["submitted"] = True
                st.rerun()
        else:
            score_pct = (correct_count / len(questions)) * 100
            st.markdown(f"#### 📊 Final Score: **{correct_count} / {len(questions)}** ({score_pct:.1f}%)")
            if score_pct >= 80.0:
                st.success("🎉 Excellent! You have mastered this session's concepts.")
            elif score_pct >= 50.0:
                st.warning("⚡ Good effort. Review the slides and try again to improve your score.")
            else:
                st.error("❌ Need revision. Check the study slide summary logs above.")
                
            if st.button("Retake Quiz", key=f"retake_{state_sub_key}"):
                q_state["submitted"] = False
                q_state["answers"] = [None] * len(questions)
                st.rerun()
                
            # Render answers post-submission
            st.markdown("### 📋 Detailed Assessment Feedback:")
            for idx, q in enumerate(questions):
                user_ans = q_state["answers"][idx]
                if user_ans == q["correct"]:
                    st.write(f"🟢 **Q{idx+1}: Correct** — Your answer: *{user_ans}*")
                else:
                    st.write(f"🔴 **Q{idx+1}: Incorrect** — Your answer: *{user_ans}* (Correct: *{q['correct']}*)")
                with st.expander(f"See Q{idx+1} Explanation", expanded=False):
                    st.write(q["explanation"])

# ─── DYNAMIC AI GENERATOR INTERFACE RENDERER ───
def render_ai_generator(session_index, session_title):
    st.markdown("#### 🤖 AI Dynamic Practice Test Generator")
    st.write("Construct customized practice tests using slide context dynamically fed to Google Gemini.")
    
    if not api_key:
        st.warning("🔑 Please enter your Gemini API Key in the sidebar to activate the AI Generator.")
        return
        
    num_q = st.number_input("Number of questions to generate (e.g. 5, 10, 30):", min_value=1, max_value=50, value=5, key=f"num_q_{session_index}")
    
    generate_btn = st.button("🌀 Generate Custom Quiz with Gemini", key=f"gen_btn_{session_index}")
    
    state_quiz_key = f"quiz_{session_index}"
    
    if generate_btn:
        with st.spinner("Gemini is analyzing slide blueprints and compiling questions..."):
            try:
                slide_context = load_slides_context(session_index)
                raw_json = generate_questions_api(api_key, slide_context, num_q, session_title)

                
                # Parse output
                parsed_questions = json.loads(raw_json)
                st.session_state.dynamic_quizzes[state_quiz_key] = parsed_questions
                
                # Clear previous answers
                state_key = f"dyn_{state_quiz_key}"
                st.session_state.dynamic_quiz_states[state_key] = {
                    "answers": [None] * len(parsed_questions),
                    "submitted": False,
                    "mode": "Study Mode"
                }
                
                st.success(f"Successfully generated {len(parsed_questions)} practice questions!")
            except Exception as e:
                st.error(f"Error generating quiz: {e}")
                
    # Display the quiz if it exists in state
    if state_quiz_key in st.session_state.dynamic_quizzes:
        st.markdown("### 📝 AI Generated Practice Test")
        render_quiz(state_quiz_key, st.session_state.dynamic_quizzes[state_quiz_key], is_dynamic=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1: WEEK 1 & WEEK 2 (SYSTEMS THINKING & REQUIREMENTS)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[0]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Standard Practice Quiz", "🤖 AI Dynamic Quiz"])
    
    with sub_tabs[0]:
        st.markdown('<div class="interactive-header"><h3>⚡ Systems Perspective & Requirement Engineering</h3></div>', unsafe_allow_html=True)
        
        col_l, col_r = st.columns([1, 1])
        
        with col_l:
            st.subheader("📚 Slide Curriculum Contents")
            
            with st.expander("📖 Week 1: Systems Thinking & Feedback Loops", expanded=True):
                st.markdown("""
                **The Systems Perspective**
                Organizations are interconnected webs. Managers must understand system functions and workflows before applying technology.
                
                **System Characteristics:**
                - **Components:** People, Process, Tech, Info, Governance.
                - **Relationships:** Workflows and connections.
                - **Boundaries:** Internal control vs. external parameters.
                - **Goals:** The unified objective components work toward.
                
                **Feedback Loops:**
                - *Positive (Reinforcing):* Drives growth (e.g. viral network adoption) or runaway panic.
                - *Negative (Balancing):* Corrects errors, maintaining stability (e.g. thermostat, inventory thresholds).
                """)
                
            with st.expander("📖 Week 2: Technology Planning & Requirements Analysis", expanded=False):
                st.markdown("""
                **Technology Management Planning**
                - Focus on solving real business problems, not chasing tech hype.
                - Avoid *Tech-First Thinking* (selecting tools before problems are scoped).
                
                **Syllabus Requirements Categories:**
                - **Functional:** *What* the system does (e.g. log transactions, track resources).
                - **Non-Functional:** *How* it performs (e.g. reliability, security, scalability).
                - **Human-Centered:** Simplicity, accessibility, and trust.
                """)
                
        with col_r:
            st.subheader("🎮 Interactive Sandbox: Feedback Loops & Trade Requirements")
            
            # Sandbox 1: Panic Buying Reinforcing Loop
            st.markdown("#### 🔄 Simulator: Panic Buying Reinforcing Loop")
            st.write("Simulate how positive feedback leads to system collapse, and how negative control loops restore balance.")
            
            loop_type = st.selectbox("Apply Stabilization Policy (Negative Loop):", ["None (Runaway Panic)", "Rationing Rules (Cap allocations)", "Price Ceiling Controls"])
            initial_panic = st.slider("Initial System Panic Level:", 1, 10, 3)
            
            panic = initial_panic
            stock = 100
            history = []
            
            for step in range(1, 6):
                if loop_type == "None (Runaway Panic)":
                    demand = panic * 8
                    panic += 2
                elif loop_type == "Rationing Rules (Cap allocations)":
                    demand = min(panic * 3, 15)
                    panic = max(1, panic - 1)
                else: # Price Ceiling
                    demand = panic * 5
                    panic = max(1, panic - 0.5)
                    
                stock = max(0, stock - demand)
                history.append({"Day": f"Day {step}", "Stock Reserves": stock, "Panic Level": panic})
                
            df_hist = pd.DataFrame(history)
            st.line_chart(df_hist.set_index("Day"))
            
            if stock == 0:
                st.error("🚨 System Failure: Food/Resource stock depleted due to runaway buying loop!")
            else:
                st.success("✅ System Stabilized: Reserves maintained through the balancing feedback loop.")
                
            st.markdown("---")
            
            # Sandbox 2: Requirements Classifier
            st.markdown("#### 📝 Lab: Requirements Classification Matrix")
            st.write("Drag/categorize the trade system requirements based on class definitions:")
            
            req_item = st.selectbox("Select Requirement Item to Classify:", [
                "1. Clerk must record every grain allocation.",
                "2. Access tokens must be encrypted.",
                "3. Ledger must support 10,000 active users.",
                "4. Portal screen must load in under 2 seconds.",
                "5. Ledger must be readable by local supervisors."
            ])
            
            user_class = st.radio("Choose correct category:", ["Functional Requirement", "Non-Functional: Security/Performance", "Human-Centered Design"])
            
            if "record every" in req_item and user_class == "Functional Requirement":
                st.success("🎯 Correct! Defining WHAT the system must do.")
            elif ("encrypted" in req_item or "active users" in req_item or "2 seconds" in req_item) and user_class == "Non-Functional: Security/Performance":
                st.success("🎯 Correct! Specifying operational quality/constraint.")
            elif "readable" in req_item and user_class == "Human-Centered Design":
                st.success("🎯 Correct! Ensuring usability and trust.")
            else:
                st.info("Try to categorize based on Slide 15-17 theory.")

    with sub_tabs[1]:
        w1_questions = [
            {
                "text": "What is the primary characteristic of a system as defined in the Week 1 slide context?",
                "options": [
                    "A set of isolated, completely independent hardware servers.",
                    "A set of interrelated components working together toward a common goal.",
                    "An ad-hoc collection of code packages."
                ],
                "correct": "A set of interrelated components working together toward a common goal.",
                "explanation": "As slide 5 emphasizes, a system is characterized by components (people, process, tech) working interactively to achieve a unified goal."
            },
            {
                "text": "Which type of feedback loop acts as a stability mechanism by correcting error deviations?",
                "options": [
                    "Positive (Reinforcing) Loop",
                    "Negative (Balancing) Loop",
                    "Linear Progression Loop"
                ],
                "correct": "Negative (Balancing) Loop",
                "explanation": "Balancing loops (negative feedback) maintain system equilibrium and correct fluctuations, while reinforcing loops drive runaway expansion or collapse."
            },
            {
                "text": "According to the technology management syllabus, what is the main risk of 'Tech-First Thinking'?",
                "options": [
                    "Selecting and buying software tools before identifying the actual business problem.",
                    "Using non-commercial open source databases.",
                    "Failing to backup data on local computers."
                ],
                "correct": "Selecting and buying software tools before identifying the actual business problem.",
                "explanation": "Slide 13 details that selecting solutions before scoping requirements is a common technology planning pitfall."
            },
            {
                "text": "Which of the following is categorized as a non-functional requirement?",
                "options": [
                    "The system must allow a clerk to log grain allocations.",
                    "The system must maintain 99% uptime availability during trade hours.",
                    "The system must print daily accounting summaries."
                ],
                "correct": "The system must maintain 99% uptime availability during trade hours.",
                "explanation": "Uptime and reliability define HOW a system operates under constraints, making it a non-functional requirement (Slide 17)."
            },
            {
                "text": "What is the primary difference between conceptual and technical system design?",
                "options": [
                    "Conceptual defines purpose, relationships, and business rules; technical defines code and database structures.",
                    "Conceptual is developer-facing; technical is manager-facing.",
                    "Conceptual focuses entirely on hardware; technical focuses on user profiles."
                ],
                "correct": "Conceptual defines purpose, relationships, and business rules; technical defines code and database structures.",
                "explanation": "Slide 21 clarifies that managers operate at the conceptual level to align strategy, while developers focus on the technical implementation level."
            }
        ]
        render_quiz("Session 1", w1_questions)

    with sub_tabs[2]:
        render_ai_generator(0, "Session 1: Weeks 1 & 2 Systems Thinking & Requirements")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2: WEEK 3 & WEEK 4 (SYSTEM DESIGN & ETHICS)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[1]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Standard Practice Quiz", "🤖 AI Dynamic Quiz"])
    
    with sub_tabs[0]:
        st.markdown('<div class="interactive-header"><h3>⚡ Business Systems Design & Ethical Governance</h3></div>', unsafe_allow_html=True)
        
        col_l, col_r = st.columns([1, 1])
        
        with col_l:
            st.subheader("📚 Slide Curriculum Contents")
            
            with st.expander("📖 Week 3: Systems Design & Problem Analysis", expanded=True):
                st.markdown("""
                **What is System Design?**
                - Transforms requirements into implementable blueprints.
                - **Conceptual Design:** Focuses on purpose, workflows, and relationship rules. (Manager-facing).
                - **Technical Design:** Focuses on database schema, APIs, and code structure. (Developer-facing).
                
                **Digital Transformation Roadmap Stages:**
                1. Manual Operations (paper-based)
                2. Organized Processes (standard operating procedures)
                3. Digital Records (databases/ledgers)
                4. Integrated Systems (connected departments)
                5. Intelligent Systems (analytics and AI support)
                """)
                
            with st.expander("📖 Week 4: Information Ethics, Data Protection & AI Support", expanded=False):
                st.markdown("""
                **Syllabus Ethics Guidelines:**
                - **Data Protection:** Safeguarding credentials, identity logs, and financial balances.
                - **AI and DSS:** Decisional assistants spot trends, but humans remain fully accountable.
                
                **The Ethical Checklist for Managers:**
                1. *Is it legal?* (Compliance)
                2. *Is it fair?* (Equity)
                3. *Is it necessary?* (Purpose & Scale)
                4. *What are the consequences?* (Risk/Benefit analysis)
                """)
                
        with col_r:
            st.subheader("🎮 Interactive Sandbox: Ethical Governance & AI Decision Maker")
            
            # Sandbox 1: Ethical Risk Evaluator
            st.markdown("#### ⚖️ Manager Tool: Ethical Assessment Matrix")
            st.write("Run a proposed technology deployment through the 4-Question Ethical Checklist.")
            
            proposal = st.selectbox("Proposed Deployment Scenario:", [
                "Workplace biometric scans to access trade ledgers",
                "AI automated rationing based on biometric data",
                "Public community trade logging board"
            ])
            
            q1 = st.checkbox("Q1: Is it compliant with local privacy laws/guidelines?")
            q2 = st.checkbox("Q2: Is it fair and free from system bias?")
            q3 = st.checkbox("Q3: Is this the minimum intrusion necessary to solve the problem?")
            q4 = st.checkbox("Q4: Do benefits outweigh long-term tracking risks?")
            
            score = sum([q1, q2, q3, q4])
            st.metric(label="Ethical Alignment Score", value=f"{score} / 4")
            
            if score == 4:
                st.success("🚀 Proposal APPROVED. Fully compliant with managerial ethics guidelines.")
            elif score >= 2:
                st.warning("⚠️ Revision needed. Integrate safeguards or reduce data scope.")
            else:
                st.error("❌ Proposal REJECTED. High ethical risk. Redesign system rules.")

    with sub_tabs[1]:
        w3_questions = [
            {
                "text": "What does conceptual systems design primarily focus on?",
                "options": [
                    "Writing compiler optimization flags.",
                    "Defining purpose, relationships, and business logic rules.",
                    "Configuring cloud load balancers."
                ],
                "correct": "Defining purpose, relationships, and business logic rules.",
                "explanation": "According to slide 21, conceptual design maps the core system structure and relationships for managerial alignment before coding."
            },
            {
                "text": "Under the Data Protection Act frameworks, what is a primary threat vector to evaluate for a database ledger?",
                "options": [
                    "Balance manipulation and unauthorized data monitoring.",
                    "Lack of CSS formatting options.",
                    "Slow page scrolling speeds."
                ],
                "correct": "Balance manipulation and unauthorized data monitoring.",
                "explanation": "Slide 24 details that data protection risks focus on data integrity (balance modification) and confidential access (surveillance)."
            },
            {
                "text": "In the digital transformation roadmap, what is the stage directly preceding 'Integrated Systems'?",
                "options": [
                    "Manual Operations",
                    "Digital Records",
                    "Intelligent Systems"
                ],
                "correct": "Digital Records",
                "explanation": "Slide 23 charts the roadmap stages: Manual -> Organized -> Digital Records -> Integrated Systems -> Intelligent Systems."
            },
            {
                "text": "What are the four components of the Ethical Decision Checklist in order?",
                "options": [
                    "Is it legal? Is it fair? Is it necessary? What are the consequences?",
                    "Is it cheap? Is it fast? Is it secure? Is it popular?",
                    "Who built it? Is it licensed? How is it hosted? Is it automated?"
                ],
                "correct": "Is it legal? Is it fair? Is it necessary? What are the consequences?",
                "explanation": "Slide 25 sets the checklist: Legal (policy), Fair (equity), Necessary (scale), and Consequences (risks)."
            },
            {
                "text": "What is the key rule for using Artificial Intelligence (AI) in Decision Support Systems (DSS)?",
                "options": [
                    "AI systems assume full management accountability for errors.",
                    "AI assists by spotting trends, but humans remain accountable.",
                    "AI replaces the database layer completely."
                ],
                "correct": "AI assists by spotting trends, but humans remain accountable.",
                "explanation": "Slide 38 states that AI should aid trend analysis, but humans remain accountable for final operational decisions."
            }
        ]
        render_quiz("Session 2", w3_questions)

    with sub_tabs[2]:
        render_ai_generator(1, "Session 2: Weeks 3 & 4 System Design & Ethics")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3: WEEK 5 & WEEK 6 (SDLC & EXECUTION)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[2]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Standard Practice Quiz", "🤖 AI Dynamic Quiz"])
    
    with sub_tabs[0]:
        st.markdown('<div class="interactive-header"><h3>⚡ Systems Development Life Cycle (SDLC) & Execution</h3></div>', unsafe_allow_html=True)
        
        col_l, col_r = st.columns([1, 1])
        
        with col_l:
            st.subheader("📚 Slide Curriculum Contents")
            
            with st.expander("📖 Week 5: SDLC Models & Suitability", expanded=True):
                st.markdown("""
                **System Development Life Cycle (SDLC)**
                Structured approach to plan, design, build, test, and maintain enterprise information networks.
                
                **Syllabus SDLC Models:**
                - **Waterfall Model:** Sequential, documentation-driven. Ideal for fixed regulations, stable currencies, and well-understood systems.
                - **Spiral Model:** Iterative, focusing on risk analysis. Ideal for highly complex, high-risk systems.
                - **Prototyping Model:** Rapid build-and-learn cycle. Ideal for experimental features with unclear requirements.
                - **Agile Model:** Highly flexible, user-feedback loop driven. Ideal for fast-changing requirements.
                """)
                
            with st.expander("📖 Week 6: IT Frameworks, TPS & DIKW Hierarchy", expanded=False):
                st.markdown("""
                **Information Processing Stack:**
                - **TPS (Transaction Processing Systems):** Records routine daily activities.
                - **DSS (Decision Support Systems):** Evaluates alternatives using TPS data.
                
                **The DIKW Hierarchy:**
                1. **Data:** Raw transactional facts (e.g. "Clerk logs 10 kg").
                2. **Information:** Structured reports (e.g. "Monthly grain storage trends").
                3. **Knowledge:** Actionable relationships (e.g. "Rain failure triggers 15% drop").
                4. **Wisdom:** Strategic management rules (e.g. "Enact emergency distribution").
                """)
                
        with col_r:
            st.subheader("🎮 Interactive Sandbox: SDLC Model Matcher & DIKW Builder")
            
            # Sandbox 1: SDLC Selector
            st.markdown("#### 🎯 Decision Tool: SDLC Suitability Matrix")
            st.write("Input your project parameters to identify the best lifecycle model.")
            
            req_stability = st.radio("Requirement Stability:", ["Completely Fixed & Policy-governed", "Iterative/Requires User Feedback", "Highly Uncertain & Risky"])
            time_limit = st.selectbox("Timeline Pressure:", ["Generous/Quality-focused", "Extremely urgent/Need immediate working prototype"])
            
            if req_stability == "Completely Fixed & Policy-governed" and time_limit == "Generous/Quality-focused":
                st.success("💡 Recommendation: **Waterfall Model**. Document-driven, highly structured, stable.")
            elif req_stability == "Iterative/Requires User Feedback" or time_limit == "Extremely urgent/Need immediate working prototype":
                st.success("💡 Recommendation: **Prototyping / Agile Model**. Rapid validation prevents user rejection.")
            else:
                st.success("💡 Recommendation: **Spiral Model**. Iterative risk audits manage complexity.")

    with sub_tabs[1]:
        w5_questions = [
            {
                "text": "Which SDLC model is sequential, requiring one phase to end completely before the next begins?",
                "options": [
                    "Prototyping Model",
                    "Agile Model",
                    "Waterfall Model"
                ],
                "correct": "Waterfall Model",
                "explanation": "The Waterfall model flows in one direction and requires complete documentation before transitions (Slide 8)."
            },
            {
                "text": "What is the primary operational focus of the Spiral SDLC model?",
                "options": [
                    "Continuous risk analysis and component assessment.",
                    "Creating rapid sketches of user interfaces.",
                    "Minimizing system developer testing."
                ],
                "correct": "Continuous risk analysis and component assessment.",
                "explanation": "Slide 9 highlights risk management as the core driver for the iterative quadrants in the Spiral model."
            },
            {
                "text": "In the DIKW hierarchy, what does 'Information' represent?",
                "options": [
                    "Raw, unstructured transaction facts.",
                    "Summarized trends and structured data relationships.",
                    "Strategic decisions made by leaders."
                ],
                "correct": "Summarized trends and structured data relationships.",
                "explanation": "Information adds structure and meaning to raw data facts, placing it directly above data in the hierarchy (Slide 37)."
            },
            {
                "text": "What is the core benefit of the Prototyping development model?",
                "options": [
                    "It ensures strict regulatory compliance checks.",
                    "It obtains early user feedback to clarify requirements and reduce risk.",
                    "It executes without requiring code compilation."
                ],
                "correct": "It obtains early user feedback to clarify requirements and reduce risk.",
                "explanation": "Prototyping prioritizes rapid build-and-learn loops to clarify user requirements (Slide 31)."
            },
            {
                "text": "Which system component logs daily, routine transaction records?",
                "options": [
                    "Decision Support System (DSS)",
                    "Transaction Processing System (TPS)",
                    "Bare-Metal Hypervisor"
                ],
                "correct": "Transaction Processing System (TPS)",
                "explanation": "TPS operates at the operational level, recording daily routine logs that form the foundation for metrics (Slide 37)."
            }
        ]
        render_quiz("Session 3", w5_questions)

    with sub_tabs[2]:
        render_ai_generator(2, "Session 3: Weeks 5 & 6 SDLC Models & Execution")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 4: WEEK 7 & WEEK 8 (HARDWARE & SEMICONDUCTORS)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[3]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Standard Practice Quiz", "🤖 AI Dynamic Quiz"])
    
    with sub_tabs[0]:
        st.markdown('<div class="interactive-header"><h3>⚡ Semiconductors, Digital Stack & Platforms</h3></div>', unsafe_allow_html=True)
        
        col_l, col_r = st.columns([1, 1])
        
        with col_l:
            st.subheader("📚 Slide Curriculum Contents")
            
            with st.expander("📖 Week 8: Semiconductors, Platforms & Cloud Stack", expanded=True):
                st.markdown("""
                **The Digital & Hardware Stack**
                1. **Applications (SaaS):** Frontend tools (e.g. Salesforce, Slack).
                2. **Cloud Infrastructure (IaaS/PaaS):** Compute/storage layers (AWS, Azure, GCP).
                3. **Telecommunication Networks:** 5G, fiber, satellite data relays.
                4. **Semiconductors (Chips):** Silicon CPUs, GPUs, memory. (The foundation).
                
                **Semiconductor Industry Dynamics:**
                - Chips power all modern computing infrastructure.
                - Silicon is the fundamental element (semi-conductor of electrical currents).
                - Key Players: Nvidia (GPU/AI), Intel (CPU), TSMC (Fabrication).
                
                **Telecom Regulations:**
                - Allocating radio bandwidth channels.
                - Local vs long-distance transmission limits.
                """)
                
        with col_r:
            st.subheader("🎮 Interactive Sandbox: Hardware-Cloud Stack Architect")
            
            st.markdown("#### ⚙️ Lab: Digital Stack Cost & Performance Builder")
            st.write("Configure the hardware/cloud layers for a company and review system capacity.")
            
            chip_tier = st.selectbox("Processor Chipset Tier:", ["Standard Core CPU (Low Overhead)", "Enterprise AI GPU/TPU (High performance)"])
            cloud_service = st.radio("Cloud Hosting Strategy:", ["IaaS (EC2/Azure VMs - Complete control)", "SaaS (Fully managed cloud services)"])
            user_scale = st.number_input("Target Monthly Active Users:", min_value=100, max_value=1000000, value=50000)
            
            # Capacity logic
            if chip_tier == "Standard Core CPU (Low Overhead)" and user_scale > 100000:
                st.error("⚠️ Chip bottlenecks detected! Standard CPUs cannot handle the query volume.")
            else:
                st.success("🚀 Stack configuration validated. Compute resources are balanced.")

    with sub_tabs[1]:
        w8_questions = [
            {
                "text": "What is the primary material used to manufacture microscopic computer chips?",
                "options": [
                    "Copper",
                    "Silicon",
                    "Rubber"
                ],
                "correct": "Silicon",
                "explanation": "Silicon is the fundamental semiconductor material used to construct computer chips (Slide 5)."
            },
            {
                "text": "Which layer sits directly between Telecommunication Networks and Applications in the digital stack?",
                "options": [
                    "Semiconductors",
                    "Cloud Infrastructure",
                    "Fiber Optics"
                ],
                "correct": "Cloud Infrastructure",
                "explanation": "Cloud Infrastructure (compute/storage) bridges telecommunication channels with client-facing applications (Slide 3)."
            },
            {
                "text": "Why is the semiconductor industry considered the foundation of the digital economy?",
                "options": [
                    "It manufactures the physical cables connecting routers.",
                    "Microscopic silicon chips are required to build processors for computers, EVs, and servers.",
                    "It registers global domain names."
                ],
                "correct": "Microscopic silicon chips are required to build processors for computers, EVs, and servers.",
                "explanation": "Without silicon chips, all hardware layers (laptops, datacenters, communication chips) grind to a halt (Slide 4)."
            },
            {
                "text": "What function does a semiconductor perform in an electrical circuit?",
                "options": [
                    "Acts as a pure electrical insulator.",
                    "Conducts electricity only under specific conditions, enabling control of electrical currents.",
                    "Eliminates network lag."
                ],
                "correct": "Conducts electricity only under specific conditions, enabling control of electrical currents.",
                "explanation": "Semiconductors operate between conductors and insulators to precisely regulate electrical flow (Slide 5)."
            },
            {
                "text": "Which cloud infrastructure deployment level provides raw compute resources, giving admins full root OS control?",
                "options": [
                    "SaaS (Software as a Service)",
                    "PaaS (Platform as a Service)",
                    "IaaS (Infrastructure as a Service)"
                ],
                "correct": "IaaS (Infrastructure as a Service)",
                "explanation": "IaaS provides bare compute VMs, requiring the client's sysadmin to configure the operating systems and software stack."
            }
        ]
        render_quiz("Session 4", w8_questions)

    with sub_tabs[2]:
        render_ai_generator(3, "Session 4: Weeks 7 & 8 Semiconductors, Platforms & Cloud Stack")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 5: WEEK 9 & WEEK 10 (PORTFOLIO GOVERNANCE)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[4]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Standard Practice Quiz", "🤖 AI Dynamic Quiz"])
    
    with sub_tabs[0]:
        st.markdown('<div class="interactive-header"><h3>⚡ Application Portfolio Management (APM) & Backlogs</h3></div>', unsafe_allow_html=True)
        
        col_l, col_r = st.columns([1, 1])
        
        with col_l:
            st.subheader("📚 Slide Curriculum Contents")
            
            with st.expander("📖 Week 9 & 10: APM, Prioritization & Backlog Management", expanded=True):
                st.markdown("""
                **Application Portfolio Management (APM)**
                Managers systematically classify software assets to optimize maintenance, upgrade pathways, or retire obsolete systems.
                
                **Key Decisions:**
                - **Maintenance vs Enhancement:** Patching bugs vs building new features.
                - **Cost of Change:** Changes late in the SDLC cost significantly more than early design adjustments.
                - **Governance:** Avoiding ad-hoc requests by prioritizing items using business case metrics.
                """)
                
        with col_r:
            st.subheader("🎮 Interactive Sandbox: Backlog Priority Matrix")
            
            st.markdown("#### 📊 Manager Tool: Strategic Backlog Prioritizer")
            st.write("Evaluate backlog features using Strategic Importance and Cost of Change to allocate resources.")
            
            col_bl1, col_bl2 = st.columns(2)
            with col_bl1:
                benefit = st.slider("Strategic Business Importance (1-10):", 1, 10, 8)
            with col_bl2:
                cost = st.slider("Development Cost / Complexity (1-10):", 1, 10, 3)
                
            priority = benefit - cost
            st.metric(label="Calculated Priority Score", value=priority)
            
            if priority >= 5:
                st.success("🔥 Priority: **High**. Schedule for the next development sprint.")
            elif priority >= 1:
                st.info("⚡ Priority: **Medium**. Keep in backlog for future sprint cycles.")
            else:
                st.warning("💤 Priority: **Low / Defer**. Resource investment does not align with business value.")

    with sub_tabs[1]:
        w9_questions = [
            {
                "text": "What is the primary goal of Application Portfolio Management (APM)?",
                "options": [
                    "To visually compile graphic UI assets.",
                    "To systematically categorize and govern software assets based on lifecycle and business value.",
                    "To write code comments."
                ],
                "correct": "To systematically categorize and govern software assets based on lifecycle and business value.",
                "explanation": "APM helps managers optimize maintenance budgets, retire legacy systems, and allocate development resources."
            },
            {
                "text": "According to the cost-of-change curve in project management, when is a mistake cheapest to fix?",
                "options": [
                    "During the early planning and design requirements phase.",
                    "During system integration testing.",
                    "After system deployment during maintenance."
                ],
                "correct": "During the early planning and design requirements phase.",
                "explanation": "Fixing defects early prevents cascading rework. The cost of changes scales exponentially later in the SDLC."
            }
        ]
        render_quiz("Session 5", w9_questions)

    with sub_tabs[2]:
        render_ai_generator(4, "Session 5: Weeks 9 & 10 Application Portfolios & Governance")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 6: WEEK 11 & WEEK 12 (ACQUISITION & E-BUSINESS)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[5]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Standard Practice Quiz", "🤖 AI Dynamic Quiz"])
    
    with sub_tabs[0]:
        st.markdown('<div class="interactive-header"><h3>⚡ System Acquisition & E-Business Systems</h3></div>', unsafe_allow_html=True)
        
        col_l, col_r = st.columns([1, 1])
        
        with col_l:
            st.subheader("📚 Slide Curriculum Contents")
            
            with st.expander("📖 Week 11 & 12: Buy vs Build & Network Zonation", expanded=True):
                st.markdown("""
                **System Acquisition Alternatives**
                - **Outsourcing:** Transferring development/operations to external partners.
                - **Buy vs. Build:**
                  - *Buy (SaaS):* Fast rollout, predictable license costs, vendor lock-in risk.
                  - *Build (Custom):* High upfront CapEx, competitive differentiation, custom fit.
                  
                **Intranets vs Extranets:**
                - **Intranet:** Internal private corporate network. High security restrictions.
                - **Extranet:** Shared network zone extending database access to partners/suppliers.
                """)
                
        with col_r:
            st.subheader("🎮 Interactive Sandbox: Buy vs Build Decision Grid")
            
            st.markdown("#### ⚖️ Manager Tool: Acquisition Selection matrix")
            st.write("Select the option matching your organizational constraints:")
            
            has_devs = st.checkbox("Company has an experienced internal software development team?")
            need_differentiation = st.checkbox("This application is the primary source of competitive advantage?")
            tight_timeline = st.checkbox("Timeline is extremely critical (Must launch in 30 days)?")
            
            if tight_timeline:
                st.success("💡 Verdict: **Buy SaaS Product**. Custom build takes too long; launch using pre-existing code.")
            elif has_devs and need_differentiation:
                st.success("💡 Verdict: **Build Custom System**. Maintain strategic control and IP value.")
            else:
                st.info("💡 Verdict: **Buy and Customize**. Leverage standard software, customizing workflows.")

    with sub_tabs[1]:
        w11_questions = [
            {
                "text": "What distinguishes an Extranet from an Intranet?",
                "options": [
                    "Intranets are open to customers, while Extranets are strictly internal.",
                    "Intranets are internal corporate networks, while Extranets extend secure access to trusted partners and suppliers.",
                    "Intranets are hosted without firewalls."
                ],
                "correct": "Intranets are internal corporate networks, while Extranets extend secure access to trusted partners and suppliers.",
                "explanation": "Intranets support internal collaboration, while Extranets link partners directly to select corporate systems (Topic 3)."
            },
            {
                "text": "What is a 'Digital Ecosystem' in an e-business context?",
                "options": [
                    "A disconnected spreadsheet collection.",
                    "A network of organizations, technologies, and users interacting via APIs to co-create digital value.",
                    "A local server rack enclosure."
                ],
                "correct": "A network of organizations, technologies, and users interacting via APIs to co-create digital value.",
                "explanation": "Digital ecosystems connect partners directly via API channels to co-create values on a platform (Topic 2)."
            },
            {
                "text": "Which metric defines the maximum acceptable data loss interval during a system disaster?",
                "options": [
                    "Recovery Time Objective (RTO)",
                    "Recovery Point Objective (RPO)",
                    "Mean Time to Recovery (MTTR)"
                ],
                "correct": "Recovery Point Objective (RPO)",
                "explanation": "RPO defines the maximum data loss window (e.g. losing 4 hours of transaction logs) that the business can survive."
            },
            {
                "text": "In change management, what is a primary cause of software deployment failures?",
                "options": [
                    "Incorrect formatting of database keys.",
                    "Poor management of user anxiety, training deficits, and workflow transition hurdles.",
                    "Slow network cables."
                ],
                "correct": "Poor management of user anxiety, training deficits, and workflow transition hurdles.",
                "explanation": "User adoption is the main barrier. Change frameworks mitigate user resistance during transition stages (Topic 7)."
            },
            {
                "text": "What does Cloud Governance primarily focus on?",
                "options": [
                    "Regulating physical cooling fans.",
                    "Financial cost containment, resource security, and cloud policy compliance.",
                    "Standardizing laptop keyboard layouts."
                ],
                "correct": "Financial cost containment, resource security, and cloud policy compliance.",
                "explanation": "Cloud governance establishes rules to optimize costs, enforce security, and ensure regulatory compliance (Topic 6)."
            }
        ]
        render_quiz("Session 6", w11_questions)

    with sub_tabs[2]:
        render_ai_generator(5, "Session 6: Weeks 11 & 12 System Acquisition & E-Business")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 7: WEEK 13 (CHANGE MANAGEMENT & CONTINUITY)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[6]:
    sub_tabs = st.tabs(["📖 Lecture Notes & Sandbox", "📝 Standard Practice Quiz", "🤖 AI Dynamic Quiz"])
    
    with sub_tabs[0]:
        st.markdown('<div class="interactive-header"><h3>⚡ Change Management & Business Continuity Planning (BCP)</h3></div>', unsafe_allow_html=True)
        
        col_l, col_r = st.columns([1, 1])
        
        with col_l:
            st.subheader("📚 Slide Curriculum Contents")
            
            with st.expander("📖 Week 13: BCP, Change Management & Resilience", expanded=True):
                st.markdown("""
                **Business Continuity Planning (BCP)**
                - Proactive planning to maintain operations in crisis.
                - **RTO (Recovery Time Objective):** Max acceptable downtime before recovery.
                - **RPO (Recovery Point Objective):** Max acceptable data loss interval.
                
                **Change Management Frameworks:**
                - Managing user anxiety, training, and operational transitions during new software rollouts.
                """)
                
        with col_r:
            st.subheader("🎮 Interactive Sandbox: RTO / RPO Cost Optimizer")
            
            st.markdown("#### 🚨 BCP Tool: Disaster Continuity Planner")
            st.write("Balance backup cost against potential data recovery losses to optimize BCP investments.")
            
            backup_frequency = st.selectbox("Select Backup Frequency:", ["Hourly", "Daily", "Weekly"])
            hosting_tiers = st.radio("Redundancy Zones:", ["Single Datacenter (Low cost)", "Multi-Region Cloud (High cost)"])
            
            # Cost math
            if backup_frequency == "Hourly":
                rpo_loss = 1.0 # hour
                backup_cost = 5000
            elif backup_frequency == "Daily":
                rpo_loss = 24.0 # hours
                backup_cost = 1000
            else:
                rpo_loss = 168.0 # hours (weekly)
                backup_cost = 200
                
            rto_downtime = 2.0 if "Multi-Region" in hosting_tiers else 24.0
            infra_cost = 4000 if "Multi-Region" in hosting_tiers else 500
            
            st.write(f"**Calculated Metrics:**")
            st.write(f"▸ RPO Data Loss Risk: **{rpo_loss} Hours**")
            st.write(f"▸ RTO Recovery Downtime: **{rto_downtime} Hours**")
            st.metric(label="Total BCP Infrastructure Cost ($/year)", value=f"${backup_cost + infra_cost}")

    with sub_tabs[1]:
        w13_questions = [
            {
                "text": "What is the primary purpose of a Business Continuity Plan (BCP)?",
                "options": [
                    "Decreasing physical hardware purchase tax.",
                    "Mitigating business risks to maintain operational viability during a system crisis.",
                    "Increasing processor clockspeed."
                ],
                "correct": "Mitigating business risks to maintain operational viability during a system crisis.",
                "explanation": "BCP protects operations by defining roles, recovery tools, and failover steps when disasters occur."
            },
            {
                "text": "Which parameter specifies the maximum acceptable duration to restore systems after a service crash?",
                "options": [
                    "Recovery Point Objective (RPO)",
                    "Recovery Time Objective (RTO)",
                    "Mean Time Between Failures (MTBF)"
                ],
                "correct": "Recovery Time Objective (RTO)",
                "explanation": "RTO focuses strictly on time-to-restore boundaries (e.g. restoring operations within 2 hours of a power loss)."
            }
        ]
        render_quiz("Session 7", w13_questions)

    with sub_tabs[2]:
        render_ai_generator(6, "Session 7: Week 13 BCP, Change Management & Resilience")
