import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Live AI Jobs",
    page_icon="💼",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================


@st.cache_data
def load_data():
    return pd.read_csv("output/jsearch_jobs.csv")


jobs_df = load_data()

# ==========================================================
# TITLE
# ==========================================================

st.title("💼 Live AI Jobs")

st.caption("Latest Artificial Intelligence & Machine Learning Jobs")

st.divider()

# ==========================================================
# DOWNLOAD CSV
# ==========================================================

csv = jobs_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Jobs CSV",
    data=csv,
    file_name="jsearch_jobs.csv",
    mime="text/csv",
)

# ==========================================================
# FILTERS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    company = st.selectbox(
        "🏢 Company",
        ["All"] + sorted(jobs_df["company"].dropna().unique().tolist())
    )

with col2:
    country = st.selectbox(
        "🌍 Country",
        ["All"] + sorted(jobs_df["country"].dropna().unique().tolist())
    )

with col3:
    remote = st.selectbox(
        "🏠 Remote",
        ["All", "Yes", "No"]
    )

filtered = jobs_df.copy()

if company != "All":
    filtered = filtered[filtered["company"] == company]

if country != "All":
    filtered = filtered[filtered["country"] == country]

if remote == "Yes":
    filtered = filtered[filtered["remote"] == True]

elif remote == "No":
    filtered = filtered[filtered["remote"] == False]

# ==========================================================
# SEARCH
# ==========================================================

search = st.text_input("🔍 Search Job Title")

if search:
    filtered = filtered[
        filtered["job_title"].str.contains(
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
    st.metric(
        "Jobs",
        len(filtered)
    )

with c2:
    st.metric(
        "Companies",
        filtered["company"].nunique()
    )

with c3:
    st.metric(
        "Countries",
        filtered["country"].nunique()
    )

st.divider()

# ==========================================================
# TOP COMPANIES
# ==========================================================

st.subheader("🏢 Top Hiring Companies")

company_df = (
    filtered["company"]
    .value_counts()
    .head(10)
    .reset_index()
)

company_df.columns = [
    "Company",
    "Jobs"
]

fig = px.bar(
    company_df,
    x="Company",
    y="Jobs",
    color="Jobs",
    text="Jobs",
    title="Top Hiring Companies"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# JOBS BY COUNTRY
# ==========================================================

st.subheader("🌍 Jobs by Country")

country_df = (
    filtered["country"]
    .value_counts()
    .reset_index()
)

country_df.columns = [
    "Country",
    "Jobs"
]

fig = px.pie(
    country_df,
    names="Country",
    values="Jobs",
    hole=0.45,
    title="Country Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# REMOTE VS ONSITE
# ==========================================================

st.subheader("🏠 Remote vs On-site")

remote_df = (
    filtered["remote"]
    .replace({
        True: "Remote",
        False: "On-site"
    })
    .value_counts()
    .reset_index()
)

remote_df.columns = [
    "Work Type",
    "Jobs"
]

fig = px.bar(
    remote_df,
    x="Work Type",
    y="Jobs",
    color="Jobs",
    text="Jobs",
    title="Remote vs On-site Jobs"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================================
# JOB TABLE
# ==========================================================

st.subheader("📋 Job Listings")

columns = [
    "job_title",
    "company",
    "location",
    "employment_type",
    "remote"
]

salary_cols = [
    "salary_min",
    "salary_max"
]

for col in salary_cols:
    if col in filtered.columns:
        columns.append(col)

st.dataframe(
    filtered[columns],
    use_container_width=True,
    hide_index=True
)

st.divider()

st.caption("💼 Live AI Jobs | AI Career Intelligence Platform")
