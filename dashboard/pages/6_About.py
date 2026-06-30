import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
    layout="wide"
)

# ==========================================================
# TITLE
# ==========================================================

st.title("👨‍💻 About the Developer")

st.caption("AI Career Intelligence Platform")

st.divider()

# ==========================================================
# PROFILE
# ==========================================================

col1, col2 = st.columns([1, 2])

with col1:

    st.markdown("## 👨‍💻 Akhil Soni")

    st.write("🎓 M.Tech - Artificial Intelligence & Machine Learning")

    st.write("🏫 Birla Institute of Technology, Mesra")

with col2:

    st.success(
        """
### Contact

📧 **Email**

akhilsoni150@gmail.com

---

🔗 **GitHub**

https://github.com/AkHiLS0Ni

---

🔗 **LinkedIn**

https://www.linkedin.com/in/akhil-soni-a83909290
"""
    )

st.divider()

# ==========================================================
# PROJECT
# ==========================================================

st.header("🚀 Project Overview")

st.write("""
AI Career Intelligence Platform is a portfolio-ready Data Engineering
and AI Analytics project.

The dashboard combines multiple AI data sources into one interactive
analytics platform.

### Integrated Data Sources

- GitHub API
- JSearch API
- Hugging Face
- Global AI Jobs Dataset

### Features

- GitHub Analytics
- Live AI Jobs
- Global AI Market
- Hugging Face Analytics
- AI Skills Analytics
""")

st.divider()

# ==========================================================
# TECH STACK
# ==========================================================

st.header("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### Programming

- Python

- SQL

- Pandas

- NumPy
""")

with col2:

    st.info("""
### Visualization

- Streamlit

- Plotly

- Matplotlib
""")

with col3:

    st.info("""
### Tools

- Git

- GitHub

- VS Code

- Jupyter
""")

st.divider()

# ==========================================================
# PROJECT STRUCTURE
# ==========================================================

st.header("🏗 Project Architecture")

st.code("""
GitHub API
      │
JSearch API
      │
Hugging Face
      │
Global AI Jobs
      │
──────────────
   ETL Pipeline
      │
Processed CSV
      │
Dashboard
      │
Analytics
""")

st.divider()

# ==========================================================
# ROADMAP
# ==========================================================

st.header("🗺 Future Enhancements")

st.checkbox("PostgreSQL Integration", disabled=True)

st.checkbox("Apache Airflow", disabled=True)

st.checkbox("Docker", disabled=True)

st.checkbox("AWS Deployment", disabled=True)

st.checkbox("FastAPI Backend", disabled=True)

st.checkbox("Resume Analyzer", disabled=True)

st.checkbox("AI Career Recommendation", disabled=True)

st.checkbox("LLM Integration", disabled=True)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.success(
    """
Thank you for visiting the AI Career Intelligence Platform.

⭐ If you like this project, feel free to connect with me on GitHub and LinkedIn.
"""
)

st.caption(
    "🚀 AI Career Intelligence Platform | Version 3.0 | Built by Akhil Soni"
)
