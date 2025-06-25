# 📈 Trader Performance vs Market Sentiment Analysis

This project explores the relationship between **Bitcoin market sentiment** (Fear/Greed index) and **real-world trader performance** using historical trade data from Hyperliquid. The objective is to uncover patterns and insights that can guide smarter trading strategies.

---

## 📂 Dataset Overview

### 1. 🧠 Fear & Greed Index
- Columns: `timestamp`, `value`, `classification`, `date`
- Represents the daily sentiment of the Bitcoin market.

### 2. 💼 Hyperliquid Trader Data
- Columns: `Account`, `Execution Price`, `Size USD`, `Side`, `Closed PnL`, `Fee`, `Timestamp IST`, etc.
- Captures granular trade details for thousands of trades across multiple accounts.

## Link to dataset   
### Historical Data    

- https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing    

### Fear Greed Index link:    

- https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing     


---

## 🎯 Project Objectives

- Merge sentiment and trade data based on date
- Analyze how trader **PnL**, **volume**, and **fees** vary with sentiment
- Visualize trends and derive actionable insights
- Build an **interactive dashboard** using **Streamlit**

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas**, **Matplotlib**, **Seaborn**
- **Streamlit** (for interactive dashboard)
- **VS Code** (development environment)

---

## 🚀 How to Run Locally
# Create virtual environment (optional)
python -m venv venv
# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install pandas matplotlib seaborn streamlit

### 🔹 To create `merged_data.csv`:   
Run:
```bash   
python main.py     


# Run the preprocessing + analysis
python main.py      
python -m streamlit run app.py


### 1. Clone this repo

```bash
git clone https://github.com/your-username/trader-sentiment-analysis.git
cd trader-sentiment-analysis
