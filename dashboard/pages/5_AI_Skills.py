import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Skills Analytics",
    page_icon="🧠",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================


@st.cache_data
def load_data():
    return pd.read_csv("output/ai_skills_report.csv")


df = load_data()

# ==========================================================
# TITLE
# ==========================================================

st.title("🧠 AI Skills Analytics")

st.caption("Most Demanded Skills in Artificial Intelligence Jobs")

st.divider()

# ==========================================================
# DOWNLOAD
# ==========================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Skills Report",
    data=csv,
    file_name="ai_skills_report.csv",
    mime="text/csv"
)

# ==========================================================
# SEARCH
# ==========================================================

search = st.text_input("🔍 Search Skill")

filtered = df.copy()

if search:
    filtered = filtered[
        filtered["Skill"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ==========================================================
# KPI
# ==========================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Skills",
        len(filtered)
    )

with c2:
    st.metric(
        "Total Mentions",
        int(filtered["Count"].sum())
    )

with c3:
    if len(filtered):
        st.metric(
            "Top Skill",
            filtered.iloc[0]["Skill"]
        )
    else:
        st.metric(
            "Top Skill",
            "-"
        )

st.divider()

# ==========================================================
# TOP SKILLS
# ==========================================================

st.subheader("📊 Most Demanded AI Skills")

top_skills = filtered.sort_values(
    by="Count",
    ascending=False
)

fig = px.bar(
    top_skills,
    x="Skill",
    y="Count",
    color="Count",
    text="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# PIE CHART
# ==========================================================

st.subheader("🥧 Skills Distribution")

fig = px.pie(
    top_skills,
    names="Skill",
    values="Count",
    hole=0.45
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# TABLE
# ==========================================================

st.subheader("📋 Skills Dataset")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# LEARNING ROADMAP
# ==========================================================

st.subheader("🚀 Suggested Learning Roadmap")

st.success("""
1️⃣ Python

2️⃣ SQL

3️⃣ Pandas

4️⃣ NumPy

5️⃣ Data Visualization

6️⃣ Machine Learning

7️⃣ Deep Learning

8️⃣ PyTorch / TensorFlow

9️⃣ Docker

🔟 AWS / Azure

1️⃣1️⃣ Airflow

1️⃣2️⃣ Spark

1️⃣3️⃣ MLOps
""")

st.divider()

st.caption(
    "🧠 AI Skills | AI Career Intelligence Platform"
)
