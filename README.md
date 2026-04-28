# Dealership Lead Source Performance Analytics

## Project Overview

This project analyzes **534 anonymized customer leads** from a real used-car dealership to evaluate lead generation performance, sales conversion efficiency, and customer acquisition quality across multiple channels.

The goal of the project was to build a real-world business intelligence dashboard that helps management answer critical sales and marketing questions such as:

- Which platforms generate the most customer inquiries?
- Which sources generate actual sold deals?
- Which lead channels have the strongest close rates?
- Which channels create low-quality or low-intent leads?
- Where should future advertising budget be allocated?

This project was built using SQL-style analysis, Python, and Streamlit to simulate a modern analyst workflow from raw data to executive dashboard reporting.

---

## Business Problem

High lead volume does **not always mean high value**.

Many dealerships focus heavily on total inquiries, but some platforms create large amounts of low-intent leads that consume salesperson time without generating revenue.

This project demonstrates how performance measurement should shift from:

**Lead Quantity → Lead Quality + Conversion Efficiency + ROI**

---

## Tools Used

- PostgreSQL
- pgAdmin
- SQL
- Python
- Pandas
- Plotly
- Streamlit
- Excel / CSV Data Cleaning
- GitHub Deployment

---

## Business Questions Answered

1. Which lead sources generate the most inquiries?
2. Which channels produce real sold deals?
3. Which sources have the highest close rate?
4. How do monthly lead trends change over time?
5. Which lead channels should receive future budget?

---

## Key Findings

### 1. Facebook Marketplace and AutoTrader generated high lead volume

Facebook Marketplace and AutoTrader produced the highest volume of inquiries.

However, much of this volume may be explained by low-friction customer behavior:

- Facebook Marketplace allows users to quickly click **“Hi, is this still available?”** with one tap.
- AutoTrader often sends automatic or template-style inquiries such as requests for Carfax reports.

Many of these leads showed low engagement and often did not continue the conversation after first contact.

This suggests these channels are strong for visibility, but weaker for lead intent quality.

---

### 2. Higher-intent sources converted better

Channels such as:

- CarGurus  
- Walk-in traffic  
- Redbook referrals  

showed meaningfully stronger closing performance.

These sources often represent customers who are:

- Further along in the buying journey  
- Comparing vehicles seriously  
- Ready to visit in person  
- More responsive during follow-up

---

### 3. Walk-in traffic showed strong buyer intent

Walk-in leads had one of the strongest conversion profiles because customers had already taken action to visit the showroom, indicating higher purchase intent than casual online inquiries.

---

### 4. Volume alone can be misleading

If management only tracks total leads, Facebook Marketplace may appear dominant.

But when measuring **sales conversion**, smaller channels can outperform high-volume sources.

This reinforces the importance of evaluating:

- Cost per lead  
- Response quality  
- Appointment rate  
- Showroom visits  
- Close rate

---

## Business Recommendations

### Continue Using Facebook Marketplace & AutoTrader for Awareness

Use these channels for top-of-funnel exposure and inventory visibility.

### Improve Qualification Process

Implement faster filtering for low-intent inquiries through:

- automated replies  
- appointment booking links  
- follow-up scoring  
- response prioritization

### Increase Focus on Higher-Converting Sources

Allocate more attention and budget toward:

- CarGurus  
- Walk-in traffic strategies  
- Referral channels such as Redbook

### Track More KPIs Going Forward

Future data collection should include:

- Ad spend by platform  
- Appointment booked rate  
- Show-up rate  
- Gross profit per deal  
- Time-to-close

---

## Skills Demonstrated

- SQL aggregation & joins
- Funnel / KPI analysis
- Data cleaning
- Dashboard development
- Executive storytelling with data
- Conversion rate optimization
- Real business analytics
- Deployment using GitHub + Streamlit

---

## Project Files

- `app.py` → Interactive dashboard  
- `queries.sql` → SQL business analysis queries  
- `data/leads_anonymized.csv` → Clean dataset  
- `README.md` → Documentation  

---

## Future Improvements

- Predictive lead scoring model
- Monthly sales forecasting
- Cost-per-acquisition dashboard
- Salesperson performance analytics
- CRM automation recommendations
- Marketing ROI model

---

## Live Dashboard

(Add your Streamlit link here)

## GitHub Repository

(Add your GitHub repo link here)
