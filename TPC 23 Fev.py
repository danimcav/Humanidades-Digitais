# Importa as bibliotecas necessárias
from jjcli import * 
from bs4 import BeautifulSoup as bs
import re

# O caminho para o arquivo que você deseja processar
file_path = "www.nos.uminho.pt/Article.aspx?id=2286"

# Abra o arquivo e leia o conteúdo
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Agora você pode processar o conteúdo HTML como antes
a = bs(html_content, features="html.parser") # Cria uma árvore de análise do HTML
dt = ""
for span in a.find_all("span", id="ctl00_ContentPlaceHolder1_LabelInfo"): # Itera sobre todas as tags "span" com o id especificado
        data = span.get_text(strip=True)   # Obtém o texto dentro da tag <span>
        if not data:  
            continue
        dt += f"{data}\n"  # Adiciona a data à variável dt
print("===========\n", dt, a.get_text(), file=datas_ext)

def proc_article(html): # Função para processar o artigo
    a = bs(html, features="html.parser")  
    cabecalho = "" 
    for meta in a.find_all("meta"):
        p = meta.get("property") 
        if p is None:
            continue
        p = p.replace("og:", "") 
        cabecalho += f"{p}: {meta.get('content')}\n" 
        divisao = "==================="
    art = a.find("div", id="artigo")
    corpo = proc_art_contents(art)
    print("==========\n", cabecalho, divisao, corpo, file = fo)

datas_ext = open("datas.txt", "w", encoding="UTF-8")

def proc_art_contents(art):
    for tag in art.find_all("div", class_="voltar"): tag.extract()
    for tag in art.find_all("div", id="slidesjs-log"): tag.decompose()
    for tag in art.find_all("ul", class_="socialcount"): tag.decompose()
    for tag in art.find_all("div", id="slides"):
        slides = tag.extract()
    #FIXME processar slides 
    for tag in art.find_all("table"):
        tag.insert(0, "\n ## TABELA")   
    for tag in art.find_all("strong"):  # Adicionado este loop para substituir <strong> por **
        tag.replace_with(f"**{tag.get_text()}**") # Adicionado este loop para substituir <strong> por **
    finalt = art.get_text()
    return finalt

for file in ats: #Itera sobre a lista de arquivos, processa a data e imprime os resultados
    with open (file, encoding="utf-8") as f:
        html = f.read()
    proc_data(html)

for file in ats: #Itera sobre a lista de arquivos, processa o artigo e imprime os resultados
    with open (file, encoding="utf-8") as f:
        html = f.read()
    proc_article(html)
