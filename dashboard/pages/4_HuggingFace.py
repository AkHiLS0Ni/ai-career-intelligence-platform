import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Hugging Face Models",
    page_icon="📚",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================


@st.cache_data
def load_data():
    return pd.read_csv("output/huggingface_models.csv")


df = load_data()

# ==========================================================
# TITLE
# ==========================================================

st.title("📚 Hugging Face Models")

st.caption("Trending AI Models from Hugging Face")

st.divider()

# ==========================================================
# DOWNLOAD
# ==========================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Models CSV",
    data=csv,
    file_name="huggingface_models.csv",
    mime="text/csv"
)

# ==========================================================
# SEARCH
# ==========================================================

search = st.text_input("🔍 Search Model")

filtered = df.copy()

if search:
    filtered = filtered[
        filtered["model_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ==========================================================
# KPI CARDS
# ==========================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Models", len(filtered))

with c2:
    st.metric(
        "Downloads",
        f"{filtered['downloads'].sum():,}"
    )

with c3:
    st.metric(
        "Likes",
        f"{filtered['likes'].sum():,}"
    )

st.divider()

# ==========================================================
# TOP DOWNLOADS
# ==========================================================

st.subheader("⬇ Most Downloaded Models")

top_downloads = filtered.sort_values(
    by="downloads",
    ascending=False
).head(10)

fig = px.bar(
    top_downloads,
    x="model_name",
    y="downloads",
    color="downloads",
    text="downloads"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# MOST LIKED
# ==========================================================

st.subheader("❤️ Most Liked Models")

top_likes = filtered.sort_values(
    by="likes",
    ascending=False
).head(10)

fig = px.bar(
    top_likes,
    x="model_name",
    y="likes",
    color="likes",
    text="likes"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# TASK DISTRIBUTION
# ==========================================================

st.subheader("🤖 Task Distribution")

task_df = (
    filtered["task"]
    .fillna("Unknown")
    .value_counts()
    .reset_index()
)

task_df.columns = [
    "Task",
    "Models"
]

fig = px.pie(
    task_df,
    names="Task",
    values="Models",
    hole=0.45
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# AUTHORS
# ==========================================================

st.subheader("👨‍💻 Top Authors")

author_df = (
    filtered["author"]
    .fillna("Unknown")
    .value_counts()
    .head(10)
    .reset_index()
)

author_df.columns = [
    "Author",
    "Models"
]

fig = px.bar(
    author_df,
    x="Author",
    y="Models",
    color="Models",
    text="Models"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# TABLE
# ==========================================================

st.subheader("📋 Models")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.caption(
    "📚 Hugging Face Analytics | AI Career Intelligence Platform"
)
