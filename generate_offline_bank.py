import os
import orjson

def generate_week1():
    return {
        "week": 1,
        "title": "Systems Thinking & Information as a Strategic Asset",
        "questions": [
            # 10 MCQ
            {
                "id": "w1_q1", "type": "mcq",
                "question": "Which of the following best defines a 'system' within the context of technology management?",
                "choices": [
                    "A standalone server running compiled operating system binaries.",
                    "A set of interrelated components (people, process, technology) working together to achieve a common goal.",
                    "An ad-hoc group of software scripts without defined data models.",
                    "A pure hardware network switch configuration."
                ],
                "answer": 1,
                "explanation": "A system is defined by its components (people, process, technology, governance) working together towards a common goal."
            },
            {
                "id": "w1_q2", "type": "mcq",
                "question": "What is the primary role of a balancing (negative) feedback loop in a control system?",
                "choices": [
                    "To accelerate the growth rate of system outputs exponentially.",
                    "To maintain equilibrium and correct deviations from the system goal.",
                    "To eliminate the boundaries between internal and external environments.",
                    "To log transaction operations for audit purposes."
                ],
                "answer": 1,
                "explanation": "Negative feedback loops act as error-correctors and maintain equilibrium (like a thermostat)."
            },
            {
                "id": "w1_q3", "type": "mcq",
                "question": "Which system interdependency conflict is most likely when introducing a new Payroll System?",
                "choices": [
                    "HR updates files, but Finance faces budget reconciliation and cash liquidity constraints.",
                    "The operating system halts compilation due to security encryption keys.",
                    "The database index duplicates key values.",
                    "The network mesh runs out of backup power batteries."
                ],
                "answer": 0,
                "explanation": "Introducing payroll affects HR, Finance (liquidity), IT (mesh networks), and employees (trust)."
            },
            {
                "id": "w1_q4", "type": "mcq",
                "question": "Why is information considered a strategic asset in modern organizational system theories?",
                "choices": [
                    "It has physical depreciation schedules similar to factory buildings.",
                    "It can be traded directly on open commodity exchanges as gold.",
                    "It reduces operational risk and enables managers to coordinate complex logistics quickly.",
                    "It replaces the need for local database storage structures."
                ],
                "answer": 2,
                "explanation": "Information assets reduce uncertainty and improve resource coordination speeds."
            },
            {
                "id": "w1_q5", "type": "mcq",
                "question": "A reinforcing (positive) feedback loop is characterized by which system behavior?",
                "choices": [
                    "Stable, flat-line equilibrium metrics.",
                    "Dampened oscillations that settle to a target temperature.",
                    "Runaway exponential growth or accelerating system collapse.",
                    "Immediate shutdown of all mesh routing protocols."
                ],
                "answer": 2,
                "explanation": "Positive feedback loops reinforce changes, causing runaway growth or catastrophic collapse."
            },
            {
                "id": "w1_q6", "type": "mcq",
                "question": "What are the core components of any system boundary?",
                "choices": [
                    "The separation between what is inside vs. outside the system's control.",
                    "The physical ethernet cables linking local routing hubs.",
                    "The backup policies for local database recovery blocks.",
                    "The division between junior programmers and management directors."
                ],
                "answer": 0,
                "explanation": "System boundaries define the scope of what is inside the controller's authority versus the external environment."
            },
            {
                "id": "w1_q7", "type": "mcq",
                "question": "In systems thinking, what does the term 'symptom-solving' refer to?",
                "choices": [
                    "Identifying database query bottlenecks and optimizing indexes.",
                    "Solving immediate visible problems without addressing underlying structural causes.",
                    "Rebuilding electrical solar cells after battery failures.",
                    "Implementing strict code validation routines."
                ],
                "answer": 1,
                "explanation": "Symptom-solving is a common management pitfall where superficial fixes are applied instead of addressing structural system issues."
            },
            {
                "id": "w1_q8", "type": "mcq",
                "question": "Which of the following describes 'Information' in the context of organizational resources?",
                "choices": [
                    "Raw, unorganized transaction numbers.",
                    "Structured, meaningful data that directly supports digital decisions.",
                    "Physical metal bullion stored in security vaults.",
                    "Code compilers running on local servers."
                ],
                "answer": 1,
                "explanation": "Information adds structure and context to raw data, rendering it valuable for decision support."
            },
            {
                "id": "w1_q9", "type": "mcq",
                "question": "What is a major risk of a highly interconnected system without partition controls?",
                "choices": [
                    "Lack of database logging fields.",
                    "Changes in one small component can cascade into widespread system-wide failures.",
                    "Total loss of network interface cards.",
                    "High costs of printing paper documents."
                ],
                "answer": 1,
                "explanation": "Interconnection means local failures can cascade globally across the system (unintended consequences)."
            },
            {
                "id": "w1_q10", "type": "mcq",
                "question": "How do managers make strategic decisions in digital decision environments?",
                "choices": [
                    "By delegating all data queries to system administrators.",
                    "By interpreting structured data trends and weighing system risks rather than only looking at coding details.",
                    "By configuring database query optimization parameters.",
                    "By manually writing software scripts."
                ],
                "answer": 1,
                "explanation": "Managers must understand what systems can do and identify risks without needing to write code."
            },
            
            # 5 True/False
            {
                "id": "w1_q11", "type": "tf",
                "question": "A system's performance depends entirely on its individual components, not how they interact.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. System performance depends heavily on the interactions and relationships between components."
            },
            {
                "id": "w1_q12", "type": "tf",
                "question": "Panic buying is a classic example of a reinforcing (positive) feedback loop that can crash a supply system.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Shortages cause panic, leading to hoarding, which worsens the shortages—an escalating reinforcing loop."
            },
            {
                "id": "w1_q13", "type": "tf",
                "question": "Without information assets, it is impossible to coordinate resource distribution or prevent hoarding in a crisis.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Information coordinates operations and balances physical demand and supply constraints."
            },
            {
                "id": "w1_q14", "type": "tf",
                "question": "Balancing feedback loops drive a system away from stability into runaway growth.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Balancing loops correct deviations and stabilize systems, while reinforcing loops drive runaway changes."
            },
            {
                "id": "w1_q15", "type": "tf",
                "question": "A new IT system can affect HR, Finance, and employees even if they don't use the software directly.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Organizational systems are interconnected; change in one area cascades to other departments."
            },
            
            # 5 Fill in the Blanks
            {
                "id": "w1_q16", "type": "fitb",
                "question": "A system is defined as a set of __________ components working together toward a common goal.",
                "answer": "interrelated",
                "explanation": "Interrelation is the key feature of system components working interactively."
            },
            {
                "id": "w1_q17", "type": "fitb",
                "question": "A feedback loop that maintains system stability and equilibrium is a __________ loop.",
                "answer": "balancing",
                "explanation": "Balancing (or negative) feedback loops stabilize the system."
            },
            {
                "id": "w1_q18", "type": "fitb",
                "question": "A feedback loop that causes runaway expansion or collapse is a __________ loop.",
                "answer": "reinforcing",
                "explanation": "Reinforcing (or positive) feedback loops drive runaway behaviors."
            },
            {
                "id": "w1_q19", "type": "fitb",
                "question": "Data that has been processed, structured, and organized to add value is called __________.",
                "answer": "information",
                "explanation": "Information is data with context, structure, and strategic meaning."
            },
            {
                "id": "w1_q20", "type": "fitb",
                "question": "The boundary of a system defines what is inside versus outside of the system's __________.",
                "answer": "control",
                "explanation": "Boundaries divide internal elements within system control from external environmental variables."
            },
            
            # 3 Match
            {
                "id": "w1_q21", "type": "match",
                "question": "Match each organizational component to its core definition:",
                "left_items": ["People", "Process", "Technology", "Governance"],
                "right_items": ["Workflows and rules", "Users and stakeholders", "Hardware and databases", "Audit and policies"],
                "answer": {
                    "People": "Users and stakeholders",
                    "Process": "Workflows and rules",
                    "Technology": "Hardware and databases",
                    "Governance": "Audit and policies"
                },
                "explanation": "System components map to roles: People (users), Process (workflows), Tech (hardware), Governance (audit/policies)."
            },
            {
                "id": "w1_q22", "type": "match",
                "question": "Match the loop example with its feedback type:",
                "left_items": ["Rationing limits", "Panic buying hoard", "Thermostat cooling"],
                "right_items": ["Balancing loop", "Reinforcing loop", "Linear process"],
                "answer": {
                    "Rationing limits": "Balancing loop",
                    "Panic buying hoard": "Reinforcing loop",
                    "Thermostat cooling": "Balancing loop"
                },
                "explanation": "Panic buying is reinforcing; rationing and thermostats are balancing (corrective)."
            },
            {
                "id": "w1_q23", "type": "match",
                "question": "Match the asset class to its example resource:",
                "left_items": ["Physical Asset", "Information Asset", "Financial Asset"],
                "right_items": ["Warehouse buildings", "Transaction audit logs", "Gold standard coins"],
                "answer": {
                    "Physical Asset": "Warehouse buildings",
                    "Information Asset": "Transaction audit logs",
                    "Financial Asset": "Gold standard coins"
                },
                "explanation": "Physical assets are material; information assets are data/records; financial assets represent currency/value."
            },
            
            # 2 Scenarios
            {
                "id": "w1_q24", "type": "scenario",
                "scenario": "A post-collapse settlement attempts to restart trade. To maintain stability, the community leaders build a central database to track crop stocks, but they do not establish transport logistics or define trading hours. Farmers dump crops at closed depots, causing them to spoil, while city residents face immediate starvation.",
                "question": "Which systems thinking concept explains this failure?",
                "choices": [
                    "Lack of high-speed fiber cables.",
                    "Failing to recognize system interdependencies between inventory data and physical logistics.",
                    "The reinforcing loop of food storage optimization.",
                    "Software compiler compatibility issues."
                ],
                "answer": 1,
                "explanation": "Systems thinking requires mapping the interdependencies between database records (inventory) and physical components (transportation, scheduling)."
            },
            {
                "id": "w1_q25", "type": "scenario",
                "scenario": "A local community leader notices food reserves are dropping. To solve this, she immediately opens the emergency reserves without changing the distribution rules. This causes a massive buying spike where families purchase more than they need, resulting in total depletion of the emergency stock in 48 hours.",
                "question": "What feedback loop error did the leader make?",
                "choices": [
                    "She applied a balancing control when she should have used a reinforcing loop.",
                    "She treated a symptom (reserves drop) without changing consumption rules, triggering a reinforcing panic buying loop.",
                    "She spent too much time compiling hardware assets.",
                    "She configured the server database backup files incorrectly."
                ],
                "answer": 1,
                "explanation": "Releasing stocks without rule changes reinforces the hoarding panic buying loop, which empties reserves completely."
            }
        ]
    }

