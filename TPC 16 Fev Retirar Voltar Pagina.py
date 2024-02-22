from jjcli import *
from bs4 import BeautifulSoup as bs
import re

ats= glob("nos_1146_1149/Article.aspx*")
print (ats)

fo = open("saida.txt", "w", encoding = "utf-8")

def limpezas(text):
    # Adicione aqui as expressões que deseja remover
    lixo = ["voltar à página anterior"]
    for l in lixo:
        text = text.replace(l, "")
    return text

def proc_article(html):
    a=bs(html) 
    cabecalho = ""
    for meta in a.find_all("meta"):
        p = meta.get("property")
        if p is None:
            continue
        p = p.replace("og:", "")
        cabecalho+= f"{p}:{meta.get('content')}\n"
        print(p, ":" , meta.get("content"))
    art= a.find("div", id="artigo") 
    date = a.find("span", id="ctl00_ContentPlaceHolder1_LabelInfo").get_text()
    date = re.search(r"\d{2}-\d{2}-\d{4}", date).group()
    cabecalho = f"Date:{date}\n" + cabecalho
    art_text = limpezas(art.get_text())
    print ("=========\n", cabecalho, "---", art_text, file)

for file in ats:
    with open(file, encoding="utf-8") as f:
        html= f.read() 
    proc_article (html)
