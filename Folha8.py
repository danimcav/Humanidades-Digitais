#Universidade do Minho - UMinho
#Mestrado em Humanidades Digitais
#Processamento de Linguagem Natural
#
#Prof. José João
#
#Aluna: Daniella Monteiro Cavalheiro
#Matricula: PG54506
#
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
def calcular_total_publicacoes(materias):
    return len(materias)

# 2. Extrair as listas das tags
def extrair_tags(materia):
    tags = re.findall(r'tag:{.*?}', materia)
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

# Carrega o conteúdo do arquivo para variável folha8
folha8 = le_arquivo_fonte("folha8.OUT.txt")

# Quebra por matérias
lista_materias = quebra_por_materias(folha8)

# 1. Calcular quantas publicações existem na base
total_publicacoes = calcular_total_publicacoes(lista_materias)
print(f"Total de publicações: {total_publicacoes}")

# 3. Calcular as tags que ocorrem e quanto ocorrem
contagem_tags = calcular_contagem_tags(lista_materias)

# 4. Contar o número total de '{}' no texto
numero_chaves = folha8.count('{}')
print(f"Número total de '{{}}': {numero_chaves}")

# 5. Contar o número total de ocorrências de todas as tags
total_tags = sum(contagem_tags.values())
print(f"Total de ocorrências de todas as tags: {total_tags}")


# 4. Extrair a gama de dados do texto
# Implemente a lógica para extrair a gama de dados aqui, se aplicável
