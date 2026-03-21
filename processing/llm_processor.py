"""
processing/llm_processor.py
Utilise l'API Gemini avec Google Search pour résumer les articles
et produire un résumé général de l'actualité tech.
"""

import os
import yaml
from datetime import datetime
from mistralai.client import Mistral


def load_profile(config_path="config/profile.yaml"):
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["profile"]


def get_client():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("❌ MISTRAL_API_KEY manquante. Vérifie ton fichier .env")

    # Initialize the client with the API key
    client = Mistral(api_key=api_key)

    # Return the client instance instead of a model wrapper
    return client


def summarize_article(client, article):
    """
    Demande au LLM de résumer un article en 3-5 lignes
    en utilisant Google Search pour accéder au contenu réel.
    """
    prompt = f"""Tu es un assistant de veille technologique pour un étudiant en Data Science.

Voici un article à résumer :
- Titre : {article['title']}
- Source : {article['source']}
- URL : {article['url']}
- Extrait disponible : {article.get('summary', "Pas d'extrait disponible")}

Utilise ta capacité de recherche web pour accéder au contenu complet de cet article si possible.

Produis un résumé en français en 3 à 5 phrases maximum. Sois concis, informatif et mets en avant :
1. Le sujet principal
2. Les résultats ou conclusions clés
3. La pertinence pour un profil Data Science / IA

Ne commence pas par "Cet article" ou "L'article". Va droit au but."""

    try:
        response = client.chat.complete(
            model="mistral-small-2603",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"    ⚠️  Erreur LLM pour '{article['title']}' : {e}")
        return article.get("summary", "Résumé non disponible.")


def generate_general_summary(client, articles):
    """
    Génère un résumé global de l'actualité tech du jour
    à partir des 5 articles sélectionnés.
    """
    articles_text = "\n".join([
        f"- [{art['source']}] {art['title']}" for art in articles
    ])

    prompt = f"""Tu es un assistant de veille technologique pour un étudiant en Data Science & IA.

Voici les 5 articles tech les plus importants du jour :
{articles_text}

En te basant sur ces articles et sur ta connaissance de l'actualité récente en Data Science et IA,
rédige un résumé général de l'actualité tech du jour en 4 à 6 phrases en français.

Ce résumé doit :
- Identifier les grandes tendances du moment
- Être rédigé de façon synthétique et engageante
- Être utile pour un étudiant en Data Science qui veut rester informé

Commence directement par le résumé, sans titre ni introduction."""

    try:
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"    ⚠️  Erreur LLM résumé général : {e}")
        return "Résumé général non disponible."


def process_articles(articles):
    """
    Pipeline complet : résume chaque article + génère le résumé global.
    Retourne le digest complet sous forme de dict.
    """
    profile = load_profile()
    client = get_client()

    print(f"  → Traitement LLM de {len(articles)} articles...")

    # Résumé de chaque article
    for i, article in enumerate(articles, 1):
        print(f"    [{i}/{len(articles)}] {article['title'][:60]}...")
        article["llm_summary"] = summarize_article(client, article)

    # Résumé général
    print("  → Génération du résumé général...")
    general_summary = generate_general_summary(client, articles)

    digest = {
        "date": datetime.now().strftime("%d %B %Y"),
        "generated_at": datetime.now().isoformat(),
        "general_summary": general_summary,
        "articles": articles,
        "profile_name": profile.get("name", "Utilisateur"),
    }

    print("  ✅ Traitement LLM terminé")
    return digest
