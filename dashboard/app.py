import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Career Intelligence Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD DATA
# ==========================================================


@st.cache_data
def load_data():

    github = pd.read_csv("output/github_repositories.csv")
    jobs = pd.read_csv("output/jsearch_jobs.csv")
    global_jobs = pd.read_csv("output/global_ai_jobs.csv")
    models = pd.read_csv("output/huggingface_models.csv")
    skills = pd.read_csv("output/ai_skills_report.csv")

    return github, jobs, global_jobs, models, skills


github_df, jobs_df, global_df, models_df, skills_df = load_data()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🤖 AI Career")

    st.caption("Intelligence Platform")

    st.divider()

    st.success("Version 3.0")

    st.markdown("### 🚀 Dashboard")

    st.info(
        """
Use the navigation above to explore:

⭐ GitHub Analytics

💼 Live AI Jobs

🌍 Global AI Market

📚 Hugging Face

🧠 AI Skills

👨‍💻 About
"""
    )

    st.divider()

    st.markdown("### 👨‍💻 Developer")

    st.write("**Akhil Soni**")

    st.caption("M.Tech AI & ML")

# ==========================================================
# TITLE
# ==========================================================

st.title("🤖 AI Career Intelligence Platform")

st.caption(
    "Production Grade AI Analytics & Data Engineering Dashboard"
)

st.divider()

# ==========================================================
# KPI CARDS
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "💼 AI Jobs",
        f"{len(global_df):,}"
    )

with c2:

    st.metric(
        "⭐ GitHub Repositories",
        len(github_df)
    )

with c3:

    st.metric(
        "📚 Hugging Face Models",
        len(models_df)
    )

with c4:

    st.metric(
        "🧠 AI Skills",
        len(skills_df)
    )

st.divider()

# ==========================================================
# DATA SUMMARY
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("📊 Dataset Summary")

    summary = pd.DataFrame(
        {
            "Dataset": [
                "GitHub",
                "Live Jobs",
                "Global AI Jobs",
                "Hugging Face",
                "AI Skills"
            ],
            "Records": [
                len(github_df),
                len(jobs_df),
                len(global_df),
                len(models_df),
                len(skills_df)
            ]
        }
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("📌 Project Overview")

    st.success(
        """
✔ GitHub Analytics

✔ Live AI Jobs

✔ Global AI Market

✔ Hugging Face Analytics

✔ AI Skills Analytics

✔ Interactive Dashboard
"""
    )

    st.info(
        f"🕒 Last Updated\n\n{datetime.now().strftime('%d %b %Y %I:%M %p')}"
    )

st.divider()

# ==========================================================
# PLATFORM DESCRIPTION
# ==========================================================

st.subheader("🚀 About This Platform")

st.write(
    """
The **AI Career Intelligence Platform** is a portfolio project built to
analyze the Artificial Intelligence ecosystem.

The dashboard integrates multiple data sources and provides interactive
analytics for:

- GitHub AI repositories
- Live AI jobs
- Global AI job market
- Hugging Face models
- AI skills demand

Use the **left sidebar** to navigate through the dashboard pages.
"""
)

st.divider()

# ==========================================================
# QUICK STATS
# ==========================================================

st.subheader("📈 Quick Insights")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "⭐ Total GitHub Stars",
        f"{github_df['stars'].sum():,}"
    )

    st.metric(
        "🍴 Total Forks",
        f"{github_df['forks'].sum():,}"
    )

with col2:

    st.metric(
        "🏢 Companies Hiring",
        jobs_df["company"].nunique()
    )

    st.metric(
        "🌍 Countries",
        global_df["country"].nunique()
    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "🚀 AI Career Intelligence Platform | Version 3.0 | Built by Akhil Soni"
)
