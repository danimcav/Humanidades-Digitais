texto = """Era um vez, um gato maltês,
que tocava piano e falava francês,
queres que te conte outa vez?"""

# escreva uma função que conte as palavras com comprimento 3
# escreva a lista das palavras ordenadamente
# qual a palavra mais comprida
# calcular o número de ocorrências de cada palavra no texto

def contar_palavras_com_comprimento(texto, comprimento):
    palavras = texto.split()
    palavras_com_comprimento = [palavra for palavra in palavras if len(palavra) == comprimento]
    return palavras_com_comprimento

def lista_palavras_ordenadas(texto):
    palavras = texto.split()
    return sorted(palavras)

def palavra_mais_comprida(texto):
    palavras = texto.split()
    return max(palavras, key=len)

def contar_ocorrencias_palavras(texto):
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

texto = """Era um vez, um gato maltês,
que tocava piano e falava francês,
queres que te conte outa vez? """

comprimento_alvo = 3

palavras_com_comprimento = contar_palavras_com_comprimento(texto, comprimento_alvo)
palavras_ordenadas = lista_palavras_ordenadas(texto)
palavra_mais_longa = palavra_mais_comprida(texto)
ocorrencias_palavras = contar_ocorrencias_palavras(texto)

print(f"Palavras com comprimento {comprimento_alvo}: {palavras_com_comprimento}")
print(f"Lista de palavras ordenadas: {palavras_ordenadas}")
print(f"Palavra mais comprida: {palavra_mais_longa}")
print(f"Contagem de ocorrências de cada palavra:\n{ocorrencias_palavras}")
