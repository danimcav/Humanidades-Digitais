import requests
from bs4 import BeautifulSoup
import os

def baixar_entrevistas(inicio, fim):
    for n in range(inicio, fim + 1):
        url = f"http://www.nos.uminho.pt/History.aspx?id={n}"
        print(f"Verificando a URL: {url}")

        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica se houve algum erro na requisição

            soup = BeautifulSoup(response.text, 'html.parser')

            # Obtém o conteúdo do artigo
            conteudo_artigo = soup.get_text()

            # Verifica se o conteúdo contém pontos de interrogação
            if '?' in conteudo_artigo:
                print(f"Pontos de interrogação encontrados no artigo {n}. Baixando...")

                # Salva o artigo no diretório 'entrevistas'
                destino = f"entrevistas/artigo_{n}.txt"
                with open(destino, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(conteudo_artigo)

                print(f"Artigo {n} salvo com sucesso.")
            else:
                print("Nenhum ponto de interrogação encontrado no artigo.")

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição para a URL {url}: {e}")

# Criar diretório 'entrevistas' se não existir
if not os.path.exists('entrevistas'):
    os.makedirs('entrevistas')

# Definir o intervalo de IDs das entrevistas que deseja baixar
inicio_id = 1067
fim_id = 1150

# Chamar a função para baixar os arquivos
baixar_entrevistas(inicio_id, fim_id)