def generate_week2():
    return {
        "week": 2,
        "title": "Technology Planning & Requirements Gathering",
        "questions": [
            # 10 MCQ
            {
                "id": "w2_q1", "type": "mcq",
                "question": "What is the core mistake of 'Tech-First Thinking' in technology planning?",
                "choices": [
                    "Purchasing a software tool before identifying the actual business problem.",
                    "Using open-source software libraries.",
                    "Relying on local area networks instead of cloud databases.",
                    "Hiring developers before writing HTML stylesheets."
                ],
                "answer": 0,
                "explanation": "Tech-First Thinking forces popular or expensive tools on an organization without scoping real requirements first."
            },
            {
                "id": "w2_q2", "type": "mcq",
                "question": "Which of the following defines a functional requirement in systems design?",
                "choices": [
                    "The system must load pages in under 1 second.",
                    "The system database must encrypt all password fields.",
                    "The system must allow traders to check inventory stock balances.",
                    "The system must achieve 99.9% uptime."
                ],
                "answer": 2,
                "explanation": "Functional requirements define WHAT a system must do (functions, data inputs/outputs)."
            },
            {
                "id": "w2_q3", "type": "mcq",
                "question": "Which parameter describes a non-functional requirement?",
                "choices": [
                    "Allow a supervisor to delete a transaction.",
                    "Print daily tax audit summaries.",
                    "Ensure the platform remains operational during power-grid down times (reliability).",
                    "Record farmer name and grain weight."
                ],
                "answer": 2,
                "explanation": "Non-functional requirements specify quality constraints on HOW the system operates."
            },
            {
                "id": "w2_q4", "type": "mcq",
                "question": "Which requirement gathering method is best for understanding how employees currently perform tasks manually?",
                "choices": [
                    "Distributing anonymous email surveys.",
                    "Direct observation of workflows.",
                    "Reviewing developer API documentation.",
                    "Running automatic database diagnostic checks."
                ],
                "answer": 1,
                "explanation": "Direct observation reveals the raw reality of how tasks are run without relying on user memory."
            },
            {
                "id": "w2_q5", "type": "mcq",
                "question": "Why is stakeholder involvement critical during the requirements phase?",
                "choices": [
                    "It speeds up code compilation times.",
                    "Different stakeholder groups have different, sometimes conflicting, system requirements.",
                    "It eliminates the need for database index optimization.",
                    "It allows managers to avoid writing technical documentation."
                ],
                "answer": 1,
                "explanation": "Stakeholders (farmers, traders, managers) have unique requirements that must be balanced during system design."
            },
            {
                "id": "w2_q6", "type": "mcq",
                "question": "What does a business capability analysis attempt to map?",
                "choices": [
                    "The programming syntax choices for frontend layout.",
                    "What an organization must do to survive and execute its strategy.",
                    "The speed of network packets across mesh lines.",
                    "The storage capacity of secondary backup drives."
                ],
                "answer": 1,
                "explanation": "Capability analysis links technology strategy to core business execution needs."
            },
            {
                "id": "w2_q7", "type": "mcq",
                "question": "Which characteristic defines a human-centered system requirement?",
                "choices": [
                    "Maximum CPU clock speed configuration.",
                    "Usability, accessibility, simplicity, and user trust.",
                    "Minimum network cable resistance parameters.",
                    "Low server hosting fees."
                ],
                "answer": 1,
                "explanation": "Human-centered design focuses on user adoption, simplicity, trust, and ease of learning."
            },
            {
                "id": "w2_q8", "type": "mcq",
                "question": "What is the primary risk of vendor-driven technology decisions?",
                "choices": [
                    "Software providers might define business processes based on what their tool does, rather than business needs.",
                    "The software will compile into unreadable machine binaries.",
                    "The database will run out of space for new users.",
                    "Users will bypass the login credentials."
                ],
                "answer": 0,
                "explanation": "Vendor-driven planning allows suppliers to dictate business design based on pre-packaged features."
            },
            {
                "id": "w2_q9", "type": "mcq",
                "question": "Which metric evaluates system scalability?",
                "choices": [
                    "The system must encrypt all user passwords.",
                    "The system must load transaction histories within 3 seconds.",
                    "The system must support growth from 100 to 10,000 active users without degrading performance.",
                    "The system must allow reports to be printed as PDF."
                ],
                "answer": 2,
                "explanation": "Scalability is a non-functional constraint regarding how a system adapts to increased operational load."
            },
            {
                "id": "w2_q10", "type": "mcq",
                "question": "What is the correct flow for digital strategy planning?",
                "choices": [
                    "Buy software ➔ Code database ➔ Identify requirements.",
                    "Identify business problem ➔ Scope requirements ➔ Evaluate options ➔ Aligned software choice.",
                    "Hire developers ➔ Run beta test ➔ Define target capability.",
                    "Deploy code ➔ Write user manuals ➔ Audit system requirements."
                ],
                "answer": 1,
                "explanation": "Planning must flow from problem discovery to requirement analysis before selecting software."
            },
            
            # 5 True/False
            {
                "id": "w2_q11", "type": "tf",
                "question": "A technically flawless system is a success even if target users refuse to adopt it.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. User adoption is the ultimate metric of system success; human requirements must be met."
            },
            {
                "id": "w2_q12", "type": "tf",
                "question": "Functional requirements define what the system does, while non-functional requirements define how it operates.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Functional is behavior (logins, reports); non-functional is quality constraints (uptime, security)."
            },
            {
                "id": "w2_q13", "type": "tf",
                "question": "Purchasing a popular CRM platform before identifying corporate customer needs is a correct planning practice.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. This is a classic 'Solution-Before-Problem' pitfall (Tech-First Thinking)."
            },
            {
                "id": "w2_q14", "type": "tf",
                "question": "Direct observation can reveal requirement details that users might forget to mention in interviews.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Observing actual workflows spots inefficiencies and undocumented workarounds."
            },
            {
                "id": "w2_q15", "type": "tf",
                "question": "Security constraints on database access are classified as functional requirements.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Security is a non-functional quality constraint regarding system governance."
            },
            
            # 5 Fill in the Blanks
            {
                "id": "w2_q16", "type": "fitb",
                "question": "Selecting a software solution before identifying the actual business problem is called __________-first thinking.",
                "answer": "technology",
                "explanation": "Technology-first (or tech-first) thinking is a major strategic planning mistake."
            },
            {
                "id": "w2_q17", "type": "fitb",
                "question": "Requirements that specify quality constraints (like uptime, scalability, and security) are __________ requirements.",
                "answer": "non-functional",
                "explanation": "Non-functional requirements govern how the system behaves under performance constraints."
            },
            {
                "id": "w2_q18", "type": "fitb",
                "question": "Anyone who is affected by, or involved in, the implementation of a new system is a __________.",
                "answer": "stakeholder",
                "explanation": "Stakeholders include users, administrators, clients, and developers."
            },
            {
                "id": "w2_q19", "type": "fitb",
                "question": "Observing workflows directly to gather system needs is a __________-driven requirements method.",
                "answer": "data",
                "explanation": "Observation, surveys, and logs provide objective data-driven inputs."
            },
            {
                "id": "w2_q20", "type": "fitb",
                "question": "The design dimension that ensures users trust that records are stored fairly is called __________.",
                "answer": "trust",
                "explanation": "Trust is a central human-centered requirement for community adoption."
            },
            
            # 3 Match
            {
                "id": "w2_q21", "type": "match",
                "question": "Match the requirement example to its proper classification:",
                "left_items": ["System must load page within 2s", "System must save transaction record", "System must encrypt user balances"],
                "right_items": ["Non-Functional (Performance)", "Functional (Feature)", "Non-Functional (Security)"],
                "answer": {
                    "System must load page within 2s": "Non-Functional (Performance)",
                    "System must save transaction record": "Functional (Feature)",
                    "System must encrypt user balances": "Non-Functional (Security)"
                },
                "explanation": "Performance and security define qualities (non-functional), while saving records is a system action (functional)."
            },
            {
                "id": "w2_q22", "type": "match",
                "question": "Match the stakeholder profile to their primary system concern:",
                "left_items": ["Trade Clerks", "Logistics Teams", "Security Officers"],
                "right_items": ["Fast transaction logging", "Route capacity tracking", "Preventing balance editing"],
                "answer": {
                    "Trade Clerks": "Fast transaction logging",
                    "Logistics Teams": "Route capacity tracking",
                    "Security Officers": "Preventing balance editing"
                },
                "explanation": "Each stakeholder has target operational priorities within the system design."
            },
            {
                "id": "w2_q23", "type": "match",
                "question": "Match the gathering source to its description:",
                "left_items": ["Interviews", "Transaction logs", "Observation"],
                "right_items": ["Deep dialogs with leaders", "Analyzing database entries", "Watching manual trade tasks"],
                "answer": {
                    "Interviews": "Deep dialogs with leaders",
                    "Transaction logs": "Analyzing database entries",
                    "Observation": "Watching manual trade tasks"
                },
                "explanation": "Interviews gather qualitative views; logs extract data records; observation audits actions."
            },
            
            # 2 Scenarios
            {
                "id": "w2_q24", "type": "scenario",
                "scenario": "An IT manager in the kingdom buys a complex ERP software from a traveling salesman because it has advanced analytics. When deployed, the trade clerks find it requires high-power processors they don't have, and the interface is too complex for them to input transaction lines quickly. They return to manual paper notebooks.",
                "question": "Which requirement gathering pitfall is shown here?",
                "choices": [
                    "Failure to configure network interfaces.",
                    "Failing to evaluate human usability constraints and hardware limitations during the planning phase.",
                    "Using database structures that are too small.",
                    "Choosing open-source code libraries."
                ],
                "answer": 1,
                "explanation": "Failing to check hardware constraints and user usability needs leads to immediate system rejection."
            },
            {
                "id": "w2_q25", "type": "scenario",
                "scenario": "A development team designs an online food order ledger. They document that the software must allow users to select items and pay. However, they do not state that the portal must recover from grid downtime within 10 minutes. During the first storm, the system fails and remains offline for 3 days, spoiling all local dairy shipments.",
                "question": "What type of specification error occurred?",
                "choices": [
                    "The team forgot to specify functional features.",
                    "The team failed to define critical non-functional reliability requirements (recovery times).",
                    "They coded the frontend pages in incorrect CSS files.",
                    "They used incorrect database indexing tools."
                ],
                "answer": 1,
                "explanation": "Omitting non-functional recovery limits (like RTO) makes systems highly vulnerable to operational disasters."
            }
        ]
    }

