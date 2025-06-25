# main.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set(style="whitegrid")

# ---------------------
# Load Data
# ---------------------
sentiment_df = pd.read_csv('fear_greed_index.csv')
trader_df = pd.read_csv('historical_data.csv')

# ---------------------
# Preprocessing
# ---------------------
# Convert date columns
sentiment_df['date'] = pd.to_datetime(sentiment_df['date']).dt.date
trader_df['Timestamp IST'] = pd.to_datetime(trader_df['Timestamp IST'], format='%d-%m-%Y %H:%M')
trader_df['date'] = trader_df['Timestamp IST'].dt.date

# Merge on 'date'
merged_df = pd.merge(trader_df, sentiment_df[['date', 'classification']], on='date', how='left')

# ---------------------
# Step 1: Avg PnL by Sentiment
# ---------------------
avg_pnl_by_sentiment = merged_df.groupby('classification')['Closed PnL'].mean().sort_values()

print("\n--- Average Closed PnL by Market Sentiment ---")
print(avg_pnl_by_sentiment)

# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_pnl_by_sentiment.index, y=avg_pnl_by_sentiment.values, palette='coolwarm')
plt.ylabel("Average Closed PnL")
plt.xlabel("Market Sentiment")
plt.title("Average Trader Performance by Market Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------
# Step 2: Time-Series Total PnL by Sentiment
# ---------------------
# Aggregate daily total Closed PnL and most common sentiment
daily_pnl = merged_df.groupby('date').agg({
    'Closed PnL': 'sum',
    'classification': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown'
}).reset_index()

# Convert date to datetime for plotting
daily_pnl['date'] = pd.to_datetime(daily_pnl['date'])

# Line Plot
plt.figure(figsize=(14, 6))
sns.lineplot(data=daily_pnl, x='date', y='Closed PnL', hue='classification', palette='Set2')
plt.title("Daily Total Closed PnL Over Time by Market Sentiment")
plt.xlabel("Date")
plt.ylabel("Total Closed PnL")
plt.legend(title='Sentiment', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# ---------------------
# Step 3: Trade Metrics by Sentiment
# ---------------------

# Aggregate by sentiment
metrics_by_sentiment = merged_df.groupby('classification').agg({
    'Size USD': 'sum',
    'Fee': 'mean',
    'Closed PnL': 'mean',
    'Account': 'count'
}).rename(columns={
    'Size USD': 'Total Volume (USD)',
    'Fee': 'Average Fee',
    'Closed PnL': 'Average PnL',
    'Account': 'Number of Trades'
}).sort_values(by='Total Volume (USD)', ascending=False)

print("\n--- Trade Metrics by Sentiment ---")
print(metrics_by_sentiment)

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=metrics_by_sentiment.index, y=metrics_by_sentiment['Total Volume (USD)'], palette='Blues_d')
plt.title("Total Trade Volume by Market Sentiment")
plt.ylabel("Total Volume (USD)")
plt.xlabel("Market Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=metrics_by_sentiment.index, y=metrics_by_sentiment['Average Fee'], palette='Oranges')
plt.title("Average Fee by Market Sentiment")
plt.ylabel("Average Fee (USD)")
plt.xlabel("Market Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Merge on 'date'
merged_df = pd.merge(trader_df, sentiment_df[['date', 'classification']], on='date', how='left')

# ✅ Save for Streamlit
merged_df.to_csv("merged_data.csv", index=False)
