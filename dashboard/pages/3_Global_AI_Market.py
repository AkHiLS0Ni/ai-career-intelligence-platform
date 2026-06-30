import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Global AI Market",
    page_icon="🌍",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================


@st.cache_data
def load_data():
    return pd.read_csv("output/global_ai_jobs.csv")


df = load_data()

# ==========================================================
# TITLE
# ==========================================================

st.title("🌍 Global AI Market Analytics")

st.caption("AI Job Market Analysis using 90,000+ Global AI Jobs")

st.divider()

# ==========================================================
# DOWNLOAD
# ==========================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Dataset",
    data=csv,
    file_name="global_ai_jobs.csv",
    mime="text/csv",
)

# ==========================================================
# FILTERS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    country = st.selectbox(
        "🌍 Country",
        ["All"] + sorted(df["country"].dropna().unique())
    )

with col2:
    role = st.selectbox(
        "💼 Job Role",
        ["All"] + sorted(df["job_role"].dropna().unique())
    )

with col3:
    specialization = st.selectbox(
        "🤖 AI Specialization",
        ["All"] + sorted(df["ai_specialization"].dropna().unique())
    )

filtered = df.copy()

if country != "All":
    filtered = filtered[filtered["country"] == country]

if role != "All":
    filtered = filtered[filtered["job_role"] == role]

if specialization != "All":
    filtered = filtered[
        filtered["ai_specialization"] == specialization
    ]

# ==========================================================
# KPI
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Jobs", f"{len(filtered):,}")

with c2:
    st.metric("Countries", filtered["country"].nunique())

with c3:
    st.metric("Roles", filtered["job_role"].nunique())

with c4:
    if "salary_usd" in filtered.columns:
        st.metric(
            "Average Salary",
            f"${filtered['salary_usd'].mean():,.0f}"
        )
    else:
        st.metric("Average Salary", "N/A")

st.divider()

# ==========================================================
# TOP COUNTRIES
# ==========================================================

st.subheader("🌍 Top Hiring Countries")

country_df = (
    filtered["country"]
    .value_counts()
    .head(10)
    .reset_index()
)

country_df.columns = ["Country", "Jobs"]

fig = px.bar(
    country_df,
    x="Country",
    y="Jobs",
    color="Jobs",
    text="Jobs",
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# TOP JOB ROLES
# ==========================================================

st.subheader("💼 Top AI Roles")

role_df = (
    filtered["job_role"]
    .value_counts()
    .head(10)
    .reset_index()
)

role_df.columns = ["Role", "Jobs"]

fig = px.bar(
    role_df,
    x="Role",
    y="Jobs",
    color="Jobs",
    text="Jobs",
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SPECIALIZATIONS
# ==========================================================

st.subheader("🤖 AI Specializations")

spec_df = (
    filtered["ai_specialization"]
    .value_counts()
    .reset_index()
)

spec_df.columns = [
    "Specialization",
    "Jobs"
]

fig = px.pie(
    spec_df,
    names="Specialization",
    values="Jobs",
    hole=0.45,
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# EXPERIENCE LEVEL
# ==========================================================

if "experience_level" in filtered.columns:

    st.subheader("📈 Experience Level")

    exp_df = (
        filtered["experience_level"]
        .value_counts()
        .reset_index()
    )

    exp_df.columns = [
        "Experience",
        "Jobs"
    ]

    fig = px.bar(
        exp_df,
        x="Experience",
        y="Jobs",
        color="Jobs",
        text="Jobs",
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# DATA TABLE
# ==========================================================

st.subheader("📋 Dataset Preview")

st.dataframe(
    filtered.head(100),
    use_container_width=True,
    hide_index=True,
)

st.divider()

st.caption(
    "🌍 Global AI Market | AI Career Intelligence Platform"
)