def generate_week3():
    return {
        "week": 3,
        "title": "Systems Design & Digital Transformation",
        "questions": [
            # 10 MCQ
            {
                "id": "w3_q1", "type": "mcq",
                "question": "What is the primary difference between conceptual and technical system design?",
                "choices": [
                    "Conceptual defines purpose, relationships, and business rules; technical defines code structures and database schemes.",
                    "Conceptual design is for developers; technical design is for business clients.",
                    "Conceptual focus is strictly on hardware specs; technical design maps organization charts.",
                    "Conceptual design happens after deployment; technical design is done in planning."
                ],
                "answer": 0,
                "explanation": "Conceptual design aligns managers on rules and relationships, while technical design is the developers' code blueprint (Slide 21)."
            },
            {
                "id": "w3_q2", "type": "mcq",
                "question": "In the Digital Transformation Roadmap, what is Stage 3?",
                "choices": [
                    "Manual Operations",
                    "Digital Records (isolated ledgers)",
                    "Integrated Systems (connected departments)",
                    "Intelligent Systems"
                ],
                "answer": 1,
                "explanation": "The roadmap flows: 1. Manual -> 2. Organized -> 3. Digital Records -> 4. Integrated Systems -> 5. Intelligent Systems."
            },
            {
                "id": "w3_q3", "type": "mcq",
                "question": "Which of the following represents a business capability in system design?",
                "choices": [
                    "The system must use standard SQL queries.",
                    "The system must load in 1 second.",
                    "The organizational capacity to track and reconcile gold standard transactions.",
                    "A specific python-docx code package."
                ],
                "answer": 2,
                "explanation": "Capabilities represent what an organization does to execute strategy (e.g. inventory tracking, auditing)."
            },
            {
                "id": "w3_q4", "type": "mcq",
                "question": "Why does a manager define system architecture diagrams?",
                "choices": [
                    "To generate code files automatically.",
                    "To map out the relationships between people, processes, technology, and data boundaries.",
                    "To verify ethernet cable resistance metrics.",
                    "To compute employee tax rates."
                ],
                "answer": 1,
                "explanation": "System architecture maps connections and data paths to highlight dependencies and prevent system bottlenecks."
            },
            {
                "id": "w3_q5", "type": "mcq",
                "question": "Which stage on the digital transformation roadmap must a post-collapse society target first?",
                "choices": [
                    "Stage 5: Intelligent Systems",
                    "Stage 1: Manual Operations (stable workflows)",
                    "Stage 4: Integrated Systems",
                    "Stage 3: Digital Records"
                ],
                "answer": 1,
                "explanation": "Before digitizing, stable workflows must be built manually and organized (Stages 1 and 2)."
            },
            {
                "id": "w3_q6", "type": "mcq",
                "question": "What does 'Digital Records' signify in transformation planning?",
                "choices": [
                    "Fully automated AI networks.",
                    "Storing data in isolated local databases rather than manual paper logs.",
                    "Eliminating all regional cache servers.",
                    "Relying strictly on verbal trade agreements."
                ],
                "answer": 1,
                "explanation": "Digital records digitize single assets locally before linking them into integrated pipelines."
            },
            {
                "id": "w3_q7", "type": "mcq",
                "question": "What is a main limitation of isolated 'Digital Records' (Stage 3)?",
                "choices": [
                    "No database backup exists.",
                    "Systems cannot share data easily across different departments (data silos).",
                    "High cost of solar power units.",
                    "Difficulty in compiling python-pptx."
                ],
                "answer": 1,
                "explanation": "Stage 3 creates database silos; Stage 4 (Integrated Systems) is needed to connect departments."
            },
            {
                "id": "w3_q8", "type": "mcq",
                "question": "Which design component governs how data moves between departments?",
                "choices": [
                    "Process and integration maps.",
                    "HTML stylesheet files.",
                    "Standard hypervisor configurations.",
                    "The layout of server cooling fans."
                ],
                "answer": 0,
                "explanation": "Process and integration maps trace how data flows across organizational boundaries."
            },
            {
                "id": "w3_q9", "type": "mcq",
                "question": "What occurs when you automate a broken manual process?",
                "choices": [
                    "The process stabilizes instantly.",
                    "You speed up and amplify the errors in the system.",
                    "You eliminate the need for system maintenance.",
                    "The hardware requirements drop."
                ],
                "answer": 1,
                "explanation": "Management Rule: Technology supports business needs. Automating a broken manual process just produces faster failures."
            },
            {
                "id": "w3_q10", "type": "mcq",
                "question": "Which design pillar is required to ensure trust in trade records?",
                "choices": [
                    "Using high-frequency wireless routers.",
                    "Defining clear business logic rules and keeping unalterable audit trails.",
                    "Configuring standard color layouts.",
                    "Bypassing all regulator roles."
                ],
                "answer": 1,
                "explanation": "Trust is established through transparent validation rules and secure audit logs."
            },
            
            # 5 True/False
            {
                "id": "w3_q11", "type": "tf",
                "question": "Conceptual system design focus is primarily code, database layouts, and API integrations.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Conceptual design focuses on purpose, rules, and relationships; technical design handles code and schema details."
            },
            {
                "id": "w3_q12", "type": "tf",
                "question": "Stage 4 of digital transformation links different departmental databases together.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Stage 4 is Integrated Systems, where departmental databases are connected."
            },
            {
                "id": "w3_q13", "type": "tf",
                "question": "A system architecture map should show how data, people, and processes connect.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. An architecture map integrates all system dimensions to evaluate dependencies."
            },
            {
                "id": "w3_q14", "type": "tf",
                "question": "A business system is stable even if you remove its governance or rule component.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Removing any system component (People, Process, Tech, Governance) degrades system performance."
            },
            {
                "id": "w3_q15", "type": "tf",
                "question": "Isolated digital databases are classified as Stage 5 (Intelligent Systems) on the roadmap.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Isolated databases are Stage 3 (Digital Records). Stage 5 features smart alerts and analytics."
            },
            
            # 5 Fill in the Blanks
            {
                "id": "w3_q16", "type": "fitb",
                "question": "The design stage that maps out system purpose and business logic before coding is called __________ design.",
                "answer": "conceptual",
                "explanation": "Conceptual design translates business requirements into logical relationships."
            },
            {
                "id": "w3_q17", "type": "fitb",
                "question": "In the digital transformation roadmap, Stage 1 represents __________ operations.",
                "answer": "manual",
                "explanation": "Stage 1 is manual (paper or verbal) operations."
            },
            {
                "id": "w3_q18", "type": "fitb",
                "question": "Departmental databases that are isolated and cannot share data easily are called data __________.",
                "answer": "silos",
                "explanation": "Data silos result from isolated Stage 3 record keeping."
            },
            {
                "id": "w3_q19", "type": "fitb",
                "question": "The level on the roadmap that integrates department systems is __________ systems.",
                "answer": "integrated",
                "explanation": "Integrated systems link isolated records across boundaries."
            },
            {
                "id": "w3_q20", "type": "fitb",
                "question": "A manager should never automate a __________ manual process.",
                "answer": "broken",
                "explanation": "Automating a broken process only scale-up errors."
            },
            
            # 3 Match
            {
                "id": "w3_q21", "type": "match",
                "question": "Match the roadmap level to its description:",
                "left_items": ["Stage 1", "Stage 3", "Stage 5"],
                "right_items": ["Paper-based operations", "Isolated local databases", "Smart alerts and analytics"],
                "answer": {
                    "Stage 1": "Paper-based operations",
                    "Stage 3": "Isolated local databases",
                    "Stage 5": "Smart alerts and analytics"
                },
                "explanation": "Transformation maps from paper (1) to local data (3) to intelligent analytics (5)."
            },
            {
                "id": "w3_q22", "type": "match",
                "question": "Match the design level to the audience:",
                "left_items": ["Conceptual Design", "Technical Design", "Syllabus Layout"],
                "right_items": ["Business Managers", "Database Developers", "Course Lecturers"],
                "answer": {
                    "Conceptual Design": "Business Managers",
                    "Technical Design": "Database Developers",
                    "Syllabus Layout": "Course Lecturers"
                },
                "explanation": "Managers focus on conceptual structures; developers code technical implementations; instructors guide layouts."
            },
            {
                "id": "w3_q23", "type": "match",
                "question": "Match the system component to its function:",
                "left_items": ["Business Rules", "Data Flow Paths", "Tech Platforms"],
                "right_items": ["Define compliance limits", "Route database packets", "Store binary records"],
                "answer": {
                    "Business Rules": "Define compliance limits",
                    "Data Flow Paths": "Route database packets",
                    "Tech Platforms": "Store binary records"
                },
                "explanation": "Rules regulate operations; flows route data packets; platforms house hardware records."
            },
            
            # 2 Scenarios
            {
                "id": "w3_q24", "type": "scenario",
                "scenario": "A medical clinic coordinator wants to digitalize records. She hires a developer who starts coding database structures immediately. The developer writes code for 3 weeks but builds fields that omit prescription confirmation steps, which are legally required. The system must be scrapped and rewritten.",
                "question": "What design phase was bypassed here?",
                "choices": [
                    "Technical database optimization.",
                    "Conceptual design and alignment on business rules.",
                    "Server memory installation check.",
                    "Workplace monitoring audit."
                ],
                "answer": 1,
                "explanation": "Skipping conceptual design leads to coding systems that violate business rules or legal requirements."
            },
            {
                "id": "w3_q25", "type": "scenario",
                "scenario": "A post-collapse settlement attempts to launch an intelligent AI routing engine to direct trucks. However, truck coordinators still write routes on scrap paper, depots don't have local computers, and there is no synchronized ledger tracking truck inventory.",
                "question": "What roadmap planning error did they make?",
                "choices": [
                    "They should have used faster CPU chips.",
                    "They tried to deploy Stage 5 (Intelligent AI) before establishing Stage 1 (Manual), 2 (Organized), and 3 (Records) systems.",
                    "They forgot to write a CSS style sheet.",
                    "They did not purchase proprietary databases."
                ],
                "answer": 1,
                "explanation": "Digital transformation requires systematic build-up; you cannot deploy intelligent systems without record-keeping foundations."
            }
        ]
    }

