import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/platform_analytics.csv")

st.title("🔥 Engagement Analytics")

eng_chart = px.line(df, x="Month", y="EngagementScore", markers=True)
st.plotly_chart(eng_chart, use_container_width=True)