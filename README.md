# Dealership Lead Source Performance Analytics

## Project Overview

This project analyzes 534 anonymized customer leads from a used-car dealership to evaluate which lead sources generate the most inquiries, which sources produce sold deals, and which channels convert most efficiently.

The goal is to support dealership marketing and sales decisions using SQL-style business analysis and an interactive dashboard.

## Tools Used

- PostgreSQL
- pgAdmin
- SQL
- Python
- Streamlit
- Pandas
- Plotly
- Excel / CSV data cleaning

## Business Questions

1. Which lead sources generate the most customer inquiries?
2. Which lead sources produce actual sold deals?
3. Which channels have the strongest close rates?
4. How do lead volume and sold deals change over time?
5. What marketing channels should the dealership prioritize?

## Key Findings

- Facebook Marketplace generated the highest lead volume.
- Walk-in traffic had a much stronger conversion rate than most online platforms.
- Some high-volume lead sources produced low close rates, showing the importance of measuring quality, not just quantity.
- The dealership can improve ROI by tracking lead qualification, appointment booking, ad cost, and gross profit in future data collection.

## Project Files

```text
dealership_lead_analytics_project/
├── app.py
├── requirements.txt
├── queries.sql
├── README.md
├── analysis_report_draft.md
└── data/
    └── leads_anonymized.csv
```

## How to Run Locally

Install required packages:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

## Dashboard Features

- KPI cards for total leads, sold deals, close rate, and visits
- Filter by month, source, and outcome
- Lead volume by source
- Sold deals by source
- Close rate by source
- Monthly trends
- Anonymized data table

## Privacy Note

The public dataset removes customer names, phone numbers, and private notes. Only anonymized operational fields are included.
