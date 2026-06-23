# 🚀 AI Career Intelligence Platform

> A production-grade Data Engineering platform that continuously collects, processes, and visualizes AI ecosystem data from multiple live sources.

## 📌 Current Version

**v0.1.0 — Project Foundation**

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

The AI ecosystem changes every day.

New AI models are released, companies publish new job openings, GitHub repositories become popular overnight, and AI news evolves rapidly.

Keeping track of all this information requires visiting multiple websites.

**AI Career Intelligence Platform** solves this problem by automatically collecting data from multiple public sources, processing it through an ETL pipeline, storing it in a database, and presenting it through an interactive dashboard.

This project is built as a **production-style Data Engineering project**, focusing on real-world engineering practices rather than simple data analysis.

---

# 🎯 Problem Statement

AI professionals and students spend significant time searching across multiple platforms for:

- Latest AI news
- Trending GitHub repositories
- Popular Hugging Face models
- AI job opportunities
- Emerging technologies

This platform centralizes these data sources into a single automated intelligence dashboard.

---

## 🏗️ System Architecture

```text
                  Live Data Sources
     ┌─────────────────────────────────────┐
     │                                     │
     │  GitHub API                         │
     │  AI News API                        │
     │  Hugging Face API                   │
     │  Job RSS / Public APIs              │
     └─────────────────────────────────────┘
                      │
                      ▼
             Data Ingestion Services
                      │
                      ▼
               Raw JSON Storage
                      │
                      ▼
             ETL Pipeline (Python)
                      │
                      ▼
             PostgreSQL Database
                      │
                      ▼
                 FastAPI Backend
                      │
                      ▼
             Streamlit Dashboard
                      │
                      ▼
               Live Cloud Deployment
```

---

# ✨ Features

### Data Collection

- Collect AI news automatically
- Fetch trending GitHub repositories
- Track Hugging Face trending models
- Aggregate AI job opportunities

### ETL Pipeline

- Automated extraction
- Data validation
- Data cleaning
- Data transformation
- Logging
- Error handling

### Database

- PostgreSQL storage
- Historical data
- Efficient querying

### Dashboard

- AI News Feed
- Trending GitHub Projects
- Popular AI Models
- AI Hiring Trends
- Technology Insights
- Search & Filtering

### Automation

- Scheduled ETL jobs
- Automatic updates
- Live deployment

---

# 🛠️ Tech Stack

| Category        | Technology      |
| --------------- | --------------- |
| Language        | Python          |
| API Integration | Requests        |
| Data Processing | Pandas          |
| Database        | PostgreSQL      |
| Dashboard       | Streamlit       |
| Scheduler       | GitHub Actions  |
| Deployment      | Streamlit Cloud |
| Version Control | Git & GitHub    |

---

# 📂 Project Structure

```text
ai-career-intelligence-platform/

│
├── ingestion/
│
├── transform/
│
├── validation/
│
├── database/
│
├── dashboard/
│
├── scheduler/
│
├── config/
│
├── tests/
│
├── logs/
│
├── raw_data/
│
├── requirements.txt
│
├── README.md
│
└── .env
```

---

# 🚀 Development Roadmap

## Phase 1 — Foundation

- [x] Git & GitHub
- [x] FastAPI Setup
- [x] Virtual Environment
- [x] Professional Project Structure

## Phase 2 — Data Ingestion

- [ ] GitHub API
- [ ] AI News API
- [ ] Hugging Face API
- [ ] Job Data Collection
- [ ] Raw JSON Storage

## Phase 3 — Data Engineering

- [ ] PostgreSQL
- [ ] SQLAlchemy
- [ ] ETL Pipeline
- [ ] Data Validation
- [ ] Logging

## Phase 4 — Dashboard

- [ ] Streamlit
- [ ] Charts
- [ ] Search
- [ ] Filters

## Phase 5 — Production

- [ ] GitHub Actions
- [ ] Deployment
- [ ] Docker
- [ ] CI/CD

---

# 📊 Future Enhancements

- Docker support
- Apache Airflow
- Kubernetes deployment
- AWS deployment
- Machine Learning recommendations
- Email alerts
- User authentication
- REST API

---

# 🎓 Learning Objectives

This project demonstrates practical experience with:

- REST APIs
- ETL Pipelines
- Data Engineering
- PostgreSQL
- Python
- Data Validation
- Data Cleaning
- Dashboard Development
- CI/CD
- Automation
- Cloud Deployment

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Akhil Soni**

M.Tech (AI & ML)

Building real-world Data Engineering projects one pipeline at a time.
