import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dealership Lead Analytics", page_icon="🚗", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/leads_anonymized.csv")
    df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
    df["month"] = df["month"].astype(str)
    df["lead_source"] = df["lead_source"].fillna("Unknown")
    df["outcome"] = df["outcome"].fillna("Unknown")
    df["payment_type"] = df["payment_type"].fillna("Unknown")
    df["vehicle_interested"] = df["vehicle_interested"].fillna("Unknown")
    df["visit_count"] = pd.to_numeric(df["visit_count"], errors="coerce").fillna(0)
    df["sold_flag"] = df["outcome"].str.contains("sold", case=False, na=False).astype(int)
    df["visit_flag"] = (df["visit_count"] > 0).astype(int)
    return df

df = load_data()

st.sidebar.title("Filters")
selected_sources = st.sidebar.multiselect("Lead Source", sorted(df["lead_source"].unique()), default=sorted(df["lead_source"].unique()))
selected_months = st.sidebar.multiselect("Month", sorted(df["month"].unique()), default=sorted(df["month"].unique()))
selected_outcomes = st.sidebar.multiselect("Outcome", sorted(df["outcome"].unique()), default=sorted(df["outcome"].unique()))

filtered = df[
    df["lead_source"].isin(selected_sources)
    & df["month"].isin(selected_months)
    & df["outcome"].isin(selected_outcomes)
].copy()

total_leads = len(filtered)
sold_deals = int(filtered["sold_flag"].sum())
visits = int(filtered["visit_flag"].sum())
close_rate = sold_deals / total_leads * 100 if total_leads else 0
visit_rate = visits / total_leads * 100 if total_leads else 0

source_summary = (
    filtered.groupby("lead_source", as_index=False)
    .agg(
        total_leads=("lead_id", "count"),
        sold_deals=("sold_flag", "sum"),
        visits=("visit_flag", "sum"),
        avg_visits=("visit_count", "mean"),
    )
)
source_summary["close_rate_percent"] = (source_summary["sold_deals"] / source_summary["total_leads"] * 100).round(2)
source_summary["visit_rate_percent"] = (source_summary["visits"] / source_summary["total_leads"] * 100).round(2)

st.title("Dealership Lead Source Performance Dashboard")
st.caption("Interactive business analytics project using anonymized dealership lead data, SQL-style KPIs, and conversion-focused marketing analysis.")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Leads", f"{total_leads:,}")
k2.metric("Sold Deals", f"{sold_deals:,}")
k3.metric("Close Rate", f"{close_rate:.2f}%")
k4.metric("Visit Rate", f"{visit_rate:.2f}%")

st.divider()

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Executive Summary",
    "Lead Source Performance",
    "Conversion Funnel",
    "Monthly Trends",
    "SQL Analysis",
    "Dataset",
])

with tab1:
    st.header("Executive Summary")
    if total_leads == 0:
        st.warning("No data available for selected filters.")
    else:
        volume_leader = source_summary.sort_values("total_leads", ascending=False).iloc[0]
        sales_leader = source_summary.sort_values("sold_deals", ascending=False).iloc[0]
        meaningful_sources = source_summary[source_summary["total_leads"] >= 5]
        conversion_leader = meaningful_sources.sort_values("close_rate_percent", ascending=False).iloc[0]

        c1, c2, c3 = st.columns(3)
        c1.subheader("Volume Leader")
        c1.metric(str(volume_leader["lead_source"]), f'{int(volume_leader["total_leads"]):,} leads')
        c2.subheader("Sales Leader")
        c2.metric(str(sales_leader["lead_source"]), f'{int(sales_leader["sold_deals"]):,} sold')
        c3.subheader("Best Close Rate")
        c3.metric(str(conversion_leader["lead_source"]), f'{conversion_leader["close_rate_percent"]:.2f}%')

        st.subheader("Business Interpretation")
        st.markdown(f"""
        This dashboard analyzes **{total_leads:,} dealership leads** to compare lead volume, sold deals,
        showroom visits, and close rates across acquisition channels.

        - **{volume_leader['lead_source']}** generated the most leads, showing strong top-of-funnel reach.
        - **{sales_leader['lead_source']}** produced the highest number of sold deals.
        - **{conversion_leader['lead_source']}** had the strongest conversion rate among meaningful-volume channels.
        - Overall close rate is **{close_rate:.2f}%**, so lead quality and follow-up strategy matter as much as lead volume.
        """)

        st.subheader("Recommendation")
        st.info(
            "Do not optimize only for lead volume. High-volume platforms should be filtered and qualified more carefully, "
            "while high-conversion sources should receive more attention through appointment-setting, faster follow-up, "
            "and showroom-focused sales strategy."
        )

