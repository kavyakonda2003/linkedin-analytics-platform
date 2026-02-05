import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/platform_analytics.csv")

st.title("📈 Growth Analytics")

new_users = px.bar(df, x="Month", y="NewUsers", title="Monthly New Users")
st.plotly_chart(new_users, use_container_width=True)

total_users = px.line(df, x="Month", y="ActiveUsers", markers=True)
st.plotly_chart(total_users, use_container_width=True)