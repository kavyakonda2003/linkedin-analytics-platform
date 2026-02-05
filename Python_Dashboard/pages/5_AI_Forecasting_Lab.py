import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
import numpy as np

df = pd.read_csv("data/platform_analytics.csv")

st.title("🤖 AI Growth Forecasting Lab")

X = np.arange(len(df)).reshape(-1,1)
y = df["ActiveUsers"].values

model = RandomForestRegressor(n_estimators=200)
model.fit(X, y)

future = np.arange(len(df), len(df)+6).reshape(-1,1)
pred = model.predict(future)

future_df = pd.DataFrame({
    "Month": [f"Future {i+1}" for i in range(6)],
    "Predicted Users": pred.astype(int)
})

chart = px.line(
    future_df,
    x="Month",
    y="Predicted Users",
    markers=True,
    title="AI Forecasted User Growth"
)

st.plotly_chart(chart, use_container_width=True)
st.dataframe(future_df)