import streamlit as st
import pandas as pd
from utils import render_quiz
from data_store import (
    SESSION_1_QUIZ,
    SESSION_2_QUIZ,
    SESSION_3_QUIZ,
    SESSION_4_QUIZ,
    SESSION_5_QUIZ,
    SESSION_6_QUIZ,
    SESSION_7_QUIZ,
)

def render_session_1(sub_tabs):
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
        render_quiz("Session 1", SESSION_1_QUIZ)

def render_session_2(sub_tabs):
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
        render_quiz("Session 2", SESSION_2_QUIZ)

def render_session_3(sub_tabs):
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
        render_quiz("Session 3", SESSION_3_QUIZ)

def render_session_4(sub_tabs):
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
        render_quiz("Session 4", SESSION_4_QUIZ)

def render_session_5(sub_tabs):
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
        render_quiz("Session 5", SESSION_5_QUIZ)

def render_session_6(sub_tabs):
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
        render_quiz("Session 6", SESSION_6_QUIZ)

def render_session_7(sub_tabs):
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
        render_quiz("Session 7", SESSION_7_QUIZ)
