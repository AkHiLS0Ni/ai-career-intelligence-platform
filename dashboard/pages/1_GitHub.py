import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="GitHub Analytics",
    page_icon="⭐",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================


@st.cache_data
def load_data():
    return pd.read_csv("output/github_repositories.csv")


github_df = load_data()

# ==========================================================
# TITLE
# ==========================================================

st.title("⭐ GitHub Repository Analytics")

st.caption("Trending Artificial Intelligence repositories from GitHub")

st.divider()

# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

csv = github_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download GitHub CSV",
    data=csv,
    file_name="github_repositories.csv",
    mime="text/csv",
)

# ==========================================================
# KPI CARDS
# ==========================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Repositories",
        len(github_df)
    )

with c2:
    st.metric(
        "Total Stars",
        f"{github_df['stars'].sum():,}"
    )

with c3:
    st.metric(
        "Total Forks",
        f"{github_df['forks'].sum():,}"
    )

st.divider()

# ==========================================================
# SEARCH
# ==========================================================

search = st.text_input(
    "🔍 Search Repository"
)

filtered = github_df.copy()

if search:

    filtered = filtered[
        filtered["repository"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ==========================================================
# TOP STARRED REPOSITORIES
# ==========================================================

st.subheader("⭐ Top 10 Starred Repositories")

top_starred = filtered.sort_values(
    by="stars",
    ascending=False
).head(10)

fig = px.bar(
    top_starred,
    x="repository",
    y="stars",
    color="stars",
    text="stars",
    title="Top Starred GitHub Repositories"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# LANGUAGE DISTRIBUTION
# ==========================================================

st.subheader("🐍 Programming Languages")

language = (
    filtered["language"]
    .fillna("Unknown")
    .value_counts()
    .reset_index()
)

language.columns = [
    "Language",
    "Repositories"
]

fig = px.pie(
    language,
    names="Language",
    values="Repositories",
    hole=0.45,
    title="Repository Language Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# STARS VS FORKS
# ==========================================================

st.subheader("📈 Stars vs Forks")

fig = px.scatter(
    filtered,
    x="stars",
    y="forks",
    hover_name="repository",
    color="language",
    size="stars",
    title="Stars vs Forks"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# DATA TABLE
# ==========================================================

st.subheader("📋 Repository Dataset")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.caption("⭐ GitHub Analytics | AI Career Intelligence Platform")