def generate_week4():
    return {
        "week": 4,
        "title": "Information Ethics & Governance",
        "questions": [
            # 10 MCQ
            {
                "id": "w4_q1", "type": "mcq",
                "question": "Under the Data Protection Act frameworks, what is a primary threat vector for database ledgers?",
                "choices": [
                    "Unsynchronized font layouts on CSS.",
                    "Unauthorized data manipulation and tracking surveillance.",
                    "Lack of automated code tests.",
                    "Low CPU core speed availability."
                ],
                "answer": 1,
                "explanation": "Data protection focuses on preventing confidential leaks, unauthorized manipulation, and surveillance states (Slide 24)."
            },
            {
                "id": "w4_q2", "type": "mcq",
                "question": "What is the primary role of AI in Decision Support Systems (DSS)?",
                "choices": [
                    "To assume full legal and operational accountability for database choices.",
                    "To assist managers by identifying trends, but humans remain accountable.",
                    "To write code files and replace engineers completely.",
                    "To bypass standard regulatory audits."
                ],
                "answer": 1,
                "explanation": "AI functions as a decision aid. Operational and ethical accountability belongs strictly to human managers (Slide 26)."
            },
            {
                "id": "w4_q3", "type": "mcq",
                "question": "Which of the following is the correct order of the four-question ethical decision checklist?",
                "choices": [
                    "Is it cheap? Is it fast? Is it legal? Is it popular?",
                    "Is it legal? Is it fair? Is it necessary? What are the consequences?",
                    "Who built it? Is it open-source? How is it hosted? Is it fast?",
                    "Is it encrypted? Is it database-backed? Is it logged? Is it scalable?"
                ],
                "answer": 1,
                "explanation": "The checklist: Legal (policy), Fair (equity), Necessary (scale), and Consequences (risks) (Slide 25)."
            },
            {
                "id": "w4_q4", "type": "mcq",
                "question": "What is a main risk of invasive workplace monitoring policies?",
                "choices": [
                    "High costs of network cabling.",
                    "Reduced employee trust, increased privacy anxiety, and lower morale.",
                    "Bypassing data validation code scripts.",
                    "Slow system database performance."
                ],
                "answer": 1,
                "explanation": "While monitoring can protect compliance, over-monitoring destroys workforce trust and morale."
            },
            {
                "id": "w4_q5", "type": "mcq",
                "question": "Why does a manager define clear data governance rules?",
                "choices": [
                    "To accelerate the speed of code compilation.",
                    "To ensure data integrity, restrict access, and manage compliance.",
                    "To avoid using secondary backup servers.",
                    "To automatically generate CSS variables."
                ],
                "answer": 1,
                "explanation": "Governance defines access authorities and protects data from corruption or abuse."
            },
            {
                "id": "w4_q6", "type": "mcq",
                "question": "In a post-collapse ledger system, why must leaders respect data limits?",
                "choices": [
                    "To save storage block bytes.",
                    "To prevent surveillance misuse and maintain citizen trust in new institutions.",
                    "To accelerate mesh router sync schedules.",
                    "To avoid using Python scripting tools."
                ],
                "answer": 1,
                "explanation": "Over-gathering data in a crisis opens risk vectors for administrative overreach and abuse."
            },
            {
                "id": "w4_q7", "type": "mcq",
                "question": "Which issue is categorized under 'Computer Ethics'?",
                "choices": [
                    "Configuring proper database query indexes.",
                    "Weighing equity, bias, privacy, and tracking rights in system design.",
                    "Choosing between Linux or Windows servers.",
                    "Installing system cooling hardware."
                ],
                "answer": 1,
                "explanation": "Ethics concerns values, fairness, rights, and responsibilities in tech implementations."
            },
            {
                "id": "w4_q8", "type": "mcq",
                "question": "What is a secondary benefit of intranet-based coordination portals (DSS)?",
                "choices": [
                    "They allow unlimited public internet routing.",
                    "They speed up resource coordination and reduce public panic.",
                    "They eliminate the need for backup batteries.",
                    "They replace manual trade clerks entirely."
                ],
                "answer": 1,
                "explanation": "DSS portals keep stakeholders updated, coordinating distribution and stabilizing public expectations."
            },
            {
                "id": "w4_q9", "type": "mcq",
                "question": "Why can AI not replace human managers in operational decision-making?",
                "choices": [
                    "AI has no ability to write SQL queries.",
                    "AI lacks accountability, ethical reasoning capacity, and holistic judgment.",
                    "AI operates at too slow of a processing speed.",
                    "AI cannot run inside local area networks."
                ],
                "answer": 1,
                "explanation": "AI models process data but cannot hold legal responsibility or evaluate complex human values."
            },
            {
                "id": "w4_q10", "type": "mcq",
                "question": "What does data integrity refer to in database governance?",
                "choices": [
                    "The physical strength of server components.",
                    "The accuracy, completeness, and reliability of data over its lifecycle.",
                    "The speed of network sync schedules.",
                    "The cost of buying backup software."
                ],
                "answer": 1,
                "explanation": "Integrity guarantees that data records are not modified or corrupted by unauthorized means."
            },
            
            # 5 True/False
            {
                "id": "w4_q11", "type": "tf",
                "question": "Under modern ethics guidelines, any technology that can be built should be implemented.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Managers must evaluate ethical limits (surveillance, tracking) before building systems."
            },
            {
                "id": "w4_q12", "type": "tf",
                "question": "Workplace monitoring is always illegal regardless of corporate security needs.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Monitoring is legal for compliance and security but requires fair boundaries."
            },
            {
                "id": "w4_q13", "type": "tf",
                "question": "The ethical question of fairness includes auditing AI models for data biases.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Fairness requires ensuring systems do not produce biased outputs against subgroups."
            },
            {
                "id": "w4_q14", "type": "tf",
                "question": "Information governance policies are only required when using cloud servers.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Governance is required for both online and offline (mesh, local) databases."
            },
            {
                "id": "w4_q15", "type": "tf",
                "question": "An intranet DSS speeds up coordination by sharing resource logs across mesh nodes.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Local networks share strategic information, avoiding panic and optimizing shipping."
            },
            
            # 5 Fill in the Blanks
            {
                "id": "w4_q16", "type": "fitb",
                "question": "The framework that regulates database privacy and citizen data tracking is the Data __________ Act.",
                "answer": "protection",
                "explanation": "Data Protection Acts establish rules for collecting, storing, and securing data."
            },
            {
                "id": "w4_q17", "type": "fitb",
                "question": "AI systems support managers, but __________ remains strictly human.",
                "answer": "accountability",
                "explanation": "Managers cannot delegate ultimate operational accountability to AI systems."
            },
            {
                "id": "w4_q18", "type": "fitb",
                "question": "A network restricted to internal corporate use with access controls is an __________.",
                "answer": "intranet",
                "explanation": "Intranets support internal collaboration safely inside local firewalls."
            },
            {
                "id": "w4_q19", "type": "fitb",
                "question": "The step in the ethical decision checklist evaluating risks versus benefits is __________.",
                "answer": "consequences",
                "explanation": "Consequences check for unintended risks or harms from technology."
            },
            {
                "id": "w4_q20", "type": "fitb",
                "question": "Unauthorized change or hacking of ledger balances violates data __________.",
                "answer": "integrity",
                "explanation": "Data integrity guarantees records remain unchanged and correct."
            },
            
            # 3 Match
            {
                "id": "w4_q21", "type": "match",
                "question": "Match the ethical concern with its system risk scenario:",
                "left_items": ["Privacy Leak", "Data Bias", "Workplace Stress"],
                "right_items": ["Clerks access health records", "AI allocates resources unfairly", "Logging keystrokes hourly"],
                "answer": {
                    "Privacy Leak": "Clerks access health records",
                    "Data Bias": "AI allocates resources unfairly",
                    "Workplace Stress": "Logging keystrokes hourly"
                },
                "explanation": "Privacy leaks reveal data; bias creates unfairness; monitoring keystrokes raises employee anxiety."
            },
            {
                "id": "w4_q22", "type": "match",
                "question": "Match the checklist question to its target metric:",
                "left_items": ["Is it legal?", "Is it fair?", "Is it necessary?"],
                "right_items": ["Compliance check", "Equity check", "Purpose scope check"],
                "answer": {
                    "Is it legal?": "Compliance check",
                    "Is it fair?": "Equity check",
                    "Is it necessary?": "Purpose scope check"
                },
                "explanation": "Legal is compliance; fair is equity; necessary scopes purpose constraints."
            },
            {
                "id": "w4_q23", "type": "match",
                "question": "Match the portal component to its functionality:",
                "left_items": ["Audit log", "Encryption keys", "Access roles"],
                "right_items": ["Record balance edits", "Secure data packets", "Assign editing rights"],
                "answer": {
                    "Audit log": "Record balance edits",
                    "Encryption keys": "Secure data packets",
                    "Access roles": "Assign editing rights"
                },
                "explanation": "Audit logs track edits; encryption secures packets; roles manage modification authorities."
            },
            
            # 2 Scenarios
            {
                "id": "w4_q24", "type": "scenario",
                "scenario": "A regional commander implements a mesh network tool that checks employee locations every 5 minutes. The goal is to track trade speed. Within 3 weeks, two clerks resign due to anxiety, and others report fake locations by leaving devices at desks, corrupting the transit log database.",
                "question": "What management mistake was made here?",
                "choices": [
                    "They should have used faster GPS trackers.",
                    "Failing to balance workplace monitoring security benefits against trust and morale costs.",
                    "Failing to write code validation scripts.",
                    "Bypassing the database index settings."
                ],
                "answer": 1,
                "explanation": "Over-monitoring damages trust, inducing employees to corrupt database metrics to bypass surveillance."
            },
            {
                "id": "w4_q25", "type": "scenario",
                "scenario": "An AI system is deployed to allocate vaccines. It reads historical logs and notices that central settlements received drugs faster. It recommends sending all vaccines to central depots, leaving regional outposts with zero medicine, triggering a localized outbreak.",
                "question": "What concept describes this AI failure?",
                "choices": [
                    "Slow network sync speed.",
                    "A failure to audit AI bias, showing why AI should support decisions but humans remain accountable.",
                    "The system had too few database backup disks.",
                    "Coding in incorrect HTML formats."
                ],
                "answer": 1,
                "explanation": "AI models replicate historical biases. Humans must remain accountable to override unfair automated recommendations."
            }
        ]
    }

