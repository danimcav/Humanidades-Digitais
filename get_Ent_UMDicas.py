import os
import spacy
from bs4 import BeautifulSoup as bs
from jjcli import *

def main():
    diretorio = r'D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\saida\PDF_to_TEXT'
    
    cl = clfilter()
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                texto = arquivo.read()
                proctexto(texto)

def proctexto(text):
    nlp = spacy.load("pt_core_news_lg")
    doc = nlp(text)
    for entity in doc.ents:
        print(entity.text, entity.label_)

if __name__ == "__main__":
    main()
