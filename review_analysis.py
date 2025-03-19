from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()


def ler_reviews():
    # Leitura do arquivo 'reviews.txt' que contém todos os inputs
    # OBS - O azure só aceita 10 leituras por vez
    with open('inputs/reviews.txt', 'r', encoding='utf-8') as file:
        reviews = file.readlines()
    reviews = [review.strip() for review in reviews]
    return reviews

# Analisando os reviews fornecidos
def analisar_reviews():
    reviews = ler_reviews()

    result = text_analytics_client.analyze_sentiment(reviews)

    # Imprimindo a análise de todos os reviews
    # Salvando o resultado e o texto analisado em uma tupla
    for i, (doc, review) in enumerate(zip(result, reviews)):
        print(f"Review {i+1}:")
        print(f"Texto analisado: {review}")
        print(f"Sentimento: {doc.sentiment}")
        print(f"Pontuação positiva: {doc.confidence_scores.positive}")
        print(f"Pontuação negativa: {doc.confidence_scores.negative}")
        print(f"Pontuação neutra: {doc.confidence_scores.neutral}")
        print("-" * 25)

# Configurando as variáveis de acesso ao azure
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("AZURE_LANGUAGE_KEY")

# Especificando que o uso do serviço será uma análise de texto
text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

if __name__ == "__main__":
    analisar_reviews()