def generate_week5():
    return {
        "week": 5,
        "title": "Systems Development Life Cycles (SDLC)",
        "questions": [
            # 10 MCQ
            {
                "id": "w5_q1", "type": "mcq",
                "question": "Which of the following describes the Waterfall development model?",
                "choices": [
                    "A model where phases overlap continuously without documentation.",
                    "A structured, sequential model where one phase ends completely before the next begins.",
                    "A rapid coding method that bypasses the design phase.",
                    "A model that requires no customer requirements gathering."
                ],
                "answer": 1,
                "explanation": "Waterfall flows sequentially from planning through maintenance, requiring heavy documentation (Slide 29)."
            },
            {
                "id": "w5_q2", "type": "mcq",
                "question": "Under what condition is the Waterfall model most suitable?",
                "choices": [
                    "When project requirements are highly unstable and change weekly.",
                    "When requirements are stable, well-understood, and changes are minimal.",
                    "When the customer wants a prototype within 3 days.",
                    "When there is no database developer available."
                ],
                "answer": 1,
                "explanation": "Waterfall is best when scope is locked down and changes are minimized (Slide 29)."
            },
            {
                "id": "w5_q3", "type": "mcq",
                "question": "What is the primary operational benefit of the Prototyping model?",
                "choices": [
                    "It enforces heavy documentation structures at every step.",
                    "It obtains early user feedback to clarify requirements and reduce design risk.",
                    "It eliminates the coding phase entirely.",
                    "It runs without requiring hypervisor setups."
                ],
                "answer": 1,
                "explanation": "Prototyping builds a mock-up quickly to test assumptions and clarify what users need (Slide 31)."
            },
            {
                "id": "w5_q4", "type": "mcq",
                "question": "Which SDLC phase focus belongs primarily to business managers rather than developers?",
                "choices": [
                    "Writing CSS design templates.",
                    "Scoping objectives, budgets, timelines, risk, and resources.",
                    "Debugging syntax errors in code packages.",
                    "Setting up database indices."
                ],
                "answer": 1,
                "explanation": "Managers align project variables with corporate resources, while developers implement the code (Slide 28)."
            },
            {
                "id": "w5_q5", "type": "mcq",
                "question": "What is a main limitation of the Waterfall model?",
                "choices": [
                    "It has no clear milestones or stages.",
                    "It is extremely difficult to change requirements late in the cycle.",
                    "It requires no system documentation.",
                    "It runs slower on cloud computers."
                ],
                "answer": 1,
                "explanation": "Because Waterfall is sequential, modifications late in development trigger high costs and rework loops (Slide 30)."
            },
            {
                "id": "w5_q6", "type": "mcq",
                "question": "What does the Agile development model prioritize?",
                "choices": [
                    "Comprehensive documentation over working software.",
                    "Adaptability, customer collaboration, and iterative incremental delivery.",
                    "Strict sequential development schedules.",
                    "Replacing developers with automated templates."
                ],
                "answer": 1,
                "explanation": "Agile embraces change and delivers working features in short feedback loops (Slide 33)."
            },
            {
                "id": "w5_q7", "type": "mcq",
                "question": "In the SDLC, what is the correct order of the first three phases?",
                "choices": [
                    "Coding ➔ Testing ➔ Maintenance",
                    "Planning ➔ Requirements Analysis ➔ Design",
                    "Deployment ➔ Design ➔ Testing",
                    "Requirements ➔ Maintenance ➔ Coding"
                ],
                "answer": 1,
                "explanation": "Projects start with Planning, move to Requirements scoping, then Design blueprints (Slide 28)."
            },
            {
                "id": "w5_q8", "type": "mcq",
                "question": "What is the core focus of the Spiral SDLC model?",
                "choices": [
                    "Rapid visual user interface sketches.",
                    "Continuous risk analysis and assessment loops.",
                    "Strict sequential checklist compliance.",
                    "Eliminating coding tests."
                ],
                "answer": 1,
                "explanation": "The Spiral model iterates through risk valuation quadrants, making it ideal for high-risk projects (Slide 9)."
            },
            {
                "id": "w5_q9", "type": "mcq",
                "question": "Which of the following is a classic prototyping application in a post-collapse setting?",
                "choices": [
                    "Writing a 10,000-line database scheme in SQL.",
                    "Deploying a draft paper ledger to trade posts for a week to check user interaction.",
                    "Buying proprietary server software from external sellers.",
                    "Bypassing all regulator rules."
                ],
                "answer": 1,
                "explanation": "Paper prototyping tests layout usability and workflow logic quickly before coding starts (Slide 31)."
            },
            {
                "id": "w5_q10", "type": "mcq",
                "question": "What is the core rule for selecting an SDLC model?",
                "choices": [
                    "Always use Agile for every project.",
                    "Always use Waterfall to ensure documentation.",
                    "Align the model choice with the stability of requirements and project constraints.",
                    "Select the model based on popular trends."
                ],
                "answer": 2,
                "explanation": "No model is universally best; managers must select the model matching the project context (Slide 33)."
            },
            
            # 5 True/False
            {
                "id": "w5_q11", "type": "tf",
                "question": "The SDLC is primarily a coding pipeline and is not a management control process.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. The SDLC is a critical management process to track costs, risk, and resource timelines (Slide 28)."
            },
            {
                "id": "w5_q12", "type": "tf",
                "question": "Waterfall is highly suitable for projects where scope is clear and requirements are stable.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Sequential stability prevents scope creep and keeps projects on budget (Slide 29)."
            },
            {
                "id": "w5_q13", "type": "tf",
                "question": "Prototyping is slower than Waterfall because you have to build mock-ups first.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Prototyping reduces long-term rework by correcting requirements early, saving total time."
            },
            {
                "id": "w5_q14", "type": "tf",
                "question": "The Agile model views requirement modifications as a normal, manageable reality.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Agile values adaptability over strict contract negotiation (Slide 33)."
            },
            {
                "id": "w5_q15", "type": "tf",
                "question": "The Spiral SDLC is characterized by iterative quadrants focusing on risk management.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Risk analysis drives the spiral increments (Slide 9)."
            },
            
            # 5 Fill in the Blanks
            {
                "id": "w5_q16", "type": "fitb",
                "question": "A sequential development process that flows steadily downwards is the __________ model.",
                "answer": "waterfall",
                "explanation": "Waterfall is named after its sequential downward flow structure."
            },
            {
                "id": "w5_q17", "type": "fitb",
                "question": "An early, simplified model of a system built to gather feedback is a __________.",
                "answer": "prototype",
                "explanation": "Prototypes clarify user expectations before database coding begins."
            },
            {
                "id": "w5_q18", "type": "fitb",
                "question": "The SDLC model that prioritizes risk management at every stage is the __________ model.",
                "answer": "spiral",
                "explanation": "Spiral iterations focus on evaluating and mitigating architectural risks."
            },
            {
                "id": "w5_q19", "type": "fitb",
                "question": "In the SDLC, coding and syntax debugging are done in the __________ phase.",
                "answer": "development",
                "explanation": "Development (or coding) translates design files into programs."
            },
            {
                "id": "w5_q20", "type": "fitb",
                "question": "Delivering working software in small, incremental blocks is a core principle of __________.",
                "answer": "agile",
                "explanation": "Agile increments focus on releasing functional modules iteratively."
            },
            
            # 3 Match
            {
                "id": "w5_q21", "type": "match",
                "question": "Match the development model to its primary advantage:",
                "left_items": ["Waterfall", "Prototyping", "Agile"],
                "right_items": ["Clear documentation and phases", "Early requirement verification", "High adaptability to change"],
                "answer": {
                    "Waterfall": "Clear documentation and phases",
                    "Prototyping": "Early requirement verification",
                    "Agile": "High adaptability to change"
                },
                "explanation": "Waterfall secures structure; prototyping clarifies user scope; Agile supports adaptivity."
            },
            {
                "id": "w5_q22", "type": "match",
                "question": "Match the project parameter to the aligned model selection:",
                "left_items": ["Highly unstable scope", "Strict compliance ledger", "Unclear user workflows"],
                "right_items": ["Agile Model", "Waterfall Model", "Prototyping Model"],
                "answer": {
                    "Highly unstable scope": "Agile Model",
                    "Strict compliance ledger": "Waterfall Model",
                    "Unclear user workflows": "Prototyping Model"
                },
                "explanation": "Unstable scope requires Agile; strict regulatory ledgers fit Waterfall; unclear workflows fit prototyping."
            },
            {
                "id": "w5_q23", "type": "match",
                "question": "Match the SDLC phase to its output artifact:",
                "left_items": ["Requirements Phase", "Design Phase", "Testing Phase"],
                "right_items": ["Functional Spec sheet", "Architecture blueprint", "Bug report logs"],
                "answer": {
                    "Requirements Phase": "Functional Spec sheet",
                    "Design Phase": "Architecture blueprint",
                    "Testing Phase": "Bug report logs"
                },
                "explanation": "Requirements define what (specs); design charts structures (blueprints); testing traces errors (bug logs)."
            },
            
            # 2 Scenarios
            {
                "id": "w5_q24", "type": "scenario",
                "scenario": "A kingdom logistics department wants to build a simple transport reservation system. The user flows are completely new, and clerks are unsure how they will match cargoes to carts. The IT manager chooses the Waterfall model, requiring 3 months of strict design document lockups before coding.",
                "question": "What is the main risk of this choice?",
                "choices": [
                    "The system will use too much power.",
                    "The project will deliver a system that clerks reject because they couldn't see and modify the workflow mock-ups early.",
                    "The database will run out of storage lines.",
                    "They will use incorrect network codes."
                ],
                "answer": 1,
                "explanation": "Using Waterfall for highly uncertain user workflows leads to delivering products that miss actual user needs (Slide 30)."
            },
            {
                "id": "w5_q25", "type": "scenario",
                "scenario": "A development team has to replace a legacy gold coins ledger. The rules of gold trade compliance are strictly locked by the Kingdom Monetary Board and cannot change. The team chooses Agile and starts writing small database codes, changing features weekly. This causes conflicts with auditor boards.",
                "question": "Why did Agile fail here?",
                "choices": [
                    "Agile does not support database code files.",
                    "With strict, non-negotiable compliance rules, Waterfall's structured documentation and design lock-ins were better suited.",
                    "They should have used faster server processors.",
                    "They forgot to write CSS styling structures."
                ],
                "answer": 1,
                "explanation": "Agile scope fluctuations can conflict with strict, non-negotiable regulatory compliance environments (Slide 33)."
            }
        ]
    }

