# 📊 AI Business Analyst Copilot

An autonomous, voice-activated AI Agent designed to automate end-to-end business analysis. Built with Python and Streamlit, this Copilot leverages **Llama 3.3** for reasoning and **Whisper AI** for speech recognition to query databases, forecast trends, analyze sentiment, and generate executive deliverables.

## 🚀 The Elevator Pitch
This project demonstrates the transition from traditional descriptive analytics to **AI-driven, autonomous analytics**. Instead of manually writing SQL, building charts, or drafting PowerPoint slides, users can simply speak or type commands. The Copilot securely analyzes the requested data and automatically generates the final business deliverable.

---

## 🛠️ Core Capabilities (The "Superpowers")

* **🎙️ Voice-Activated Interface:** Utilizes Groq's Whisper-Large-V3 for highly accurate Speech-to-Text, and gTTS for conversational, out-loud responses.
* **📈 Predictive Forecaster:** Integrates `scikit-learn` to clean time-series data, train a Linear Regression model, and forecast 30-day sales trends.
* **📑 Presentation Architect:** Uses `python-pptx` to analyze datasets, extract 3 key business insights, and automatically build and format a downloadable `.pptx` slide deck.
* **📄 Executive PDF Reporter:** Employs `fpdf2` to draft professional, multi-paragraph executive summaries based on raw CSV data.
* **🧠 Customer Sentiment NLP:** Uses `TextBlob` to perform Natural Language Processing on customer reviews, scoring them (Positive/Neutral/Negative) and generating distribution charts.
* **🏦 Live Financial Analyst:** Integrates `yfinance` to pull real-time Wall Street data, profit margins, and 52-week highs for dynamic market summaries.
* **🗄️ SQL Database Connector:** Reads internal company databases (`sqlite3`), writes the necessary SQL queries, and answers business questions dynamically.
* **🕸️ Web Scraper:** Utilizes `BeautifulSoup4` to parse and summarize public web pages and competitor sites.

---

## 💻 Tech Stack
* **Frontend UI:** Streamlit
* **LLM & Speech:** Groq API (Llama 3.3 70B & Whisper-Large-V3)
* **Data & ML:** Pandas, Scikit-learn, Matplotlib
* **Document Generation:** FPDF, Python-PPTX
* **NLP & Finance:** TextBlob, YFinance

---

## ⚙️ How to Run Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/YourUsername/ai-business-analyst-copilot.git](https://github.com/YourUsername/ai-business-analyst-copilot.git)
cd ai-business-analyst-copilot
