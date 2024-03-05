import os
import fitz  # PyMuPDF

# Especifica o diretório onde os PDFs serão salvos
diretorio = "D:/Users/lfher/Dani/UMinho/Processamento de Linguagem  Prof João/saida"

# Cria o diretório se ele não existir
os.makedirs(diretorio, exist_ok=True)

# Baixa os PDFs
for n in range(1, 20):  # Ajuste o intervalo conforme necessário
    comando = f'wget --no-check-certificate -P "{diretorio}" -nd "https://natura.di.uminho.pt/~jj/umdicas/UMdicas-{n}.pdf"'
    os.system(comando)

# Lista todos os PDFs baixados
pdf_files = [f for f in os.listdir(diretorio) if f.endswith('.pdf')]

# Extrair o texto de imagens em cada PDF
for pdf_file in pdf_files:
    pdf_path = os.path.join(diretorio, pdf_file)
    
    doc = fitz.open(pdf_path)

    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_index, img_info in enumerate(images):
            img_index += 1
            base_image = doc.extract_image(img_index)
            image_bytes = base_image["image"]

            # Faça o processamento da imagem conforme necessário (usando OCR, por exemplo)
            # Aqui você pode usar uma biblioteca como pytesseract para OCR

    doc.close()
