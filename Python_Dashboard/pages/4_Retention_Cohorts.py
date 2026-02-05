import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/platform_analytics.csv")

st.title("📊 User Retention Cohort Matrix")

df["Retention"] = (df["ActiveUsers"] / df["ActiveUsers"].shift(1)) * 100
df["Retention"].fillna(100, inplace=True)

cohort = df[["Month", "Retention"]]

heatmap = px.imshow(
    cohort.set_index("Month").T,
    aspect="auto",
    color_continuous_scale="Greens",
    title="Retention Cohort Heatmap (%)"
)

st.plotly_chart(heatmap, use_container_width=True)

st.dataframe(cohort)