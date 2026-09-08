"""M8 — Dashboard marketing interactif (Streamlit)."""
import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.data_loader import load_customers, load_marketing, load_sales_with_context

# Palette catégorielle validée (ordre fixe, ne jamais permuter)
CATEGORICAL = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
SEQUENTIAL_BLUE = "#2a78d6"

st.set_page_config(page_title="Dashboard Marketing", layout="wide")
st.title("Dashboard Marketing — Segmentation & Performance")

customers = load_customers()
marketing = load_marketing()
sales = load_sales_with_context()

PROCESSED_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"
segments_path = PROCESSED_DIR / "segments.csv"
segments = pd.read_csv(segments_path) if segments_path.exists() else None

col1, col2, col3 = st.columns(3)
col1.metric("Clients", len(customers))
col2.metric("Dépense totale", f"{customers['Total_Spent'].sum():,.0f} $")
col3.metric("Campagnes", len(marketing))

st.divider()

# --- Segmentation client ---
st.subheader("Segmentation client")
if segments is not None:
    seg = segments.copy()
    seg["Cluster"] = seg["Cluster"].astype(str)
    fig_seg = px.scatter(
        seg, x="PCA1", y="PCA2", color="Cluster",
        hover_data=["Customer_ID", "Age", "Total_Spent", "Nb_Achats", "Categorie_Preferee"],
        color_discrete_sequence=CATEGORICAL,
        title="Clusters clients (projection PCA 2D)",
    )
    fig_seg.update_traces(marker=dict(size=14, line=dict(width=1, color="white")))
    fig_seg.update_layout(template="plotly_white", legend_title_text="Segment")
    st.plotly_chart(fig_seg, use_container_width=True)
else:
    st.info("Exécuter le notebook M3 pour générer `data/processed/segments.csv`.")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Dépense totale par client")
    spend = customers.sort_values("Total_Spent", ascending=True)
    fig_spend = px.bar(
        spend, x="Total_Spent", y="Name", orientation="h",
        color_discrete_sequence=[SEQUENTIAL_BLUE],
        labels={"Total_Spent": "Dépense totale ($)", "Name": ""},
    )
    fig_spend.update_layout(template="plotly_white", showlegend=False)
    st.plotly_chart(fig_spend, use_container_width=True)

with col_b:
    st.subheader("Ventes par canal")
    channel_counts = sales["Channel"].value_counts().reset_index()
    channel_counts.columns = ["Channel", "Nb_Ventes"]
    fig_channel = px.bar(
        channel_counts, x="Channel", y="Nb_Ventes", color="Channel",
        color_discrete_sequence=CATEGORICAL,
        labels={"Nb_Ventes": "Nombre de ventes", "Channel": "Canal"},
    )
    fig_channel.update_layout(template="plotly_white", showlegend=False)
    st.plotly_chart(fig_channel, use_container_width=True)

st.divider()

# --- Performance des campagnes ---
st.subheader("Performance des campagnes marketing")
marketing = marketing.assign(
    CTR=marketing["Clicks"] / marketing["Impressions"],
    Taux_conversion=marketing["Conversions"] / marketing["Clicks"],
    CPC=marketing["Budget"] / marketing["Clicks"],
    CPA=marketing["Budget"] / marketing["Conversions"],
)

col_c, col_d = st.columns(2)

with col_c:
    rates = marketing.melt(
        id_vars="Channel", value_vars=["CTR", "Taux_conversion"],
        var_name="Métrique", value_name="Taux",
    )
    fig_rates = px.bar(
        rates, x="Channel", y="Taux", color="Métrique", barmode="group",
        color_discrete_sequence=CATEGORICAL,
        labels={"Taux": "Taux (%)", "Channel": "Canal"},
    )
    fig_rates.update_layout(template="plotly_white", yaxis_tickformat=".0%")
    fig_rates.update_traces(hovertemplate="%{y:.1%}")
    st.plotly_chart(fig_rates, use_container_width=True)

with col_d:
    cpa_sorted = marketing.sort_values("CPA", ascending=True)
    fig_cpa = px.bar(
        cpa_sorted, x="CPA", y="Channel", orientation="h",
        color_discrete_sequence=[SEQUENTIAL_BLUE],
        labels={"CPA": "Coût par acquisition ($)", "Channel": "Canal"},
        title="CPA par canal (du plus au moins efficient)",
    )
    fig_cpa.update_layout(template="plotly_white", showlegend=False)
    st.plotly_chart(fig_cpa, use_container_width=True)

st.dataframe(marketing, use_container_width=True)

st.divider()
st.subheader("Données détaillées")
with st.expander("Clients"):
    st.dataframe(customers, use_container_width=True)
with st.expander("Ventes (avec contexte client/produit)"):
    st.dataframe(sales, use_container_width=True)
