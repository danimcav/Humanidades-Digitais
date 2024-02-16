from jjcli import *
from bs4 import BeautifulSoup as bs


ats= glob("nos_1146_1149/Article.aspx*")
print (ats)


fo = open("saida.txt", "w", encoding = "utf-8")
def proc_article(html):
    #print (len(html)) #está a contar os carateres de cada artigo
    a=bs(html) # cria uma árvore documental
    cabecalho = ""
    for meta in a.find_all("meta"):
        p = meta.get("property")
        if p is None:
            continue
        p = p.replace("og:", "")
        cabecalho+= f"{p}:{meta.get('content')}\n"
        print(p, ":" , meta.get("content"))
    art= a.find("div", id="artigo") #procura no html
    print ("=========\n", cabecalho, art.get_text(), file)

for file in ats:
    with open(file, encoding="utf-8") as f:
        html= f.read() 
    proc_article (html)




"""<meta property='og:title' content='"Recebo e aprendo muito com todos e isso satisfaz-me!"'/><meta property='og:url' content='http://www.nos.uminho.pt/Article.aspx?id=3669'/><meta property='og:image' content='http://www.nos.uminho.pt/Images/destaques/20230928103003_IMG5208.jpg'/><meta property='og:site_name' content='Jornal Online UMINHO "Recebo e aprendo muito com todos e isso satisfaz-me!"'/><meta property='og:description' content='Conhecido como Z&eacute; Manuel, o vimaranense de 58 anos come&ccedil;ou a trabalhar no Departamento de Engenharia T&ecirc;xtil em 1992, ent&atilde;o no Pal&aacute;cio Vila Flor. Atualmente presta apoio t&eacute;cnico aos cursos de Teatro e Artes Visuais, no Teatro Jord&atilde;o.'/><meta property='og:type' content='blog'/>

<div id="artigo">
                    <div class="title">
                        
                        <div class="voltar">

<h1>
                        <span id="ctl00_ContentPlaceHolder1_LabelTitle">"Recebo e aprendo muito com todos e isso satisfaz-me!"</span></h1>
                    <span class="creditos">
                        <span id="ctl00_ContentPlaceHolder1_LabelInfo">29-09-2023 | Paula Mesquita | Fotos: Nuno Gonçalves</span>
                    </span>

"""


