# M1 — Compréhension des enjeux stratégiques

**Objectif pédagogique** : identifier les enjeux de la personnalisation marketing (module théorique, sans données).

## Contexte métier

L'entreprise étudiée est un **retailer mode/textile multicanal** (vente en ligne et en
magasin physique — canaux `Online` / `In-Store` observés dans `sales_data`), avec un
catalogue de vêtements couvrant plusieurs marques et catégories (`products_data`). Elle
mène des campagnes marketing digitales mesurables (impressions, clics, conversions —
`marketing_data`) et dispose d'un historique d'achats par client (`sales_data` +
`customers_data`).

**Problématique** : comment exploiter les données existantes (clients, produits, ventes,
campagnes) pour passer d'un marketing de masse à un marketing **personnalisé et piloté par
l'IA**, afin d'améliorer l'efficacité des campagnes et la fidélisation client ?

## SWOT — Personnalisation marketing par la donnée

| | **Forces** | **Faiblesses** |
|---|---|---|
| **Interne** | Données clients/ventes/campagnes déjà collectées et structurées ; présence sur deux canaux complémentaires (Online + In-Store) ; catalogue multi-marques permettant du cross-sell | Volume de données actuellement limité (échantillon de démonstration) ; pas encore de modèle de segmentation ni de scoring client en place ; silos possibles entre données de vente et données marketing |

| | **Opportunités** | **Menaces** |
|---|---|---|
| **Externe** | Maturité des outils IA/ML accessibles (scikit-learn, XGBoost) pour industrialiser la segmentation et la prédiction ; attentes croissantes des consommateurs pour une expérience personnalisée ; dashboards temps réel (Streamlit/Power BI) facilitant le pilotage | Sensibilité accrue à la protection des données personnelles (RGPD) ; concurrence des acteurs déjà data-driven ; sur-personnalisation perçue comme intrusive si mal maîtrisée |

## 5P du marketing digital appliqués au projet

- **Product** — adapter les recommandations produit par segment (ex. mise en avant de
  catégories différentes selon le profil client identifié en M3/M4).
- **Price** — moduler les offres/promotions selon la valeur client prédite (CLV, module M6).
- **Place** — arbitrer les canaux (Online vs In-Store) selon les préférences observées par
  segment, à partir des données `sales_data.Channel`.
- **Promotion** — cibler les campagnes marketing (M5/M7) sur les canaux et messages les
  plus performants par segment, plutôt qu'une communication indifférenciée.
- **People** — utiliser les personas issus du profilage (M4) pour aligner discours
  commercial, service client et contenu sur les attentes réelles de chaque groupe.

## Parcours client (customer journey) et leviers IA associés

1. **Découverte** — le client découvre la marque via une campagne (mesurée en M5 :
   impressions, CTR).
2. **Considération** — navigation/comparaison produits ; potentiel de recommandation
   personnalisée basée sur le segment (M3/M4).
3. **Achat** — conversion sur un canal (Online/In-Store) ; les KPIs de conversion et de
   coût d'acquisition sont suivis en M5 (CPA, taux de conversion).
4. **Fidélisation** — suivi de la récurrence d'achat et de la valeur client dans le temps ;
   modélisée en M6 (churn / CLV) pour anticiper le désengagement.
5. **Recommandation** — un client fidèle à forte valeur (segment premium identifié en M4)
   devient un levier de bouche-à-oreille ; ciblage spécifique possible en M7 (programme
   ambassadeur, offres de parrainage).

## Enjeux stratégiques retenus pour la suite du projet

1. **Connaître** le client au-delà de la moyenne globale → nécessité de la segmentation (M3).
2. **Prioriser** l'effort marketing et budgétaire selon la valeur et le risque de churn de
   chaque segment (M6).
3. **Mesurer** objectivement la performance des campagnes par canal et par segment (M5),
   plutôt que sur des indicateurs agrégés peu actionnables.
4. **Industrialiser** le pilotage via un dashboard unique consolidant segments et KPIs (M8),
   pour une prise de décision continue plutôt que ponctuelle.
