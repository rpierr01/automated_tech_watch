# 📡 TechWatch — Veille Informationnelle Technologique Automatisée

> Application de veille automatisée propulsée par un LLM capable de parcourir internet pour sélectionner et résumer les articles les plus pertinents selon un profil Data Science / IA.

---

## 🎯 Objectif

TechWatch est un outil personnel de veille informationnelle qui tourne de manière automatisée. Chaque jour, il parcourt les dernières publications technologiques sur le web, sélectionne les **5 articles les plus pertinents** pour le profil de l'utilisateur, et produit un **résumé général** de l'actualité du moment.

L'outil est pensé comme un **digest quotidien intelligent**, sans intervention manuelle.

---

## ✨ Fonctionnalités

- 🔍 **Parcours automatique du web** — le LLM explore les dernières publications via des flux RSS, APIs et recherche web en temps réel
- 🏆 **Sélection des 5 meilleurs articles** — filtrés par pertinence selon un profil prédéfini (Data Science, IA, Deep Learning, Python…)
- 📝 **Résumé par article** — chaque article sélectionné est résumé en 3 à 5 lignes
- 🌐 **Résumé général** — synthèse globale de l'actualité tech du jour en quelques phrases
- ⏰ **Automatisation complète** — exécution planifiée sans intervention de l'utilisateur
- 📬 **Diffusion du digest** — envoi par e-mail et/ou affichage dans un dashboard

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    SOURCES DE DONNÉES                    │
│  Flux RSS · APIs · Recherche web temps réel             │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  COLLECTE (Python)                       │
│  feedparser · requests · BeautifulSoup                  │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│            FILTRAGE & SCORING PAR PERTINENCE            │
│  Correspondance profil · Déduplication · Classement     │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│          TRAITEMENT LLM (Mistral local)                  │
│  Résumé par article · Résumé général · Scoring final    │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                     DIFFUSION                           │
│  E-mail (SMTP) · Dashboard Streamlit · SQLite (logs)   │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Stack Technique

| Composant | Technologie |
|---|---|
| Langage principal | Python 3.11+ |
| Collecte RSS | `feedparser` |
| Scraping web | `requests`, `BeautifulSoup4` |
| LLM | Modèle Mistral local (`Mistral Small 4`) |
| Recherche web temps réel | Claude API + web search tool |
| Planification | `schedule` / `cron` |
| Envoi e-mail | `smtplib` |
| Dashboard | `Streamlit` |
| Stockage | `SQLite` |
| Versionnement | Git + GitHub |

---

## 📦 Structure du Projet

```
techwatch/
│
├── main.py                  # Point d'entrée principal
├── scheduler.py             # Planification de l'exécution
│
├── collectors/
│   ├── rss_collector.py     # Collecte via flux RSS
│   └── web_collector.py     # Recherche web temps réel
│
├── processing/
│   ├── filter.py            # Filtrage et scoring par pertinence
│   └── llm_processor.py    # Résumé et analyse via LLM
│
├── output/
│   ├── mailer.py            # Envoi du digest par e-mail
│   └── dashboard.py         # Interface Streamlit
│
├── storage/
│   └── database.py          # Gestion SQLite (logs, historique)
│
├── config/
│   ├── profile.yaml         # Profil utilisateur & mots-clés
│   └── sources.yaml         # Liste des sources RSS et domaines
│
├── .env                     # Variables d'environnement (clés API)
├── requirements.txt
└── README.md
```

---

## 📋 Format du Digest Quotidien

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📡 TechWatch — Digest du 21 mars 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 RÉSUMÉ GÉNÉRAL
Cette semaine en Data Science & IA : [synthèse en 3-4 phrases des tendances du jour]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 TOP 5 DES ARTICLES DU JOUR

① [Titre de l'article] — Source · Temps de lecture estimé
   Résumé en 3 à 5 lignes...
   🔗 https://...

② ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🚀 Installation & Lancement

```bash
# Cloner le dépôt
git clone https://github.com/Remi-Pierron/techwatch.git
cd techwatch

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# → Renseigner SMTP_PASSWORD, etc.

# Lancer manuellement
python main.py

# Lancer le dashboard
streamlit run output/dashboard.py
```

---


## 👨‍💻 Auteur

**Rémi Pierron** — Étudiant en BUT Science des Données (VCOD), IUT de Poitiers – site de Niort  
🔗 [LinkedIn](https://www.linkedin.com/in/rémi-pierron-54b8b1290/) · [Portfolio](https://remi-pierron.github.io/portfolio)

---

## 📄 Licence

Projet personnel — usage libre à des fins éducatives.