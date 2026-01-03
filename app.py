import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="IPL 2025 Cricket Dashboard",
    page_icon="🏏",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("cricket_players.csv")

# ---------------- TITLE ----------------
st.title("🏏 IPL 2025 Cricket Player Dashboard")
st.markdown("One-page interactive dashboard for 10 IPL players (2025 teams)")

# ---------------- KPI SECTION ----------------
k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Players", len(df))
k2.metric("Top Run Scorer", df.loc[df["Runs"].idxmax(), "Player"])
k3.metric("Top Wicket Taker", df.loc[df["Wickets"].idxmax(), "Player"])
k4.metric("Best Batting Average", df.loc[df["Average"].idxmax(), "Player"])

st.divider()

# ---------------- PLAYER PROFILE CARDS ----------------
st.subheader("🧑 Player Profiles")

card_cols = st.columns(5)  # 5 cards per row

for i, row in df.iterrows():
    with card_cols[i % 5]:
        st.image(row["Photo"], width=120)
        st.markdown(f"**{row['Player']}**")
        st.image(row["TeamLogo"], width=60)
        st.write(f"Runs: {row['Runs']}")
        st.write(f"Wickets: {row['Wickets']}")
        st.write(f"Strike Rate: {row['StrikeRate']}")

st.divider()

# ---------------- CHARTS : ROW 1 ----------------
c1, c2 = st.columns(2)

fig1 = px.bar(
    df.sort_values("Runs", ascending=False),
    x="Runs",
    y="Player",
    orientation="h",
    title="🏏 Top Run Scorers",
    template="plotly_dark"
)
c1.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    df.sort_values("Wickets", ascending=False),
    x="Player",
    y="Wickets",
    title="🎯 Wickets Taken",
    template="plotly_dark"
)
c2.plotly_chart(fig2, use_container_width=True)

# ---------------- CHARTS : ROW 2 ----------------
c3, c4 = st.columns(2)

fig3 = px.scatter(
    df,
    x="Runs",
    y="StrikeRate",
    size="Matches",
    color="Team",
    hover_name="Player",
    title="🔥 Runs vs Strike Rate",
    template="plotly_dark"
)
c3.plotly_chart(fig3, use_container_width=True)

fig4 = px.pie(
    df,
    values="Runs",
    names="Team",
    hole=0.4,
    title="📊 Team-wise Run Contribution",
    template="plotly_dark"
)
c4.plotly_chart(fig4, use_container_width=True)

# ---------------- FOOTER ----------------
st.divider()
st.caption("📊 IPL 2025 Dashboard | Streamlit • Pandas • Plotly")
