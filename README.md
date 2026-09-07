# Analyse & Optimisation Marketing basée sur la Segmentation Client

Projet pédagogique exploitant des données clients, produits, marketing et ventes pour
segmenter les clients, analyser les comportements d'achat, évaluer les performances des
campagnes marketing et proposer une stratégie marketing digitale personnalisée assistée
par l'intelligence artificielle.

Le cahier des charges complet (`Documentation/Projet-pédagogique-SMD-IA-et-PRSD.pdf`) est
disponible en local mais n'est pas versionné dans ce dépôt.

## Structure du projet

| Module | Thématique | Notebook / Livrable |
|--------|-----------|----------------------|
| M1 | Compréhension des enjeux stratégiques (SWOT, 5P, parcours client) | `notebooks/M1_enjeux_strategiques.md` |
| M2 | Exploration des données (nettoyage, visualisation) | `notebooks/M2_exploration_donnees.ipynb` |
| M3 | Segmentation client (K-means, PCA, t-SNE, clustering hiérarchique) | `notebooks/M3_segmentation_client.ipynb` |
| M4 | Profilage des segments (personas) | `notebooks/M4_profilage_segments.ipynb` |
| M5 | Analyse des performances des campagnes marketing | `notebooks/M5_analyse_campagnes.ipynb` |
| M6 | Prédiction de churn / CLV | `notebooks/M6_prediction_churn_clv.ipynb` |
| M7 | Élaboration d'une stratégie marketing digitale | `notebooks/M7_strategie_marketing.md` |
| M8 | Dashboard marketing interactif | `dashboard/app.py` |
| M9 | Présentation finale et livrables | `reports/` |

## Données

Fichiers sources dans `data/raw/` :

- `customers_data.csv` — identité, âge, genre, localisation, date d'inscription, dépense totale
- `products_data.csv` — catalogue produit (catégorie, prix, marque)
- `sales_data.csv` — transactions (jointure customer/produit, canal)
- `marketing_data.csv` — campagnes (impressions, clics, conversions, budget)

> ⚠️ Les fichiers fournis ne contiennent que 5 lignes chacun (échantillon de démonstration).
> Cela suffit pour dérouler le pipeline de bout en bout, mais les résultats de clustering
> (M3) et de modélisation prédictive (M6) ne seront pas statistiquement significatifs tant
> que le volume de données réel n'est pas fourni.

## Stack technique

- Python 3.11+
- pandas, numpy — manipulation de données
- matplotlib, seaborn — visualisation
- scikit-learn — clustering (K-means, PCA, t-SNE), modèles prédictifs (Random Forest, Logistic Regression)
- xgboost — prédiction churn/CLV
- streamlit — dashboard interactif (M8)

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer le dashboard (M8)

```bash
streamlit run dashboard/app.py
```

## Livrables attendus

- Segmentation client et profils détaillés
- Analyses des campagnes et recommandations
- Modèles IA de prédiction (churn, valeur client)
- Dashboard interactif
- Rapport final (Word ou PDF)
- Présentation orale (PowerPoint)
