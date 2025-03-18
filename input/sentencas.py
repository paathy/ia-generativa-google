from google.cloud import language_v1

def analyze_sentiment(text):
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment

    return {
        "frase": text,
        "sentimento": sentiment.score,
        "intensidade": sentiment.magnitude
    }

sentences = [
    "Fiquei encantada com o atendimento da Andreza, ela captou exatamente o que eu queria e realçou minha beleza de forma impecável!",
    "Infelizmente, a maquiagem feita pela Geovana não durou muito tempo e começou a craquelar após algumas horas.",
    "O estúdio tem um ambiente maravilhoso, e a Andreza fez um trabalho incrível, minha pele ficou perfeita!",
    "A experiência foi frustrante, pois a Geovana atrasou muito e parecia estar com pressa ao me maquiar.",
    "Andreza tem mãos de fada, fez um esfumado impecável e a base ficou leve e natural!",
    "A Geovana é simpática, mas senti que a maquiagem ficou diferente do que eu pedi.",
    "Melhor estúdio de maquiagem que já fui! As meninas são super atenciosas e os produtos são de alta qualidade.",
    "Minha maquiagem derreteu antes do evento começar, esperava mais do serviço oferecido.",
    "A Geovana arrasou no delineado, ficou super preciso e combinou perfeitamente com meu look!",
    "O atendimento foi bom, mas achei os preços um pouco altos pelo resultado final."
]

sentiment_results = []

for sentence in sentences:
    sentiment_results.append(analyze_sentiment(sentence))

with open("sentiment_results.md", "w", encoding="utf-8") as file:
    file.write("# Resultados da Análise de Sentimento\n\n")
    for result in sentiment_results:
        file.write(f"## Frase: {result['frase']}\n")
        file.write(f"- **Sentimento**: {result['sentimento']}\n")
        file.write(f"- **Intensidade**: {result['intensidade']}\n")
        file.write("\n---\n") 
print("Resultados exportados para sentiment_results.md")