# Metro Detroit Community Demographic Profiler

A local demographic profiling tool focused on key counties in the Metro Detroit region, built to support community insights, equity analysis, and strategic planning.

## 📊 Overview
This project pulls, cleans, and formats demographic and labor data from public sources to create consistent, ready-to-analyze profiles for Wayne, Oakland, Macomb, Washtenaw, Livingston, Lapeer, and St. Clair Counties. Built in Python using open data and reproducible code, it aims to support data-driven storytelling, grantmaking, and civic engagement.

## ✅ Features

- Focused on **Metro Detroit** counties
- Pulls data from **Census (ACS 5-Year Estimates)** and **BLS LAUS**
- Captures **population, income, race/ethnicity, education, and unemployment**
- Outputs clean `.csv` files for dashboards, policy briefs, or reports
- Easy to adapt for new counties or new metrics
- Modular Python scripts for reusability

## 📍 Counties Covered

| County     | FIPS Code |
| ---------- | --------- |
| Wayne      | 26163     |
| Oakland    | 26125     |
| Macomb     | 26099     |
| Washtenaw  | 26161     |
| Livingston | 26093     |
| Lapeer     | 26087     |
| St. Clair  | 26147     |

## 📂 Data Sources

- [U.S. Census Bureau – American Community Survey (ACS) 5-Year](https://www.census.gov/programs-surveys/acs)
- [Bureau of Labor Statistics – Local Area Unemployment Statistics (LAUS)](https://www.bls.gov/lau/)
- [Institute of Museum and Library Services - Public Libraries Survey (PLS)](https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls)
- [U.S. Department of Agriculture - Food Access Research Atlas (FARA)](https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data)

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
- Extract demographic and economic data for selected ZIP codes or counties in metro detroit
- Normalize and merge datasets into unified community profiles
- Insert into a structured database for querying
- Build an interactive Quarto report for exploration
- Automate updates using cron or GitHub Actions
- Provide visual and narrative summaries of each area
- Assess options for interactive data exploration

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
- [ ] Research and select datasets (Census, BLS, IMLS, UDSA)
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

## 📄 License
Apache License 2.0. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0.txt) for details.

