#Universidade do Minho - UMinho
#Mestrado em Humanidades Digitais
#Processamento de Linguagem Natural
#
#Prof. José João
#
#Aluna: Daniella Monteiro Cavalheiro
#Matricula: PG54506
#
import spacy
from collections import Counter
import re
import matplotlib.pyplot as plt

# Função para realizar NER apenas em entidades entre chaves {}
def realizar_ner_entre_chaves(texto):
    entidades_chaves = re.findall(r'{(.*?)}', texto)
    return entidades_chaves

# Função para extrair POS tags das palavras nas tags {}
def extrair_pos_tags(entidades):
    nlp = spacy.load('pt_core_news_sm')
    pos_tags = []
    for entidade in entidades:
        doc = nlp(entidade)
        for token in doc:
            if not token.is_punct and not token.is_space:
                pos_tags.append(token.pos_)
    return pos_tags

# Leitura dos dados do arquivo fonte "folha8.Out.txt"
def le_arquivo_fonte(nomearquivo):
    with open(nomearquivo, "r", encoding="utf8") as arquivo:
        conteudo = arquivo.read()
        return conteudo

# Carregar o conteúdo do arquivo para variável folha8
folha8 = le_arquivo_fonte("folha8.OUT.txt")

# Realizar NER apenas em entidades entre chaves no texto
entidades_chaves = realizar_ner_entre_chaves(folha8)

# Extrair POS tags das palavras nas tags {}
pos_tags_entidades = extrair_pos_tags(entidades_chaves)

# Contar frequência das classes gramaticais
contagem_pos_tags = Counter(pos_tags_entidades)

# Plotar gráfico de barras com a frequência das classes gramaticais
plt.figure(figsize=(10, 6))
plt.bar(contagem_pos_tags.keys(), contagem_pos_tags.values())
plt.title('Frequência de Classes Gramaticais das Palavras nas Tags')
plt.xlabel('Classes Gramaticais')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

