# 🌍 Community Demographic Profiler

## 📌 Project Overview
**Title:** Building a Community Demographic Profiler with Public Data
**Goal:** Create an automated data pipeline that pulls demographic, economic, and migration data (e.g., from the U.S. Census, IRS, and BLS) for U.S. ZIP codes and counties. The final output is a Quarto-based, interactive report allowing users to explore communities based on characteristics like age distribution, income levels, net migration, and employment trends.

This project simulates a realistic data engineering and analytics workflow designed for public insight, strategic planning, or relocation support. It demonstrates the integration of multiple open datasets, robust transformation logic, and stakeholder-friendly presentation.

It’s particularly well aligned with **Analytics Engineering** and **Data Engineering** roles, showcasing:
- API integration and dataset normalization
- Schema design and structured data modeling
- Automated orchestration
- Narrative and interactive data storytelling

## 🧰 Tech Stack
- **Python** (`requests`, `pandas`, `SQLAlchemy`, [`census`](https://pypi.org/project/census/))
- **APIs**: U.S. Census Bureau ([`census`](https://pypi.org/project/census/)), IRS migration data, BLS (Bureau of Labor Statistics)
- **Database**: PostgreSQL (Neon.tech) or SQLite (for local prototyping)
- **Quarto**: For interactive HTML report hosted on GitHub Pages
- **Orchestration**: GitHub Actions or local cron jobs

## 📁 Project Structure
```bash
community-demographic-profiler/
├── config/
│   └── credentials.yaml            # API keys and config params
├── data_raw/
│   ├── census_demographics.csv
│   ├── irs_migration.csv
│   └── bls_employment.csv
├── data_clean/
│   └── combined_profiles.csv
├── db/
│   └── db_utils.py                 # DB connection and load scripts
├── scripts/
│   ├── fetch_census.py
│   ├── fetch_irs.py
│   ├── fetch_bls.py
│   ├── clean_transform.py
│   └── run_pipeline.py
├── outputs/
│   ├── logs/
│   └── profiling_notes.md         # Data caveats, assumptions
├── reports/
│   └── community_explorer.qmd     # Quarto report
├── tests/
│   └── test_cleaning.py
├── .github/
│   └── workflows/
│       └── etl_pipeline.yml       # GitHub Actions
├── README.md
└── requirements.txt
```

## ✅ Goals
- Extract demographic and economic data for selected ZIP codes or counties
- Normalize and merge datasets into unified community profiles
- Insert into a structured database for querying
- Build an interactive Quarto report for exploration
- Automate updates using cron or GitHub Actions
- Provide visual and narrative summaries of each area

## 🗓️ Timeline / Phases
1. **Data Source Review**: Select endpoints and variables (e.g., population, income, age)
2. **API Extraction**: Use Python to download data into raw files
3. **Data Cleaning + Transformation**: Join, normalize, derive new fields (e.g., age bands)
4. **Database Setup**: Create schema and load pipeline
5. **Interface Development**: Build report with summary tables, charts, and location filters
6. **Automation**: GitHub Actions or cron for scheduled data refreshes
7. **Publishing**: Host Quarto report via GitHub Pages and document key findings

## 📋 Project Board

### 🔨 In Progress
- [ ] Research and select datasets (Census, IRS, BLS)
- [ ] Define database schema and key variables
- [ ] Draft fetch scripts for one data source

### 🔜 Next Up
- [ ] Normalize and join datasets into community profiles
- [ ] Write `clean_transform.py`
- [ ] Create initial Quarto report with basic charts
- [ ] Set up database with schema.sql and db_utils.py

### ✅ Completed
- [x] Project scoped and canvas created
- [x] Project structure and tech stack defined
- [x] Quarto report starter scaffolded

## 🔗 Inspiration
This project draws from real-world questions faced by individuals and organizations: where to live, where to focus services, how communities are changing, and what economic conditions look like on the ground.
