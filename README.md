# 🏏 IPL Captain AI — Virtual IPL Think-Tank

> An agentic AI system that acts as a virtual IPL captain — making tactical decisions the way Dhoni, Rohit, or Hardik would, using **5 Gemini-powered agents** debating strategy through Google's **Agent Development Kit (ADK)**.

![Built with Gemini](https://img.shields.io/badge/Built%20with-Gemini%202.5-blue)
![ADK](https://img.shields.io/badge/Agent%20Dev%20Kit-ADK-purple)
![Antigravity](https://img.shields.io/badge/Built%20in-Antigravity-orange)

## 🏗️ Architecture

```
User Input → Captain Coordinator
                    │
                    ▼
    ┌───────────────┴───────────────┐
    │     PARALLEL: Intelligence     │
    │  ┌──────────┐  ┌───────────┐  │
    │  │📊 Stats  │  │🌤️ Pitch & │  │
    │  │ Analyst  │  │Conditions │  │
    │  └──────────┘  └───────────┘  │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │  SEQUENTIAL: Strategy Debate   │
    │  🎯 Strategist proposes        │
    │       ↓                        │
    │  😈 Devil's Advocate challenges│
    │       ↓                        │
    │  🎯 Strategist revises/defends │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │  🎙️ Match Commentator          │
    │  Translates to cricket-speak   │
    └───────────────────────────────┘
                    │
                    ▼
              Final Output
```

## 🤖 The 5 Agents

| Agent | Model | Role | Tools |
|-------|-------|------|-------|
| **Captain Coordinator** | gemini-2.5-flash | Routes input, orchestrates pipeline | Live Scraper, Player Stats |
| **Stats Analyst** | gemini-2.5-flash | Player data, matchups, venue history | Google Search, Player Stats DB, Venue Stats |
| **Pitch & Conditions** | gemini-2.5-flash | Weather, dew, pitch analysis | Weather API, Venue Stats, Google Search |
| **Strategist** | gemini-2.5-flash | Proposes tactical decisions | Win Probability Calculator, Matchup Data |
| **Devil's Advocate** | gemini-2.5-flash | Challenges the strategy | Win Probability Calculator, Matchup Data |
| **Commentator** | gemini-2.5-flash | Cricket-language output | None (pure synthesis) |

## 🛠️ Tools (Function Calling)

1. **Google Search** (built-in) — Live cricket data grounding
2. **Player Stats Database** — IPL batting/bowling statistics for 20+ players
3. **Weather API** — Real-time conditions at venue (OpenWeatherMap)
4. **Win Probability Calculator** — Mathematical model with counterfactual analysis
5. **Live Match Scraper** — Paste Cricbuzz/ESPN URL for auto-extraction

## 🚀 Quick Start

### 1. Clone & Install

```bash
cd Google-APL
pip install -r requirements.txt
```

### 2. Set API Key

```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

### 3. Run with ADK Dev UI

```bash
adk web ipl_captain_ai
```

### 4. Run with Streamlit UI

```bash
streamlit run app.py
```

## 📋 Hard Requirements Checklist

- ✅ **3+ distinct Gemini agents** — 5 agents with unique system prompts and roles
- ✅ **Real tool calls** — Google Search, Weather API, Win Probability, Player Stats DB
- ✅ **Multi-turn reasoning loop** — Strategist → Devil's Advocate → Revision (visible in output)
- ✅ **Explainability** — Commentary agent translates to cricket-speak with "why-this-not-that"

## 🏆 Stretch Goals

- ✅ **Real-time mode** — Paste Cricbuzz/ESPN URL for live state extraction
- ✅ **Confidence score + counterfactual** — Win probability with alternative strategy comparison
- ✅ **Memory across turns** — Session state persists analysis across the pipeline

## 🛠 Tech Stack

| Technology | Usage |
|---|---|
| **Gemini 2.5 Flash** | All agent LLM calls |
| **Google ADK** | Multi-agent orchestration (ParallelAgent, SequentialAgent) |
| **Google Antigravity** | Development IDE |
| **Gemini Function Calling** | 5 custom tools |
| **Google Search Grounding** | Live cricket data |
| **Streamlit** | Premium web UI |

## 📁 Project Structure

```
Google-APL/
├── ipl_captain_ai/
│   ├── __init__.py
│   ├── agent.py              # Root agent + ADK orchestration
│   ├── agents/
│   │   ├── stats_analyst.py
│   │   ├── pitch_conditions.py
│   │   ├── strategist.py
│   │   ├── devils_advocate.py
│   │   └── commentator.py
│   ├── tools/
│   │   ├── cricket_stats.py   # Player stats database
│   │   ├── weather.py         # Weather API
│   │   ├── win_probability.py # Win probability calculator
│   │   └── live_scraper.py    # URL content scraper
│   └── prompts/
│       └── system_prompts.py  # All agent system prompts
├── app.py                     # Streamlit frontend
├── requirements.txt
├── .env.example
└── README.md
```

## 📊 Example Output

**Scenario**: CSK vs MI, Over 16.2, CSK 134/4 chasing 186, Dhoni on strike

> 🏏 **THE CAPTAIN'S CALL**: Bowl Hardik Pandya now — save Bumrah's final 2 for overs 18 and 20.
>
> 🎯 **THE REASONING**: Dhoni's strike rate against medium-pace in death overs is 165.8. But Pandya's cross-seam deliveries and slower balls at Wankhede create dot balls. More importantly, burning Bumrah's overs now means you have NO answer at the death when the equation is 20 off 12.
>
> 😈 **THE DISSENT**: "You're gambling! Pandya went for 42 in his last death spell. If Dhoni gets after him now, the chase is done in this over itself. Bowl Bumrah NOW while the required rate is 14+ and the pressure is maximum."
>
> 🔄 **THE VERDICT**: We're going with Pandya because Bumrah at 18 and 20 is a proven IPL matchup — his economy of 8.2 in death overs is elite. One expensive Pandya over still leaves us with the best death bowler in the world.

---

*Built with 🏏 for the Google Gemini Hackathon — using Gemini API + Agent Development Kit + Antigravity*
