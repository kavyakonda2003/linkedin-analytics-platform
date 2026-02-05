import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("data/platform_analytics.csv")

# ===== PLATFORM TITLE =====
st.markdown("# 🚀 LinkedIn User Growth & Regional Intelligence Analytics Platform")
st.markdown("### Enterprise Business Intelligence Dashboard")
st.markdown("---")

# ===== EXECUTIVE OVERVIEW =====
st.subheader("📊 Executive Analytics Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Users", df["ActiveUsers"].iloc[-1])
k2.metric("New Users (This Month)", df["NewUsers"].iloc[-1])
k3.metric("Engagement Index", df["EngagementScore"].iloc[-1])
k4.metric(
    "Growth Rate",
    f"{round((df['ActiveUsers'].iloc[-1] / df['ActiveUsers'].iloc[-2] - 1) * 100, 1)}%"
)

# ===== GROWTH TREND =====
growth_chart = px.line(
    df,
    x="Month",
    y="ActiveUsers",
    markers=True,
    title="📈 Platform User Growth Over Time"
)

st.plotly_chart(growth_chart, use_container_width=True)