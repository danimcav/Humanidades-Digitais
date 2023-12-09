#Universidade do Minho - UMinho
#Mestrado em Humanidades Digitais
#Processamento de Linguagem Natural
#
#Prof. José João
#
#Aluna: Daniella Monteiro Cavalheiro
#Matricula: PG54506

import re

# Leitura dos dados do arquivo fonte "folha8.Out.txt"
def le_arquivo_fonte(nomearquivo):
    with open(nomearquivo, "r", encoding="utf8") as arquivo:
        conteudo = arquivo.read()
        return conteudo

# Função para quebrar por matérias
def quebra_por_materias(folha):
    materias = folha.split("<pub>")
    return materias

# 1. Calcular quantas publicações existem na base
def exercicio_01(lista_materias):
    print(f"Total de matérias: {len(lista_materias)}")

# 2. Extrair as listas das tags
def extrair_tags(materia):
    tags = re.findall(r'<(.*?)>', materia)
    return tags

# 3. Calcular as tags que ocorrem e quanto ocorrem
def calcular_contagem_tags(materias):
    contagem_tags = {}
    for materia in materias:
        tags_materia = extrair_tags(materia)
        for tag in tags_materia:
            if tag not in contagem_tags:
                contagem_tags[tag] = 1
            else:
                contagem_tags[tag] += 1
    return contagem_tags

# Resto do seu código...

# Carrega o conteúdo do arquivo para variável folha8
folha8 = le_arquivo_fonte("folha8.OUT.txt")

# Quebra por matérias
lista_materias = quebra_por_materias(folha8)

# Exercício 1
exercicio_01(lista_materias)

# Exercício 3: Calcula as contagens das tags
contagem_tags = calcular_contagem_tags(lista_materias)

# Exibe as contagens das tags
for tag, quantidade in contagem_tags.items():
    print(f"Tag: {tag} - Quantidade: {quantidade}")
