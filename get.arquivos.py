from jjcli import *
from bs4 import BeautifulSoup as bs


ats= glob ("Student_4/Article.aspx*")
print (ats)

def proc_article(html):        
    print (len(html)) #conta o número de caracteres de cada arquivo
    a= bs(html) #cria uma árvore documental
    art= a.find("div", id="artigo") #procura no html
    print("=========\n", art.get_text()) #get_text - Retira apenas o texto mesmo, sem html

for file in ats:
    with open(file) as f: 
        hmtl= f.read()
    proc_article(html)


