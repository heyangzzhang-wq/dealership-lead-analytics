# Dealership Lead Source Performance Analysis

## 1. Executive Summary

This project analyzes 534 anonymized dealership leads to understand how different lead sources perform across lead volume, sold deals, and close rate. The analysis was designed to answer a practical business question: which marketing channels generate the most valuable sales opportunities?

The strongest lead-volume source was Facebook Marketplace, while walk-in leads showed stronger conversion efficiency. This suggests that the dealership should not evaluate lead sources based only on inquiry volume. A stronger marketing strategy should measure lead quality, showroom visits, sold deals, and eventually gross profit per channel.

## 2. Business Problem

Used-car dealerships often receive leads from many sources, including Facebook Marketplace, AutoTrader, CarGurus, phone calls, referrals, and walk-ins. However, more leads do not always mean better results. Some channels generate many low-intent inquiries, while others generate fewer but more serious buyers.

The business problem is:

> Which lead sources should the dealership prioritize to improve sales conversion and marketing efficiency?

## 3. Dataset

The dataset contains 534 anonymized dealership leads. The original working file included customer names, phone numbers, and internal notes. These fields were removed before preparing the public project version.

Public fields used:

- lead_id
- date_in
- month
- lead_source
- vehicle_interested
- visit_count
- outcome
- payment_type
- trade_in

## 4. Methodology

The analysis used PostgreSQL and SQL queries to calculate:

- total leads by source
- sold deals by source
- close rate by source
- payment type breakdown among sold deals
- monthly lead and sales trends

An interactive Streamlit dashboard was then designed to allow filtering by month, lead source, and outcome.

## 5. Key Findings

### Lead Volume

Facebook Marketplace generated the largest number of leads. This shows that it is a major top-of-funnel channel for the dealership.

### Sold Deals

Facebook Marketplace also produced the most sold deals by count, but this is partly because it had far more leads than other sources.

### Close Rate

Walk-in leads had a much stronger close rate than most online channels. This suggests that customers who physically visit the showroom are usually more serious and further along in the buying process.

### Payment Type

Many sold deals were missing payment type information. This is a data-quality issue and should be improved in future tracking.

## 6. Business Recommendations

1. Continue using Facebook Marketplace for lead volume, but improve lead qualification.
2. Track appointment bookings to separate casual inquiries from serious buyers.
3. Encourage online leads to visit the showroom because in-store traffic converts better.
4. Improve data collection by adding fields for ad cost, gross profit, salesperson, appointment status, and response time.
5. Evaluate channels using both volume and close rate instead of volume only.

## 7. Future Improvements

Future versions of the project can include:

- cost per lead
- cost per sold deal
- gross profit by source
- salesperson conversion rate
- appointment booking rate
- response time analysis
- vehicle segment analysis
- Power BI or Tableau version of the dashboard

## 8. Resume Summary

Built an interactive dealership lead analytics dashboard using PostgreSQL, SQL, Python, and Streamlit to analyze 500+ real business leads, identify top lead sources, measure sales conversion rates, and recommend marketing improvements.
