"""Chargement et jointure des jeux de données du projet."""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def load_customers() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "customers_data.csv", parse_dates=["Join_Date"])


def load_products() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "products_data.csv")


def load_sales() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "sales_data.csv", parse_dates=["Date"])


def load_marketing() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "marketing_data.csv", parse_dates=["Start_Date", "End_Date"])


def load_sales_with_context() -> pd.DataFrame:
    """Jointure ventes + clients + produits (utilisée en M3)."""
    sales = load_sales()
    customers = load_customers()
    products = load_products()
    return sales.merge(customers, on="Customer_ID").merge(products, on="Product_ID")
