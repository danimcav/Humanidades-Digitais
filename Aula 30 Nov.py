import json

# Função para imprimir nome e idade quando a profissão for pedreiro
def imprimir_nome_idade_pedreiros(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

        # Iterando pelas publicações e verificando se a profissão é pedreiro
        for publicacao in dados:
            if 'nome' in publicacao and 'idade' in publicacao and 'profissao' in publicacao:
                if publicacao['profissao'] == 'pedreiro':  # Verifica se a profissão é pedreiro
                    print(f"Nome: {publicacao['nome']}, Idade: {publicacao['idade']}")

# Definindo o caminho do arquivo JSON
caminho_arquivo = r'C:\Users\Lenovo\Aulas JJ Python\ex1.json.json'

# Chamada da função para imprimir nome e idade apenas quando a profissão for pedreiro
imprimir_nome_idade_pedreiros(caminho_arquivo)
import json

def calcular_total_publicacoes(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        total_publicacoes = len(dados)
        return total_publicacoes

caminho_arquivo = r'D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\ex1.json.json'
total = calcular_total_publicacoes(caminho_arquivo)
print(f"Total de publicações: {total}")