with tab2:
    st.header("Lead Source Performance")
    col1, col2 = st.columns(2)
    with col1:
        leads_chart = source_summary.sort_values("total_leads", ascending=False)
        fig = px.bar(leads_chart, x="lead_source", y="total_leads", text="total_leads", title="Lead Volume by Source")
        fig.update_layout(xaxis_title="", yaxis_title="Total Leads")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        sold_chart = source_summary.sort_values("sold_deals", ascending=False)
        fig = px.bar(sold_chart, x="lead_source", y="sold_deals", text="sold_deals", title="Sold Deals by Source")
        fig.update_layout(xaxis_title="", yaxis_title="Sold Deals")
        st.plotly_chart(fig, use_container_width=True)
    st.subheader("Source Performance Table")
    st.dataframe(source_summary.sort_values("total_leads", ascending=False), use_container_width=True)

with tab3:
    st.header("Conversion Funnel")
    funnel_df = pd.DataFrame({"Stage": ["Total Leads", "In-Store Visits", "Sold Deals"], "Count": [total_leads, visits, sold_deals]})
    fig = px.funnel(funnel_df, x="Count", y="Stage", title="Overall Lead-to-Sale Funnel")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Close Rate by Source")
    close_chart = source_summary.sort_values("close_rate_percent", ascending=False)
    fig = px.bar(close_chart, x="lead_source", y="close_rate_percent", text="close_rate_percent", title="Close Rate by Lead Source")
    fig.update_layout(xaxis_title="", yaxis_title="Close Rate (%)")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("**Analyst note:** A source with fewer leads can still be more valuable if it converts at a higher rate.")

with tab4:
    st.header("Monthly Trends")
    monthly = (
        filtered.groupby("month", as_index=False)
        .agg(total_leads=("lead_id", "count"), visits=("visit_flag", "sum"), sold_deals=("sold_flag", "sum"))
        .sort_values("month")
    )
    fig = px.line(monthly, x="month", y=["total_leads", "visits", "sold_deals"], markers=True, title="Monthly Lead, Visit, and Sales Trend")
    fig.update_layout(xaxis_title="Month", yaxis_title="Count")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(monthly, use_container_width=True)

with tab5:
    st.header("SQL Analysis Used in PostgreSQL")
    st.markdown("These are the core SQL queries used to analyze the dealership lead database.")
    st.code("""
-- Total leads by source
SELECT lead_source,
       COUNT(*) AS total_leads
FROM public.leads
GROUP BY lead_source
ORDER BY total_leads DESC;
""", language="sql")
    st.code("""
-- Sold deals by source
SELECT lead_source,
       COUNT(*) AS sold_deals
FROM public.leads
WHERE outcome ILIKE '%sold%'
GROUP BY lead_source
ORDER BY sold_deals DESC;
""", language="sql")
    st.code("""
-- Close rate by source
SELECT 
  lead_source,
  COUNT(*) AS total_leads,
  COUNT(*) FILTER (WHERE outcome ILIKE '%sold%') AS sold_deals,
  ROUND(100.0 * COUNT(*) FILTER (WHERE outcome ILIKE '%sold%') / COUNT(*), 2) AS close_rate_percent
FROM public.leads
GROUP BY lead_source
ORDER BY close_rate_percent DESC;
""", language="sql")
    st.code("""
-- Payment type among sold deals
SELECT payment_type,
       COUNT(*) AS deals
FROM public.leads
WHERE outcome ILIKE '%sold%'
GROUP BY payment_type
ORDER BY deals DESC;
""", language="sql")

with tab6:
    st.header("Anonymized Dataset")
    st.markdown("Customer names, phone numbers, and private notes were removed before publishing. Only anonymized operational fields are shown.")
    public_df = filtered.drop(columns=["sold_flag", "visit_flag"], errors="ignore")
    st.dataframe(public_df, use_container_width=True)

st.divider()
st.caption("Project built with PostgreSQL, SQL, Python, Pandas, Plotly, Streamlit, and GitHub. Dataset is anonymized for privacy.")
