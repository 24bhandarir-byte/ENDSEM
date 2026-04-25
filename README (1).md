# 🌿 ConsultGenie — Agentic AI Environmental Impact Report Generator

> **AI Agent System · Semester IV ECE · B.Tech ECE-B · 2025–26**

A production-grade agentic AI system that takes a product, industry, or everyday activity as input, autonomously decides whether to search the web for real-world environmental data, applies environmental analysis frameworks, generates a structured sustainability report, and evaluates its own output using an LLM-as-Judge — all in one pipeline.

🌐 **Live Demo →** `______________________________`

---

## 👥 Team

| Role | Member | Roll No. |
|------|--------|----------|
| Role A — Architect & Integrator | Sakshi Potfode | 33 |
| Role B — Builder & Deployer | Rashi Bhandari | 40 |

> **Semester:** IV &nbsp;|&nbsp; **Branch:** B.Tech ECE-B &nbsp;|&nbsp; **Department:** Electronics and Communication Engineering &nbsp;|&nbsp; **Date:** 24/04/2026

---

## 📋 Table of Contents

1. [Problem Statement](#-problem-statement)
2. [Why an Agentic Approach](#-why-an-agentic-approach)
3. [System Architecture](#-system-architecture)
4. [Agent Pipeline](#-agent-pipeline)
5. [Agent Workflow](#-agent-workflow)
6. [LLM-as-Judge](#️-llm-as-judge)
7. [Technology Stack](#-technology-stack)
8. [Key Features](#-key-features)
9. [Setup & Installation](#-setup--installation)
10. [Deployment](#-deployment)
11. [Example Output](#-example-output)
12. [Project Structure](#-project-structure)
13. [Environment Variables](#-environment-variables)

---

## 🎯 Problem Statement

**Environmental Impact Briefer**

Given a product, industry, or everyday activity, the agent autonomously researches:

- 🌍 Environmental impact
- 💨 Carbon footprint estimates
- ♻️ Sustainability alternatives

…using **Tavily Search**, and generates a structured environmental impact brief.

### Report Sections

| Section | Description |
|---------|-------------|
| Impact Overview | Environmental effects of the selected item/activity |
| Carbon Footprint Analysis | Emissions and resource usage estimation |
| Key Insights | Findings from real-world environmental research |
| Sustainability Alternatives | Eco-friendly and practical solutions |

---

## 🤖 Why an Agentic Approach

| Requirement | Why Single Prompt Fails | Why Agent Works |
|-------------|------------------------|-----------------|
| Real-time environmental data | Static training data is outdated | Tavily fetches live, current data |
| Product-specific analysis | Gives only generic answers | Context-aware, targeted reasoning |
| Structured reporting | No enforced fixed format | Multi-stage pipeline ensures structure |
| Validation & quality | No self-quality check | LLM-as-Judge evaluates the final output |

---

## 🏗️ System Architecture

The diagram below illustrates the full agentic pipeline — from user input through multi-agent processing to the final report displayed in the Streamlit UI.

![System Architecture](architecture_dig.png)

**Flow Summary:**

```
User Input → Research Agent → Data Extractor Agent → Brief Writer Agent → Final Report (UI)
```

---

## 🤖 Agent Pipeline

| Agent | Role |
|-------|------|
| 🔍 **Impact Researcher** | Collects environmental data using Tavily Search API |
| 🧠 **Data Extractor** | Filters and refines relevant environmental insights using LLM (Groq) |
| ✍️ **Brief Writer** | Generates structured environmental impact report with recommendations |
| ⚖️ **LLM-as-Judge** | Independently evaluates the final report for accuracy and usefulness |

### Agent I/O Details

| Agent | Input | Output |
|-------|-------|--------|
| Impact Researcher | Topic (user input) | Raw Research Text (unstructured data) |
| Data Extractor | Raw Research Text | Structured Data (key facts, stats, causes, effects) |
| Brief Writer | Structured Data | Final Environmental Impact Brief (Report) |

---

## 🔄 Agent Workflow

```
1. User Input
   └─ Product / industry / activity

2. Problem Decomposition
   ├─ Decide whether web search is required
   └─ Identify environmental analysis focus

3. Tavily Research (Conditional)
   └─ Fetch real-world environmental data

4. Data Extraction
   ├─ Filter relevant insights
   └─ Remove noise and duplicates

5. Report Generation
   └─ Structured environmental impact brief

6. LLM-as-Judge Evaluation
   └─ Score report quality

7. Final Output
   └─ Report + evaluation score
```

---

## ⚖️ LLM-as-Judge

The LLM-as-Judge evaluates each generated report on four dimensions:

| Criterion | Description |
|-----------|-------------|
| 📐 Structure | Is the report well-organized and formatted? |
| 🎯 Relevance | Does the content address the user's topic accurately? |
| 🧠 Reasoning | Are conclusions logically supported by the data? |
| 🛠️ Practical Usefulness | Are the sustainability alternatives actionable and realistic? |

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| 🖥️ UI | [Streamlit](https://streamlit.io/) |
| 🤖 LLM | [Groq](https://groq.com/) (Extraction & Report Generation) |
| 🔍 Search | [Tavily API](https://tavily.com/) |
| 💻 Language | Python |
| ☁️ Deployment | [Railway](https://railway.app/) |

---

## ✨ Key Features

- 🤖 **Agentic decision-making** — autonomous research and reasoning pipeline
- 🌐 **Real-time environmental research** — live web data via Tavily Search
- 💨 **Carbon footprint estimation** — structured emissions and resource analysis
- 📄 **Structured sustainability reporting** — consistent, professional report format
- ⚖️ **LLM-based evaluation** — automated quality scoring via LLM-as-Judge
- 🔍 **Step-by-step workflow transparency** — visible agent stages in the UI

---

## 🚀 Setup & Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

```env
TAVILY_API_KEY=your_tavily_key_here
GROQ_API_KEY=your_groq_key_here
```

### 4. Run Project

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The app can be deployed on any of the following platforms:

| Platform | Notes |
|----------|-------|
| [Railway](https://railway.app/) | Recommended — uses `Procfile` |
| [Render](https://render.com/) | Free tier available |
| [Hugging Face Spaces](https://huggingface.co/spaces) | Streamlit-native support |

---

## 📄 Example Output

**Input:**

```
Plastic bottle usage in daily life
```

**Output Includes:**

| Section | Content |
|---------|---------|
| 🌍 Environmental Impact Overview | Pollution data, ecosystem effects |
| 💨 Carbon Footprint Analysis | CO₂ emissions, resource extraction data |
| 🔑 Key Insights | Real-world stats and research findings |
| ♻️ Sustainable Alternatives | Reusable bottles, policy changes, bio-plastics |

---

## 🗂️ Project Structure

```
consultgenie/
├── app.py                  # Streamlit UI entry point
├── research_agent.py       # Impact Researcher Agent (Tavily Search)
├── data_extractor.py       # Data Extractor Agent (Groq LLM)
├── brief_writer.py         # Brief Writer Agent (Groq LLM)
├── judge_agent.py          # LLM-as-Judge evaluator
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment process file
└── README.md               # Project documentation
```

---

## 📦 Requirements

```txt
streamlit
groq
tavily-python
python-dotenv
```

---

## 🔒 Environment Variables

| Variable | Description | Where to Get |
|----------|-------------|--------------|
| `TAVILY_API_KEY` | Tavily web search API key | [app.tavily.com](https://app.tavily.com) |
| `GROQ_API_KEY` | Groq LLM inference API key | [console.groq.com](https://console.groq.com) |

> ⚠️ **Never** commit your `.env` file or expose API keys in public repositories. Add `.env` to your `.gitignore`.

```gitignore
# .gitignore
.env
__pycache__/
*.pyc
```

---

<div align="center">

Made with 💚 for a sustainable future &nbsp;·&nbsp; **B.Tech ECE-B, Semester IV · 2025–26**

</div>
