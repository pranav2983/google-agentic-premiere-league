"""
IPL Captain AI — Premium Streamlit Frontend
A stunning dark-themed UI for the virtual IPL captain's think-tank.
"""
import streamlit as st
import asyncio
import json
import os
from dotenv import load_dotenv

load_dotenv()

# ── Page Configuration ─────────────────────────────────────────────────
st.set_page_config(
    page_title="🏏 IPL Captain AI — Virtual Think Tank",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Premium CSS ────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800&display=swap');

/* Global Theme */
:root {
    --ipl-blue: #004BA0;
    --ipl-orange: #FF6B35;
    --ipl-gold: #FFD700;
    --ipl-purple: #6C3FC5;
    --bg-dark: #0a0e17;
    --bg-card: #111827;
    --bg-card-hover: #1a2332;
    --text-primary: #f0f4f8;
    --text-secondary: #94a3b8;
    --gradient-1: linear-gradient(135deg, #004BA0, #6C3FC5);
    --gradient-2: linear-gradient(135deg, #FF6B35, #FFD700);
    --gradient-3: linear-gradient(135deg, #10b981, #059669);
    --glass: rgba(17, 24, 39, 0.8);
    --glass-border: rgba(255, 255, 255, 0.08);
}

.stApp {
    background: var(--bg-dark);
    font-family: 'Inter', sans-serif;
}

/* Hero Header */
.hero-header {
    background: linear-gradient(135deg, #004BA0 0%, #6C3FC5 50%, #FF6B35 100%);
    border-radius: 20px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0, 75, 160, 0.3);
}

.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(255,215,0,0.15) 0%, transparent 70%);
    border-radius: 50%;
}

.hero-header h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: white;
    margin: 0;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.hero-subtitle {
    color: rgba(255,255,255,0.85);
    font-size: 1.15rem;
    margin-top: 0.5rem;
    font-weight: 400;
}

/* Agent Cards */
.agent-card {
    background: var(--glass);
    backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
}

.agent-card:hover {
    border-color: rgba(108, 63, 197, 0.4);
    box-shadow: 0 8px 32px rgba(108, 63, 197, 0.15);
    transform: translateY(-2px);
}

.agent-card h3 {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
}

.agent-card p {
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.6;
    margin: 0;
}

/* Decision Output */
.decision-box {
    background: linear-gradient(135deg, rgba(0,75,160,0.15), rgba(108,63,197,0.15));
    border: 1px solid rgba(0,75,160,0.3);
    border-radius: 16px;
    padding: 2rem;
    margin: 1rem 0;
}

.decision-box h2 {
    font-family: 'Outfit', sans-serif;
    color: var(--ipl-gold);
}

/* Status Badge */
.status-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.badge-active {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.3);
}

.badge-thinking {
    background: rgba(255, 107, 53, 0.15);
    color: #FF6B35;
    border: 1px solid rgba(255, 107, 53, 0.3);
}

/* Metric Cards */
.metric-card {
    background: var(--glass);
    backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}

.metric-value {
    font-family: 'Outfit', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    background: var(--gradient-2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-label {
    color: var(--text-secondary);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 0.3rem;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background: #0f1520;
    border-right: 1px solid var(--glass-border);
}

/* Custom Expander */
.streamlit-expanderHeader {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
}

/* Input Fields */
.stTextInput > div > div > input,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input,
.stTextArea > div > div > textarea {
    background: var(--bg-card) !important;
    border: 1px solid var(--glass-border) !important;
    color: var(--text-primary) !important;
    border-radius: 10px !important;
}

/* Buttons */
.stButton > button {
    background: var(--gradient-1) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0, 75, 160, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(0, 75, 160, 0.5) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card);
    border-radius: 12px;
    padding: 0.25rem;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    font-family: 'Outfit', sans-serif;
    font-weight: 500;
}

/* Spinner */
.stSpinner > div {
    border-color: var(--ipl-purple) !important;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ── Hero Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <h1>🏏 IPL Captain AI</h1>
    <div class="hero-subtitle">
        Your Virtual IPL Think-Tank — Powered by 5 Gemini Agents debating strategy like Dhoni, Rohit & Hardik
    </div>
</div>
""", unsafe_allow_html=True)


# ── Agent Pipeline Visualization ───────────────────────────────────────
cols = st.columns(5)
agents_info = [
    ("📊", "Stats Analyst", "Crunches numbers"),
    ("🌤️", "Conditions", "Pitch & weather"),
    ("🎯", "Strategist", "Proposes the plan"),
    ("😈", "Devil's Advocate", "Challenges it"),
    ("🎙️", "Commentator", "Cricket-speaks it"),
]
for col, (emoji, name, desc) in zip(cols, agents_info):
    with col:
        st.markdown(f"""
        <div class="agent-card" style="text-align:center;">
            <div style="font-size:2rem;">{emoji}</div>
            <h3 style="font-size:0.95rem; color:#f0f4f8;">{name}</h3>
            <p style="font-size:0.75rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)


# ── Sidebar: Match State Input ─────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏏 Match State Input")

    input_mode = st.radio(
        "Input Mode",
        ["📝 Manual Entry", "⚡ Quick Scenario", "🔗 Live URL"],
        horizontal=True,
    )

    if input_mode == "🔗 Live URL":
        st.markdown("##### Paste a live match URL")
        live_url = st.text_input(
            "Cricbuzz / ESPNCricinfo URL",
            placeholder="https://www.cricbuzz.com/live-cricket-scores/...",
            key="live_url",
        )
        if st.button("🔍 Fetch Live State", use_container_width=True):
            if live_url:
                st.session_state["match_input"] = f"Fetch live match data from this URL and analyze: {live_url}"
                st.session_state["run_analysis"] = True
            else:
                st.warning("Please paste a valid URL")

    elif input_mode == "⚡ Quick Scenario":
        st.markdown("##### Select a scenario")
        scenario = st.selectbox("Match Scenario", [
            "CSK vs MI — Death Overs Chase",
            "RCB vs SRH — Powerplay Bowling",
            "KKR vs RR — Middle Overs Spin",
            "GT vs LSG — Impact Player Decision",
            "DC vs PBKS — Strategic Timeout",
        ])

        SCENARIOS = {
            "CSK vs MI — Death Overs Chase": {
                "text": """Match State:
Innings: 2 | Over: 16.2 | Score: 134/4 | Target: 186
Batting: CSK | Bowling: MI
On Strike: MS Dhoni (18 off 10) | Non-Strike: Ravindra Jadeja (22 off 18)
Bowlers remaining: Jasprit Bumrah (2 overs left), Hardik Pandya (1 over left), Trent Boult (completed)
Pitch: Flat, Wankhede Stadium, Mumbai | Dew: Heavy
Impact Player: Available (CSK hasn't used it yet)
Required Run Rate: 14.18"""
            },
            "RCB vs SRH — Powerplay Bowling": {
                "text": """Match State:
Innings: 1 | Over: 3.4 | Score: 48/0
Batting: SRH | Bowling: RCB
On Strike: Travis Head (32 off 18) | Non-Strike: Abhishek Sharma (14 off 8)
Bowlers remaining: Mohammed Siraj (3 overs left), Yash Dayal (3 left), Wanindu Hasaranga (4 left)
Pitch: M Chinnaswamy, Bengaluru — flat batting paradise | Dew: Light
Impact Player: Not used
SRH going at 12+ RPO in the powerplay, Head looking murderous"""
            },
            "KKR vs RR — Middle Overs Spin": {
                "text": """Match State:
Innings: 1 | Over: 11.0 | Score: 87/3
Batting: KKR | Bowling: RR
On Strike: Suryakumar Yadav (28 off 22) | Non-Strike: Rinku Singh (12 off 10)
Bowlers remaining: Yuzvendra Chahal (2 overs left), Ravichandran Ashwin (2 left), Trent Boult (1 left)
Pitch: Eden Gardens, Kolkata — slowing down, some turn | Dew: Will come later
Impact Player: Available
Two right-handers at the crease"""
            },
            "GT vs LSG — Impact Player Decision": {
                "text": """Match State:
Innings: 2 | Over: 9.3 | Score: 72/2 | Target: 175
Batting: LSG | Bowling: GT
On Strike: KL Rahul (35 off 28) | Non-Strike: Rishabh Pant (18 off 14)
Bowlers remaining: Rashid Khan (3 overs left), Kagiso Rabada (2 left), Mohammed Shami (2 left)
Pitch: Narendra Modi Stadium, Ahmedabad — spin-friendly | Dew: Light
Impact Player: GT hasn't used it yet — considering bringing in an extra spinner
Required Run Rate: 9.71"""
            },
            "DC vs PBKS — Strategic Timeout": {
                "text": """Match State:
Innings: 1 | Over: 14.0 | Score: 112/5
Batting: DC | Bowling: PBKS
On Strike: Axar Patel (15 off 12) | Non-Strike: Kuldeep Yadav (2 off 3)
Bowlers remaining: Arshdeep Singh (2 overs left), Kagiso Rabada (2 left), Sam Curran (1 left)
Pitch: Arun Jaitley, Delhi — good batting, some spin | Dew: Coming in
Impact Player: Used
Need to decide: strategic timeout now or save for death overs?"""
            },
        }

        if st.button("⚡ Run This Scenario", use_container_width=True):
            st.session_state["match_input"] = SCENARIOS[scenario]["text"]
            st.session_state["run_analysis"] = True

    else:  # Manual Entry
        st.markdown("##### Match Details")
        innings = st.selectbox("Innings", [1, 2])
        col1, col2 = st.columns(2)
        with col1:
            overs = st.number_input("Overs", 0.0, 20.0, 12.0, 0.1)
            score = st.number_input("Score", 0, 400, 120)
        with col2:
            wickets = st.number_input("Wickets", 0, 10, 3)
            target = st.number_input("Target (2nd inn)", 0, 400, 180) if innings == 2 else 0

        st.markdown("##### Teams")
        batting_team = st.text_input("Batting Team", "CSK")
        bowling_team = st.text_input("Bowling Team", "MI")

        st.markdown("##### Batters")
        striker = st.text_input("On Strike", "MS Dhoni (18 off 10)")
        non_striker = st.text_input("Non-Striker", "Ravindra Jadeja (22 off 18)")

        st.markdown("##### Bowling")
        bowlers = st.text_area(
            "Bowlers Remaining (name — overs left)",
            "Jasprit Bumrah — 2 overs left\nHardik Pandya — 1 over left",
        )

        st.markdown("##### Conditions")
        venue = st.selectbox("Venue", [
            "Wankhede Stadium, Mumbai", "MA Chidambaram, Chennai",
            "M Chinnaswamy, Bengaluru", "Eden Gardens, Kolkata",
            "Narendra Modi, Ahmedabad", "Arun Jaitley, Delhi",
            "Rajiv Gandhi, Hyderabad", "Sawai Mansingh, Jaipur",
        ])
        pitch_type = st.selectbox("Pitch", ["Flat", "Turning", "Two-paced", "Seam-friendly"])
        dew = st.selectbox("Dew Factor", ["None", "Light", "Moderate", "Heavy"])
        impact_player = st.checkbox("Impact Player Available?", value=True)

        if st.button("🏏 Get Captain's Call", use_container_width=True):
            match_text = f"""Match State:
Innings: {innings} | Over: {overs} | Score: {score}/{wickets}{f' | Target: {target}' if innings == 2 else ''}
Batting: {batting_team} | Bowling: {bowling_team}
On Strike: {striker} | Non-Strike: {non_striker}
Bowlers remaining: {bowlers}
Pitch: {pitch_type}, {venue} | Dew: {dew}
Impact Player: {'Available' if impact_player else 'Used'}
{'Required Run Rate: ' + str(round((target - score) / ((20 - overs) * 6 / 6), 2)) if innings == 2 and overs < 20 else ''}"""
            st.session_state["match_input"] = match_text
            st.session_state["run_analysis"] = True


# ── Main Content: Run Analysis ─────────────────────────────────────────
if st.session_state.get("run_analysis"):
    st.session_state["run_analysis"] = False
    match_input = st.session_state.get("match_input", "")

    if match_input:
        st.markdown("---")

        # Show input
        with st.expander("📋 Match State Input", expanded=False):
            st.code(match_input, language="text")

        # Run the agent pipeline
        st.markdown("### 🧠 Think Tank in Action...")

        # Agent progress indicators
        progress_cols = st.columns(5)
        progress_placeholders = []
        for i, (col, (emoji, name, _)) in enumerate(zip(progress_cols, agents_info)):
            with col:
                ph = st.empty()
                ph.markdown(f'<div class="agent-card" style="text-align:center;opacity:0.4;"><div style="font-size:1.5rem;">{emoji}</div><p style="font-size:0.7rem;color:#94a3b8;">Waiting...</p></div>', unsafe_allow_html=True)
                progress_placeholders.append((ph, emoji, name))

        # Import and run agents
        try:
            from google.adk.runners import Runner
            from google.adk.sessions import InMemorySessionService
            from google.genai import types

            from ipl_captain_ai.agent import root_agent

            async def run_agent_pipeline(user_input: str):
                session_service = InMemorySessionService()
                session = await session_service.create_session(
                    app_name="ipl_captain_ai",
                    user_id="streamlit_user",
                )

                runner = Runner(
                    agent=root_agent,
                    app_name="ipl_captain_ai",
                    session_service=session_service,
                )

                user_message = types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=user_input)],
                )

                all_events = []
                agent_outputs = {}

                async for event in runner.run_async(
                    user_id="streamlit_user",
                    session_id=session.id,
                    new_message=user_message,
                ):
                    all_events.append(event)

                    # Track agent outputs from events
                    if hasattr(event, 'author') and hasattr(event, 'content'):
                        agent_name = event.author
                        if event.content and event.content.parts:
                            text_parts = [p.text for p in event.content.parts if hasattr(p, 'text') and p.text]
                            if text_parts:
                                agent_outputs[agent_name] = "\n".join(text_parts)

                # Also check session state for output keys
                final_session = await session_service.get_session(
                    app_name="ipl_captain_ai",
                    user_id="streamlit_user",
                    session_id=session.id,
                )
                if final_session and final_session.state:
                    for key in ["stats_analysis", "pitch_analysis", "strategy_proposal", "devils_dissent", "final_strategy", "final_commentary"]:
                        if key in final_session.state:
                            agent_outputs[key] = final_session.state[key]

                return agent_outputs, all_events

            # Run with progress updates
            for i, (ph, emoji, name) in enumerate(progress_placeholders):
                ph.markdown(f'<div class="agent-card" style="text-align:center;"><div style="font-size:1.5rem;">{emoji}</div><p style="font-size:0.7rem;color:#10b981;">Running...</p></div>', unsafe_allow_html=True)

            with st.spinner("🏏 The think-tank is debating... This takes 30-60 seconds."):
                agent_outputs, events = asyncio.run(run_agent_pipeline(match_input))

            # Mark all as complete
            for ph, emoji, name in progress_placeholders:
                ph.markdown(f'<div class="agent-card" style="text-align:center;"><div style="font-size:1.5rem;">{emoji}</div><p style="font-size:0.7rem;color:#10b981;">✅ Done</p></div>', unsafe_allow_html=True)

            st.success("✅ Analysis complete! The captain has made the call.")

            # ── Display Results ────────────────────────────────────
            # Final Commentary (the main output)
            final = agent_outputs.get("final_commentary") or agent_outputs.get("commentator", "")
            if final:
                st.markdown(f"""
                <div class="decision-box">
                    <h2>🏏 THE CAPTAIN'S CALL</h2>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(final)

            # Detailed Agent Outputs
            st.markdown("---")
            st.markdown("### 🔍 Agent Trace — Inside the Think Tank")

            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📊 Stats Analysis",
                "🌤️ Conditions Report",
                "🎯 Strategy Proposal",
                "😈 Devil's Advocate",
                "🔄 Final Verdict",
            ])

            with tab1:
                content = agent_outputs.get("stats_analysis") or agent_outputs.get("stats_analyst", "No output captured")
                st.markdown(content)

            with tab2:
                content = agent_outputs.get("pitch_analysis") or agent_outputs.get("pitch_conditions", "No output captured")
                st.markdown(content)

            with tab3:
                content = agent_outputs.get("strategy_proposal") or agent_outputs.get("strategist", "No output captured")
                st.markdown(content)

            with tab4:
                content = agent_outputs.get("devils_dissent") or agent_outputs.get("devils_advocate", "No output captured")
                st.markdown(content)

            with tab5:
                content = agent_outputs.get("final_strategy") or agent_outputs.get("strategist_revision", "No output captured")
                st.markdown(content)

            # Raw Event Trace (for debugging / hackathon judges)
            with st.expander("🔧 Raw Agent Events (for judges)", expanded=False):
                for i, event in enumerate(events):
                    author = getattr(event, 'author', 'unknown')
                    content_text = ""
                    if hasattr(event, 'content') and event.content and event.content.parts:
                        content_text = " | ".join([
                            p.text[:200] if hasattr(p, 'text') and p.text else str(p)[:100]
                            for p in event.content.parts
                        ])
                    if content_text:
                        st.text(f"[{i}] {author}: {content_text[:300]}...")

        except ImportError as e:
            st.error(f"❌ Import error: {e}")
            st.info("Make sure to install dependencies: `pip install -r requirements.txt`")
            st.info("And set your GOOGLE_API_KEY in a `.env` file")

        except Exception as e:
            st.error(f"❌ Agent execution error: {e}")
            st.info("Common fixes:\n1. Check your GOOGLE_API_KEY in .env\n2. Run: pip install -r requirements.txt\n3. Ensure google-adk is properly installed")
            import traceback
            with st.expander("Full Error Trace"):
                st.code(traceback.format_exc())

else:
    # ── Default: Show Architecture & Instructions ──────────────────
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ### How It Works
        
        The IPL Captain AI uses **5 Gemini-powered agents** orchestrated via **Google Agent Development Kit (ADK)** to simulate a real IPL captain's think-tank:

        1. **📊 Stats Analyst** — Fetches player data, matchup statistics, and venue history using Google Search + Player Stats DB
        2. **🌤️ Pitch & Conditions** — Analyzes weather, dew, pitch behavior via Weather API + venue analysis
        3. **🎯 Strategist** — Proposes the tactical plan (bowling changes, field setup, batting order, timeout, impact player)
        4. **😈 Devil's Advocate** — Challenges the strategy with counter-arguments and alternative plans
        5. **🎙️ Commentator** — Translates everything into engaging cricket commentary

        The **Strategist ↔ Devil's Advocate debate** is the core innovation — you see the actual back-and-forth reasoning, not just a final answer.
        """)

    with col2:
        st.markdown("""
        ### Tech Stack
        
        - **Gemini 2.5 Flash** — All agents
        - **Google ADK** — Agent orchestration
        - **ParallelAgent** — Intelligence gathering
        - **SequentialAgent** — Debate pipeline
        - **Function Calling** — 4+ real tools
        - **Google Search** — Live data grounding
        - **Streamlit** — Premium UI
        """)

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; padding: 2rem; color: #94a3b8;">
        <p style="font-size: 0.9rem;">👈 Use the sidebar to input match state and get the captain's tactical call</p>
        <p style="font-size: 0.75rem; margin-top: 1rem;">
            Built with 🏏 by Team IPL Captain AI | Google Gemini API + Agent Development Kit + Antigravity
        </p>
    </div>
    """, unsafe_allow_html=True)
