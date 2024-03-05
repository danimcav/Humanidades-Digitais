import os
from PyPDF2 import PdfReader

# Especifica o diretório onde os PDFs serão salvos
diretorio = "D:/Users/lfher/Dani/UMinho/Processamento de Linguagem  Prof João/saida.txt"

# Cria o diretório se ele não existir
os.makedirs(diretorio, exist_ok=True)

# Baixa os PDFs
for n in range(1, 20):  # Ajuste o intervalo conforme necessário
    comando = f'wget --no-check-certificate -P "{diretorio}" -nd "https://natura.di.uminho.pt/~jj/umdicas/UMdicas-{n}.pdf"'
    os.system(comando)

# Lista todos os PDFs baixados
pdf_files = [f for f in os.listdir(diretorio) if f.endswith('.pdf')]

# Extrair o texto de cada PDF
for pdf_file in pdf_files:
    with open(f"{diretorio}/{pdf_file}", 'rb') as f:
        pdf = PdfReader(f)
        text = ''
        for page in range(len(pdf.pages)):
            text += pdf.pages[page].extract_text()
        print(f'Texto do arquivo {pdf_file}:')
        print(text)