def generate_week6():
    return {
        "week": 6,
        "title": "IT Frameworks & Transaction Processing",
        "questions": [
            # 10 MCQ
            {
                "id": "w6_q1", "type": "mcq",
                "question": "What is the primary purpose of a Technology Management Framework?",
                "choices": [
                    "To speed up database packet transfers.",
                    "To integrate five core dimensions: Strategy, Processes, Technology, People, and Governance.",
                    "To write code comments automatically.",
                    "To choose the cheapest hardware vendors."
                ],
                "answer": 1,
                "explanation": "A technology management framework balances strategy, workflows, software, training, and audits (Slide 35)."
            },
            {
                "id": "w6_q2", "type": "mcq",
                "question": "In the DIKW hierarchy, what does 'Data' represent?",
                "choices": [
                    "Summarized trends and reports.",
                    "Raw, unorganized transaction facts (e.g., '10kg grain allocated').",
                    "Actionable operational insights.",
                    "Strategic rationing decisions."
                ],
                "answer": 1,
                "explanation": "Data represents raw, unstructured events and numbers without context (Slide 37)."
            },
            {
                "id": "w6_q3", "type": "mcq",
                "question": "Which system component logs daily, routine transaction records?",
                "choices": [
                    "Decision Support System (DSS)",
                    "Transaction Processing System (TPS)",
                    "High-Command Analytics Portal",
                    "Bare-metal Hypervisor"
                ],
                "answer": 1,
                "explanation": "TPS logs daily operational transactions that form the data foundation (Slide 37)."
            },
            {
                "id": "w6_q4", "type": "mcq",
                "question": "How does a Decision Support System (DSS) differ from a Transaction Processing System (TPS)?",
                "choices": [
                    "DSS is for programmers; TPS is for managers.",
                    "TPS records raw logs; DSS analyzes trends to help managers evaluate decision choices.",
                    "TPS runs on servers; DSS is printed on paper.",
                    "DSS handles security keys; TPS builds network cables."
                ],
                "answer": 1,
                "explanation": "TPS operates at the transactional baseline; DSS processes logs into trend metrics to support managers."
            },
            {
                "id": "w6_q5", "type": "mcq",
                "question": "In the DIKW hierarchy, how does 'Knowledge' differ from 'Information'?",
                "choices": [
                    "Knowledge is raw numbers; Information is insights.",
                    "Information connects data points; Knowledge adds human context and actionable understanding.",
                    "Information is stored in databases; Knowledge is written in CSS.",
                    "There is no difference between them."
                ],
                "answer": 1,
                "explanation": "Knowledge translates trends (information) into actionable operational understanding (Slide 37)."
            },
            {
                "id": "w6_q6", "type": "mcq",
                "question": "What is the risk of using database logs that are incorrect at the TPS level?",
                "choices": [
                    "Low CPU core metrics.",
                    "Incorrect baseline logs propagate upward, causing bad decisions at the DSS level (GIGO - Garbage In, Garbage Out).",
                    "Loss of wireless mesh connections.",
                    "Higher cost of database licenses."
                ],
                "answer": 1,
                "explanation": "If transactional inputs are inaccurate, all derived trends and decisions will be flawed."
            },
            {
                "id": "w6_q7", "type": "mcq",
                "question": "What represents the 'Wisdom' level in the DIKW hierarchy?",
                "choices": [
                    "A raw log of grain shipments.",
                    "The strategic decision to establish rationing rules to survive a drought.",
                    "A spreadsheet displaying grain shortages.",
                    "An inventory database schema."
                ],
                "answer": 1,
                "explanation": "Wisdom applies knowledge to make strategic decisions under values and constraints (Slide 37)."
            },
            {
                "id": "w6_q8", "type": "mcq",
                "question": "Which dimension of the Technology Management Framework focuses on user training?",
                "choices": [
                    "Strategy",
                    "Technology",
                    "People",
                    "Governance"
                ],
                "answer": 2,
                "explanation": "The People dimension ensures users are trained, capable, and willing to adopt new systems (Slide 35)."
            },
            {
                "id": "w6_q9", "type": "mcq",
                "question": "Why are decision frameworks useful for technology managers?",
                "choices": [
                    "They allow developers to compile code faster.",
                    "They structure decisions, reduce personal bias, and verify options systematically.",
                    "They automatically backup database files.",
                    "They replace the need for physical networks."
                ],
                "answer": 1,
                "explanation": "Frameworks guide logical analysis and reduce decision errors in high-pressure environments."
            },
            {
                "id": "w6_q10", "type": "mcq",
                "question": "What is a transaction processing system (TPS) output?",
                "choices": [
                    "Rationing rules policies.",
                    "Daily receipt logs and transaction files.",
                    "Strategic crop allocation roadmaps.",
                    "Competitive marketing slide decks."
                ],
                "answer": 1,
                "explanation": "TPS outputs are daily logs, receipts, and operational records."
            },
            
            # 5 True/False
            {
                "id": "w6_q11", "type": "tf",
                "question": "A Transaction Processing System is developer-facing and does not record operational trade records.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. TPS records daily routine logs at the baseline of operations (Slide 37)."
            },
            {
                "id": "w6_q12", "type": "tf",
                "question": "According to the DIKW model, Wisdom is built directly from raw data without needing Information or Knowledge.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Wisdom is the top of the pyramid, requiring structured information and knowledge processing."
            },
            {
                "id": "w6_q13", "type": "tf",
                "question": "Technology management frameworks require aligning software choice with business process workflows.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Technology must align with processes to avoid operational failures (Slide 35)."
            },
            {
                "id": "w6_q14", "type": "tf",
                "question": "GIGO means that garbage data entering a TPS results in garbage outputs from a DSS.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Garbage In, Garbage Out; base metrics dictate analysis accuracy."
            },
            {
                "id": "w6_q15", "type": "tf",
                "question": "A Decision Support System replaces managers by making operational choices automatically.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. DSS assists managers; the manager remains accountable for final decisions (Slide 26)."
            },
            
            # 5 Fill in the Blanks
            {
                "id": "w6_q16", "type": "fitb",
                "question": "The baseline system that records routine daily transactions is the __________ system.",
                "answer": "tps",
                "explanation": "TPS stands for Transaction Processing System."
            },
            {
                "id": "w6_q17", "type": "fitb",
                "question": "The system that helps managers analyze trends and options is the __________ system.",
                "answer": "dss",
                "explanation": "DSS stands for Decision Support System."
            },
            {
                "id": "w6_q18", "type": "fitb",
                "question": "In the DIKW pyramid, data is raw, whereas __________ adds meaning and context.",
                "answer": "information",
                "explanation": "Information organizes data points to reveal structures."
            },
            {
                "id": "w6_q19", "type": "fitb",
                "question": "In the technology management framework, training clerks maps to the __________ dimension.",
                "answer": "people",
                "explanation": "The People dimension governs training, usability, and adoption."
            },
            {
                "id": "w6_q20", "type": "fitb",
                "question": "GIGO stands for Garbage In, Garbage __________.",
                "answer": "out",
                "explanation": "If raw database inputs are wrong, reports outputs will be wrong."
            },
            
            # 3 Match
            {
                "id": "w6_q21", "type": "match",
                "question": "Match the DIKW level with its case example:",
                "left_items": ["Data", "Information", "Knowledge", "Wisdom"],
                "right_items": ["Log: 'Trader A bought 10g Gold'", "Chart: 'Gold value up 5% today'", "Insight: 'Monetary panic imminent'", "Rationing rule set by leaders"],
                "answer": {
                    "Data": "Log: 'Trader A bought 10g Gold'",
                    "Information": "Chart: 'Gold value up 5% today'",
                    "Knowledge": "Insight: 'Monetary panic imminent'",
                    "Wisdom": "Rationing rule set by leaders"
                },
                "explanation": "DIKW builds from raw logs (Data) to charts (Information) to insights (Knowledge) to actions (Wisdom)."
            },
            {
                "id": "w6_q22", "type": "match",
                "question": "Match the framework dimension to its concern:",
                "left_items": ["Strategy", "Processes", "Governance"],
                "right_items": ["Long-term digital goals", "Step-by-step trade workflows", "Security audit controls"],
                "answer": {
                    "Strategy": "Long-term digital goals",
                    "Processes": "Step-by-step trade workflows",
                    "Governance": "Security audit controls"
                },
                "explanation": "Strategy scopes goals; process diagrams workflows; governance enforces compliance."
            },
            {
                "id": "w6_q23", "type": "match",
                "question": "Match the system level to the target user:",
                "left_items": ["TPS", "DSS", "Bare-Metal OS"],
                "right_items": ["Frontline trade clerks", "Mid-level managers", "System administrators"],
                "answer": {
                    "TPS": "Frontline trade clerks",
                    "DSS": "Mid-level managers",
                    "Bare-Metal OS": "System administrators"
                },
                "explanation": "Clerks use transaction systems; managers use decision support; admins config OS layers."
            },
            
            # 2 Scenarios
            {
                "id": "w6_q24", "type": "scenario",
                "scenario": "A kingdom leader is checking a weekly DSS report. The report says food stocks are up 40%. Based on this, she exports 50 tons of grain to a neighbor. Within 2 days, the home settlement runs out of flour. It is discovered that clerks logged duplicate receipts at the trade posts.",
                "question": "What system concept explains this error?",
                "choices": [
                    "Poor compiler choices.",
                    "Garbage In, Garbage Out (GIGO) where incorrect TPS entries corrupted the DSS report.",
                    "Failing to install enough solar batteries.",
                    "A failure of the network mesh connections."
                ],
                "answer": 1,
                "explanation": "TPS errors propagate into DSS reports, leading managers to make catastrophic decisions based on garbage data."
            },
            {
                "id": "w6_q25", "type": "scenario",
                "scenario": "An IT team is deploying a new resource database. They buy the software and configure it. However, they do not create user guides or hold training for the clerks. On launch day, clerks do not know how to input numbers, causing massive delays and lines at depots.",
                "question": "Which Technology Management Framework dimension did they neglect?",
                "choices": [
                    "Strategy",
                    "Technology",
                    "People",
                    "Governance"
                ],
                "answer": 2,
                "explanation": "Failing to train and align the People dimension causes technically sound systems to fail on launch day (Slide 35)."
            }
        ]
    }

