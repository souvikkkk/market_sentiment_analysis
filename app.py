import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📈 Trader Performance vs Market Sentiment")

# Load merged data
merged_df = pd.read_csv("merged_data.csv", parse_dates=['Timestamp IST'])

# Plot 1: Avg PnL
st.subheader("Average PnL by Sentiment")
avg_pnl = merged_df.groupby('classification')['Closed PnL'].mean().sort_values()
st.bar_chart(avg_pnl)

# Plot 2: Daily PnL
st.subheader("Daily Total PnL Over Time")
merged_df['date'] = pd.to_datetime(merged_df['Timestamp IST']).dt.date
daily = merged_df.groupby(['date', 'classification'])['Closed PnL'].sum().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=daily, x='date', y='Closed PnL', hue='classification', ax=ax)
st.pyplot(fig)
