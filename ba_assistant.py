import os
import pandas as pd
import requests
import sqlite3
import subprocess
import yfinance as yf
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from groq import Groq

# 1. Setup & Authentication
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY") 
client = Groq(api_key=my_api_key)

# 2. System Prompt
sys_prompt = """You are a Senior Business Analyst mentoring Caleb. Keep answers professional and concise. 
- If asked to 'save it as [filename]', output the code clearly. 
- If given stock/financial data, provide a brief, professional summary of the company's current market position.
- If asked to 'plot', output ONLY valid Python code using pandas and matplotlib/seaborn to save 'chart.png'."""

conversation_history = [{"role": "system", "content": sys_prompt}]

print("🤖 Business Analyst Copilot Ready! (Llama 3.3 70B)")
print("🛠️  Available Tools:")
print("  - Type 'analyze csv [file]' to read data.")
print("  - Type 'plot [file.csv]' to generate a chart.")
print("  - Type 'stock [ticker]' to pull live financial data (e.g., stock AAPL).")
print("  - Type 'scrape [URL]' to read a website.")
print("  - Type 'query db [question]' to ask database questions.")
print("  - Type 'save it as [filename]' to save code.")
print("-" * 50)

# 3. The Conversation Loop
while True:
    user_message = input("You: ")
    if user_message.lower() == 'quit':
        print("\nSaving session... Goodbye!")
        break
        
    try:
        print("\nThinking...")

        # --- NEW FEATURE: THE FINANCIAL ANALYST ---
        if user_message.lower().startswith("stock "):
            ticker_symbol = user_message.split("stock ")[1].strip().upper()
            try:
                print(f"✅ SYSTEM: Pulling live market data for {ticker_symbol}...")
                stock = yf.Ticker(ticker_symbol)
                info = stock.info
                
                # Grab key financial metrics
                current_price = info.get('currentPrice', 'N/A')
                high_52 = info.get('fiftyTwoWeekHigh', 'N/A')
                low_52 = info.get('fiftyTwoWeekLow', 'N/A')
                margins = info.get('profitMargins', 'N/A')
                company_name = info.get('longName', ticker_symbol)
                
                # Format margins as a percentage if it's a number
                if margins != 'N/A':
                    margins = f"{margins * 100:.2f}%"

                # Feed the live data to the AI
                user_message = f"I just pulled live financial data for {company_name} ({ticker_symbol}). Current Price: ${current_price}. 52-Week High: ${high_52}. 52-Week Low: ${low_52}. Profit Margins: {margins}. Give me a short, professional analysis of this data."
            except Exception as e:
                print(f"❌ SYSTEM: Could not fetch stock data. Ensure the ticker is correct. Error: {e}")
                continue
        # -------------------------------------
        
        # --- THE VISUALIZER ---
        elif user_message.lower().startswith("plot "):
            csv_filename = user_message.split("plot ")[1].strip()
            try:
                df = pd.read_csv(csv_filename)
                columns = list(df.columns)
                plot_prompt = f"Write a Python script to read '{csv_filename}' (columns: {columns}) and create a chart. MUST save as 'chart.png'. Output ONLY raw Python code."
                print(f"✅ SYSTEM: Analyzing data and writing charting script...")
                
                conversation_history.append({"role": "user", "content": plot_prompt})
                chat_completion = client.chat.completions.create(messages=conversation_history, model="llama-3.3-70b-versatile")
                clean_code = chat_completion.choices[0].message.content.replace("```python", "").replace("```", "").strip()
                
                with open("temp_chart_script.py", "w") as f:
                    f.write(clean_code)
                
                print("✅ SYSTEM: Executing script to draw the chart...")
                subprocess.run(["python", "temp_chart_script.py"], check=True)
                print("📈 SYSTEM: Success! Open 'chart.png' to see your visualization.")
                continue 
            except Exception as e:
                print(f"❌ SYSTEM: Charting Error: {e}")
                continue
        # -------------------------------------

        # --- SQL DATABASE CONNECTOR ---
        elif user_message.lower().startswith("query db "):
            user_question = user_message.split("query db ")[1].strip()
            try:
                conn = sqlite3.connect('company_data.db')
                df = pd.read_sql_query("SELECT * FROM employees", conn)
                conn.close()
                user_message = f"SQLite database 'employees' table:\n\n{df.to_markdown()}\n\nQuestion: '{user_question}'. Answer and provide the SQL."
                print(f"✅ SYSTEM: Connected to database...")
            except Exception as e:
                print(f"❌ SYSTEM: Database Error: {e}")
                continue
        # -------------------------------------

        # --- WEB SCRAPER ---
        elif user_message.lower().startswith("scrape "):
            url = user_message.split("scrape ")[1].strip()
            try:
                print(f"✅ SYSTEM: Fetching data from {url}...")
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.content, 'html.parser')
                user_message = f"Scraped {url}. Raw text:\n{soup.get_text(separator=' ', strip=True)[:5000]}\n\nSummarize for a Business Analyst."
            except Exception as e:
                print(f"❌ SYSTEM: Could not scrape. Error: {e}")
                continue
        # -------------------------------------

        # --- CSV ANALYST ---
        elif "analyze csv" in user_message.lower():
            csv_filename = user_message.split("analyze csv ")[1].strip()
            try:
                df = pd.read_csv(csv_filename)
                user_message = f"Dataset: {csv_filename}. Columns: {list(df.columns)}. First 5 rows:\n{df.head().to_markdown()}\n\nAnalyze this data."
                print(f"✅ SYSTEM: Successfully read {csv_filename}...")
            except Exception as e:
                print(f"❌ SYSTEM: Could not read CSV. Error: {e}")
                continue
        # -------------------------------------

        # Standard AI Chat Logic
        conversation_history.append({"role": "user", "content": user_message})
        chat_completion = client.chat.completions.create(
            messages=conversation_history,
            model="llama-3.3-70b-versatile", 
        )
        response_text = chat_completion.choices[0].message.content
        print(f"\nAssistant: {response_text}")
        conversation_history.append({"role": "assistant", "content": response_text})

        # File Saving Logic
        cmd_list = ["scrape ", "analyze csv", "query db", "plot ", "stock "]
        if "save it as" in user_message.lower() and not any(cmd in user_message.lower() for cmd in cmd_list):
            filename = user_message.lower().split("save it as ")[1].split(" ")[0].strip()
            clean_code = response_text.replace("```python", "").replace("```sql", "").replace("```", "").strip()
            with open(filename, "w") as f:
                f.write(clean_code)
            print(f"\n✅ SYSTEM: Successfully created {filename}")
            
    except Exception as e:
        print(f"\n❌ SYSTEM: Error: {e}")
    
    print("-" * 50)