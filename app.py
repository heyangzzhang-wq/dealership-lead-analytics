import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Dealership Lead Analytics",
    page_icon="🚗",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/leads_anonymized.csv")
    df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
    df["month"] = df["month"].astype(str)
    df["lead_source"] = df["lead_source"].fillna("Unknown")
    df["outcome"] = df["outcome"].fillna("Unknown")
    df["payment_type"] = df["payment_type"].fillna("Unknown")
    df["visit_count"] = pd.to_numeric(df["visit_count"], errors="coerce").fillna(0)
    df["sold_flag"] = df["outcome"].str.contains("sold", case=False, na=False).astype(int)
    return df

df = load_data()

st.title("Dealership Lead Source Performance Dashboard")
st.caption("Interactive analysis of anonymized dealership leads using SQL-style business KPIs.")

with st.sidebar:
    st.header("Filters")
    sources = sorted(df["lead_source"].dropna().unique())
    selected_sources = st.multiselect("Lead source", sources, default=sources)
    months = sorted(df["month"].dropna().unique())
    selected_months = st.multiselect("Month", months, default=months)
    outcomes = sorted(df["outcome"].dropna().unique())
    selected_outcomes = st.multiselect("Outcome", outcomes, default=outcomes)

filtered = df[
    df["lead_source"].isin(selected_sources)
    & df["month"].isin(selected_months)
    & df["outcome"].isin(selected_outcomes)
].copy()

total_leads = len(filtered)
sold_deals = int(filtered["sold_flag"].sum())
close_rate = (sold_deals / total_leads * 100) if total_leads else 0
visited = int((filtered["visit_count"] > 0).sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Leads", f"{total_leads:,}")
c2.metric("Sold Deals", f"{sold_deals:,}")
c3.metric("Close Rate", f"{close_rate:.2f}%")
c4.metric("In-Store Visits", f"{visited:,}")

st.divider()

source_summary = (
    filtered.groupby("lead_source", as_index=False)
    .agg(
        total_leads=("lead_id", "count"),
        sold_deals=("sold_flag", "sum"),
        avg_visits=("visit_count", "mean")
    )
)
source_summary["close_rate_percent"] = (
    source_summary["sold_deals"] / source_summary["total_leads"] * 100
).round(2)
source_summary = source_summary.sort_values("total_leads", ascending=False)

tab1, tab2, tab3, tab4 = st.tabs([
    "Lead Sources",
    "Conversion Rate",
    "Monthly Trend",
    "Data Table"
])

with tab1:
    st.subheader("Lead Volume by Source")
    fig = px.bar(
        source_summary,
        x="lead_source",
        y="total_leads",
        text="total_leads",
        title="Which channels generate the most leads?"
    )
    fig.update_layout(xaxis_title="", yaxis_title="Leads")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Sold Deals by Source")
    sold_summary = source_summary.sort_values("sold_deals", ascending=False)
    fig2 = px.bar(
        sold_summary,
        x="lead_source",
        y="sold_deals",
        text="sold_deals",
        title="Which channels produce actual sales?"
    )
    fig2.update_layout(xaxis_title="", yaxis_title="Sold Deals")
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Close Rate by Source")
    cr = source_summary.sort_values("close_rate_percent", ascending=False)
    fig3 = px.bar(
        cr,
        x="lead_source",
        y="close_rate_percent",
        text="close_rate_percent",
        title="Which channels convert best?"
    )
    fig3.update_layout(xaxis_title="", yaxis_title="Close Rate (%)")
    st.plotly_chart(fig3, use_container_width=True)

    st.dataframe(
        cr[["lead_source", "total_leads", "sold_deals", "close_rate_percent", "avg_visits"]],
        use_container_width=True
    )

with tab3:
    st.subheader("Monthly Lead and Sales Trend")
    monthly = (
        filtered.groupby("month", as_index=False)
        .agg(total_leads=("lead_id", "count"), sold_deals=("sold_flag", "sum"))
        .sort_values("month")
    )
    fig4 = px.line(
        monthly,
        x="month",
        y=["total_leads", "sold_deals"],
        markers=True,
        title="Lead volume and sold deals by month"
    )
    fig4.update_layout(xaxis_title="", yaxis_title="Count")
    st.plotly_chart(fig4, use_container_width=True)

with tab4:
    st.subheader("Anonymized Dataset")
    st.dataframe(filtered.drop(columns=["sold_flag"]), use_container_width=True)

st.divider()
st.subheader("Business Takeaways")
st.markdown("""
- Facebook Marketplace generated the highest lead volume.
- Walk-in and other lower-volume sources can show stronger close rates.
- A dealership should evaluate both lead quantity and conversion quality before deciding marketing spend.
- Future improvement: add gross profit, ad cost, appointment booked, and salesperson fields to measure true ROI.
""")
