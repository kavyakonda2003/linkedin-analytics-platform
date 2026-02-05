import streamlit as st
import pandas as pd
import plotly.express as px

# ======================
# LOAD DATA
# ======================

df = pd.read_csv("data/platform_analytics.csv")

st.title("🌍 Regional Growth Intelligence")

# ======================
# FILTERS
# ======================

countries = ["India", "USA", "UK", "Canada"]

country_filter = st.multiselect(
    "🌎 Select Countries",
    countries,
    default=countries
)

filtered_df = df[["Month"] + country_filter]
# ======================
# REGION KPIs
# ======================

latest = df.iloc[-1]
previous = df.iloc[-2]

total_users = sum(latest[c] for c in country_filter)
prev_total = sum(previous[c] for c in country_filter)

growth_percent = round(((total_users - prev_total) / prev_total) * 100, 2)

growth_by_country = {
    c: latest[c] - previous[c]
    for c in country_filter
}

fastest_region = max(growth_by_country, key=growth_by_country.get)

k1, k2, k3 = st.columns(3)

k1.metric("🌍 Total Users (Selected Regions)", f"{int(total_users):,}")
k2.metric("📈 Growth %", f"{growth_percent}%")
k3.metric("🚀 Fastest Growing Region", fastest_region)

st.markdown("---")

# ======================
# REGIONAL GROWTH TRENDS
# ======================

trend_df = filtered_df.melt(
    id_vars="Month",
    var_name="Country",
    value_name="Users"
)

trend_chart = px.line(
    trend_df,
    x="Month",
    y="Users",
    color="Country",
    markers=True,
    title="📈 Regional Growth Trends"
)

st.plotly_chart(trend_chart, use_container_width=True, key="regional_trend")

# ======================
# WORLD MAP (LATEST MONTH)
# ======================

latest = df.iloc[-1]

map_df = pd.DataFrame({
    "Country": country_filter,
    "Users": [latest[c] for c in country_filter]
})

map_chart = px.choropleth(
    map_df,
    locations="Country",
    locationmode="country names",
    color="Users",
    color_continuous_scale="Blues",
    title="🌍 Global User Distribution"
)

st.plotly_chart(map_chart, use_container_width=True, key="regional_map")

# ======================
# GROWTH CONTRIBUTION PIE (EXECUTIVE VIEW)
# ======================

growth = df.iloc[-1][country_filter] - df.iloc[0][country_filter]

growth_df = pd.DataFrame({
    "Country": country_filter,
    "Growth": growth.values
})

growth_pie = px.pie(
    growth_df,
    names="Country",
    values="Growth",
    title="🥧 Growth Contribution by Country",
    hole=0.4
)

st.plotly_chart(growth_pie, use_container_width=True, key="growth_pie")

# ======================
# DATA SNAPSHOT
# ======================

st.subheader("📋 Latest Regional Metrics")
st.dataframe(map_df, use_container_width=True)