def generate_week7():
    return {
        "week": 7,
        "title": "E-Business Ecosystems & Cloud Governance",
        "questions": [
            # 10 MCQ
            {
                "id": "w7_q1", "type": "mcq",
                "question": "What is the primary operational difference between an Intranet and an Extranet?",
                "choices": [
                    "Intranets are open to the public; Extranets are internal.",
                    "Intranets are internal corporate networks; Extranets extend secure access to trusted suppliers and partners.",
                    "Intranets require server OS; Extranets run strictly on laptops.",
                    "There is no difference in access controls."
                ],
                "answer": 1,
                "explanation": "Intranets support internal collaboration; Extranets extend secure boundaries to suppliers/partners."
            },
            {
                "id": "w7_q2", "type": "mcq",
                "question": "In cloud infrastructure deployment models, which level gives sysadmins maximum control over the operating system?",
                "choices": [
                    "SaaS (Software as a Service)",
                    "PaaS (Platform as a Service)",
                    "IaaS (Infrastructure as a Service)",
                    "FaaS (Function as a Service)"
                ],
                "answer": 2,
                "explanation": "IaaS provides raw VM compute resources, allowing the client full control over OS configurations."
            },
            {
                "id": "w7_q3", "type": "mcq",
                "question": "What does RTO (Recovery Time Objective) define in continuity planning?",
                "choices": [
                    "The maximum age of data that must be recovered from backup archives.",
                    "The target duration of time within which a system must be restored after a disaster.",
                    "The cost of purchasing duplicate database backup disks.",
                    "The speed of network interface packet transfers."
                ],
                "answer": 1,
                "explanation": "RTO is the target duration to restore operational capacity after a crash."
            },
            {
                "id": "w7_q4", "type": "mcq",
                "question": "What does RPO (Recovery Point Objective) define?",
                "choices": [
                    "The maximum tolerable period of data loss measured in time (e.g. last 4 hours of logs).",
                    "The physical location of backup vaults.",
                    "The speed of database search runs.",
                    "The number of admins required to verify a restore."
                ],
                "answer": 0,
                "explanation": "RPO measures data loss tolerance, defining the maximum age of data that must be recoverable."
            },
            {
                "id": "w7_q5", "type": "mcq",
                "question": "Which cloud model describes using Google Workspace or Microsoft 365 directly from a browser?",
                "choices": [
                    "IaaS",
                    "PaaS",
                    "SaaS",
                    "Custom Bare-Metal"
                ],
                "answer": 2,
                "explanation": "SaaS provides ready-to-use software applications managed entirely by the vendor."
            },
            {
                "id": "w7_q6", "type": "mcq",
                "question": "Why does a company construct a Disaster Recovery Plan (DRP)?",
                "choices": [
                    "To speed up program compilation times.",
                    "To establish structured steps to restore operations and data after a system disaster.",
                    "To reduce software license costs.",
                    "To bypass standard regulatory audits."
                ],
                "answer": 1,
                "explanation": "DRP provides step-by-step procedures to recover systems and minimize business downtime."
            },
            {
                "id": "w7_q7", "type": "mcq",
                "question": "What is a 'Digital Ecosystem' in modern e-business?",
                "choices": [
                    "The biological variables surrounding server farms.",
                    "A network of interconnected businesses, customers, and platforms that co-create value.",
                    "An isolated database server.",
                    "A code script that runs without network access."
                ],
                "answer": 1,
                "explanation": "Digital ecosystems connect platforms, API logs, and suppliers to generate mutual value."
            },
            {
                "id": "w7_q8", "type": "mcq",
                "question": "What is a main risk of total vendor lock-in in cloud services?",
                "choices": [
                    "Slow page scrolling.",
                    "High costs and difficulty in migrating data and code to another cloud provider.",
                    "Loss of database search fields.",
                    "Bypassing login credentials."
                ],
                "answer": 1,
                "explanation": "Vendor lock-in leaves organizations dependent on a single supplier, exposing them to price hikes."
            },
            {
                "id": "w7_q9", "type": "mcq",
                "question": "Which cloud service level allows programmers to deploy code directly without configuring operating systems?",
                "choices": [
                    "IaaS",
                    "PaaS",
                    "SaaS",
                    "Bare-Metal OS"
                ],
                "answer": 1,
                "explanation": "PaaS provides the runtime environment, database, and OS layer, allowing developers to focus on coding."
            },
            {
                "id": "w7_q10", "type": "mcq",
                "question": "What is a primary concern of cloud governance?",
                "choices": [
                    "The color layout of the cloud provider logo.",
                    "Managing cost compliance, data security policies, and resource configurations.",
                    "The physical cooling setup in a distant datacenter.",
                    "Choosing program font variables."
                ],
                "answer": 1,
                "explanation": "Governance manages spending limits, access permissions, and data residency compliance in the cloud."
            },
            
            # 5 True/False
            {
                "id": "w7_q11", "type": "tf",
                "question": "An Intranet extends secure access to external partners and suppliers.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. Intranets are internal. Extranets extend secure access to external partners."
            },
            {
                "id": "w7_q12", "type": "tf",
                "question": "Under a SaaS model, the client's sysadmin is responsible for patching the host OS kernel.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. In SaaS, the vendor manages all infrastructure, OS patching, and code logic."
            },
            {
                "id": "w7_q13", "type": "tf",
                "question": "RTO measures the tolerable duration of data loss during a system disaster.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. RTO measures recovery speed (downtime). RPO measures tolerable data loss."
            },
            {
                "id": "w7_q14", "type": "tf",
                "question": "A business continuity plan focuses strictly on data backups and does not include manual operations procedures.",
                "choices": ["True", "False"], "answer": 1,
                "explanation": "False. BCP covers manual fallbacks, staff roles, and communication rules during disruptions."
            },
            {
                "id": "w7_q15", "type": "tf",
                "question": "IaaS provides the raw compute resources, requiring the client to install and patch the operating system.",
                "choices": ["True", "False"], "answer": 0,
                "explanation": "True. Infrastructure as a Service leaves OS management and configuration to the client."
            },
            
            # 5 Fill in the Blanks
            {
                "id": "w7_q16", "type": "fitb",
                "question": "The time limit target within which a system must be recovered after a crash is the __________.",
                "answer": "rto",
                "explanation": "RTO stands for Recovery Time Objective."
            },
            {
                "id": "w7_q17", "type": "fitb",
                "question": "The metric defining the maximum age of data that must be recovered is the __________.",
                "answer": "rpo",
                "explanation": "RPO stands for Recovery Point Objective."
            },
            {
                "id": "w7_q18", "type": "fitb",
                "question": "A secure network that extends internal assets to trusted suppliers is an __________.",
                "answer": "extranet",
                "explanation": "Extranets extend intranet limits to trusted external partners."
            },
            {
                "id": "w7_q19", "type": "fitb",
                "question": "Google Sheets or Office online is an example of the cloud service level known as __________.",
                "answer": "saas",
                "explanation": "SaaS (Software as a Service) delivers full apps through browser lines."
            },
            {
                "id": "w7_q20", "type": "fitb",
                "question": "A plan containing manual fallbacks and communications during a disaster is a business __________ plan.",
                "answer": "continuity",
                "explanation": "Business Continuity Plans (BCP) cover overall operational resilience."
            },
            
            # 3 Match
            {
                "id": "w7_q21", "type": "match",
                "question": "Match the cloud model to its primary management boundary:",
                "left_items": ["IaaS", "PaaS", "SaaS"],
                "right_items": ["Configure VM & OS", "Configure code runtime", "Configure user access only"],
                "answer": {
                    "IaaS": "Configure VM & OS",
                    "PaaS": "Configure code runtime",
                    "SaaS": "Configure user access only"
                },
                "explanation": "IaaS leaves OS to admin; PaaS manages OS but leaves code to programmer; SaaS manages all except logins."
            },
            {
                "id": "w7_q22", "type": "match",
                "question": "Match the continuity metric to its operational target:",
                "left_items": ["RTO (2 hours)", "RPO (4 hours)", "BCP fallback"],
                "right_items": ["Restore servers in 2h", "Restore data up to last 4h", "Use paper ledger temporarily"],
                "answer": {
                    "RTO (2 hours)": "Restore servers in 2h",
                    "RPO (4 hours)": "Restore data up to last 4h",
                    "BCP fallback": "Use paper ledger temporarily"
                },
                "explanation": "RTO dictates time limit; RPO limits data age loss; BCP manages manual fallbacks."
            },
            {
                "id": "w7_q23", "type": "match",
                "question": "Match the network type to its target scope:",
                "left_items": ["Intranet", "Extranet", "Public Web"],
                "right_items": ["Strictly internal employees", "Trusted supplier portals", "Anonymous global viewers"],
                "answer": {
                    "Intranet": "Strictly internal employees",
                    "Extranet": "Trusted supplier portals",
                    "Public Web": "Anonymous global viewers"
                },
                "explanation": "Intranets serve staff; extranets serve partners; public web serves everyone."
            },
            
            # 2 Scenarios
            {
                "id": "w7_q24", "type": "scenario",
                "scenario": "A retail database crashes at 14:00. The IT team restores the VM server at 16:00. However, they discover the last database backup occurred at 08:00. All transactions logged between 08:00 and 14:00 are lost, totaling 500 sales entries.",
                "question": "Which metric describes the 6 hours of lost data?",
                "choices": [
                    "The RTO target was exceeded.",
                    "The RPO metric boundary was violated.",
                    "The database was built in IaaS.",
                    "A failure of extranet firewall checks."
                ],
                "answer": 1,
                "explanation": "The age of lost data is governed by the Recovery Point Objective (RPO) configuration."
            },
            {
                "id": "w7_q25", "type": "scenario",
                "scenario": "During a massive flood, a settlement's central database server is completely destroyed. The IT director immediately directs trade posts to switch to paper ledgers and assigns runners to coordinate balances hourly, preventing market panic while a new server is configured.",
                "question": "What document guided these manual operational fallbacks?",
                "choices": [
                    "A compiler stylesheet configuration.",
                    "A Business Continuity Plan (BCP).",
                    "A technical database schema diagram.",
                    "An rclone configure command script."
                ],
                "answer": 1,
                "explanation": "BCP manages human and process fallbacks to ensure operations continue even when technical infrastructure fails."
            }
        ]
    }

if __name__ == "__main__":
    os.makedirs("/home/efar/mot-mba/sessiondata", exist_ok=True)
    
    quizzes = [generate_week1(), generate_week2(), generate_week3(), generate_week4(), generate_week5(), generate_week6(), generate_week7()]
    
    for q in quizzes:
        week = q["week"]
        filepath = f"/home/efar/mot-mba/sessiondata/week{week}.json"
        with open(filepath, "wb") as f:
            f.write(orjson.dumps(q, option=orjson.OPT_INDENT_2))
            
    print("Successfully generated all 7 week JSON files!")
