from jjcli import *
from bs4 import BeautifulSoup as bs
import re

ats= glob("nos_1146_1149/Article.aspx*")
print (ats)

fo = open("saida.txt", "w", encoding = "utf-8")
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
    date = a.find("span", id="ctl00_ContentPlaceHolder1_LabelInfo").get_text() #extrai a data usando uma expressão regular e adiciona-a ao início do cabeçalho.
    date = re.search(r"\d{2}-\d{2}-\d{4}", date).group()
    cabecalho = f"Date:{date}\n" + cabecalho
    print ("=========\n", cabecalho, art.get_text(), file)

for file in ats:
    with open(file, encoding="utf-8") as f:
        html= f.read() 
    proc_article (html)

