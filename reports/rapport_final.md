# Rapport final — Analyse & Optimisation Marketing basée sur la Segmentation Client

## 1. Contexte et objectif

Ce projet exploite des données clients, produits, ventes et campagnes marketing d'un
retailer mode multicanal (vente en ligne + magasin) afin de : segmenter les clients,
analyser leurs comportements d'achat, évaluer les performances des campagnes marketing et
proposer une stratégie marketing digitale personnalisée assistée par l'IA.

> **Avertissement méthodologique** : l'ensemble du pipeline a été développé et validé de
> bout en bout sur un jeu de données d'échantillon (5 clients, 5 produits, 5 ventes, 5
> campagnes). Les résultats numériques ci-dessous illustrent la méthode et sont directement
> reproductibles sur un volume de données réel plus large — mais ne doivent pas être
> interprétés comme statistiquement significatifs en l'état.

## 2. Enjeux stratégiques (M1)

Voir [notebooks/M1_enjeux_strategiques.md](../notebooks/M1_enjeux_strategiques.md) pour le
détail SWOT / 5P / parcours client. Synthèse : la personnalisation marketing pilotée par la
donnée est freinée par le manque de segmentation existante, mais permise par la disponibilité
des données de vente, produit et campagne déjà collectées.

## 3. Exploration des données (M2)

Nettoyage et statistiques descriptives sur `customers_data`, `products_data`, `sales_data`.
**Observation notable** : un client (2005 — Eva) ne possède aucune transaction dans
`sales_data`, ce qui l'exclut des analyses de segmentation basées sur le comportement
d'achat (M3). Sur un jeu de données réel, ce type de client "inactif" mériterait un
traitement spécifique (segment "jamais converti").

## 4. Segmentation client (M3)

Segmentation par K-means (et clustering hiérarchique en comparaison) sur l'âge, la dépense
totale et la fréquence d'achat, réduite à 2 dimensions par PCA pour visualisation
(`reports/M3_segmentation_pca.png`). 3 clusters obtenus sur les 4 clients ayant un
historique d'achat.

## 5. Profils de segments — personas (M4)

| Segment | Profil | Comportement | Recommandation |
|---|---|---|---|
| 0 | ~30 ans, dépense élevée (~675$), achat ponctuel | Achat premium occasionnel | Cibler avec offres premium / cross-sell |
| 1 | ~22 ans, dépense faible (~300$) | Entrant, petit budget | Programme de fidélisation progressif |
| 2 | ~28 ans, dépense moyenne (~500$), achats répétés | Client engagé/fidèle | Prioritaire pour la rétention |

## 6. Performance des campagnes marketing (M5)

| Canal | CTR | Taux de conversion | CPC | CPA |
|---|---|---|---|---|
| Online | 4.0% | 7.5% | 0.50 $ | 6.67 $ |
| In-Store | 1.7% | 20.0% | 3.00 $ | 15.00 $ |
| Social | 3.75% | 13.3% | 1.33 $ | 10.00 $ |
| Email | 5.0% | 5.0% | 0.50 $ | 10.00 $ |
| TV | 5.0% | 8.3% | 1.00 $ | 12.00 $ |

**Canal le plus efficient en coût d'acquisition** : Online (CPA 6.67$). **Canal le plus
qualifié en conversion** : In-Store (20%).

## 7. Modèles prédictifs — churn et CLV (M6)

Pipeline RFM (Récence / Fréquence / Montant) → régression linéaire pour la CLV, Random
Forest pour un score de risque de churn. Fonctionnel de bout en bout ; à réentraîner avec
validation croisée sur un volume de données suffisant pour un usage en production.

## 8. Stratégie marketing digitale recommandée (M7)

Voir [notebooks/M7_strategie_marketing.md](../notebooks/M7_strategie_marketing.md) pour le
détail complet. Synthèse :

- **Segment 0 (premium occasionnel)** → canal In-Store, budget élevé, faible volume
- **Segment 1 (entrant)** → canal Email pour l'activation, budget modéré, volume élevé
- **Segment 2 (engagé)** → canal Online, budget prioritaire (meilleur ROI), programme fidélité

## 9. Dashboard interactif (M8)

Dashboard Streamlit (`dashboard/app.py`) consolidant clients, ventes et KPIs de campagnes
en temps réel. Testé et fonctionnel — lancement via `streamlit run dashboard/app.py`.

## 10. Conclusion et prochaines étapes

Le pipeline complet (M1→M8) est opérationnel et reproductible. Pour une mise en production :

1. Remplacer l'échantillon de démonstration par les données réelles de l'entreprise.
2. Revalider le nombre optimal de clusters (méthode du coude / silhouette) sur volume réel.
3. Réentraîner les modèles de churn/CLV avec un vrai split train/test et validation croisée.
4. Déployer le dashboard sur un serveur accessible aux équipes marketing.
5. Mettre en place un cycle de réentraînement périodique des modèles.
