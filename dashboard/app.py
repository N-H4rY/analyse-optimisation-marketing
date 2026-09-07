"""M8 — Dashboard marketing interactif (Streamlit)."""
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.data_loader import load_customers, load_marketing, load_sales_with_context

st.set_page_config(page_title="Dashboard Marketing", layout="wide")
st.title("Dashboard Marketing — Segmentation & Performance")

customers = load_customers()
marketing = load_marketing()
sales = load_sales_with_context()

col1, col2, col3 = st.columns(3)
col1.metric("Clients", len(customers))
col2.metric("Dépense totale", f"{customers['Total_Spent'].sum():,.0f} $")
col3.metric("Campagnes", len(marketing))

st.subheader("Clients")
st.dataframe(customers)

st.subheader("Ventes (avec contexte client/produit)")
st.dataframe(sales)

st.subheader("Performance des campagnes")
marketing = marketing.assign(
    CTR=marketing["Clicks"] / marketing["Impressions"],
    Taux_conversion=marketing["Conversions"] / marketing["Clicks"],
    CPC=marketing["Budget"] / marketing["Clicks"],
    CPA=marketing["Budget"] / marketing["Conversions"],
)
st.dataframe(marketing)
st.bar_chart(marketing.set_index("Campaign_ID")[["CTR", "Taux_conversion"]])
