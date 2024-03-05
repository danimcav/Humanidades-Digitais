import os
import fitz

diretorio = "D:/Users/lfher/Dani/UMinho/Processamento de Linguagem Prof João/saida"

# Lista todos os arquivos no diretório
pdf_files = [f for f in os.listdir(diretorio) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    pdf_path = os.path.join(diretorio, pdf_file)
    
    try:
        doc = fitz.open(pdf_path)

        print(f"Processando o arquivo: {pdf_file}")
        print(f"Número de páginas: {doc.page_count}")
        print(f"Metadados: {doc.metadata}")

        # Itera sobre as páginas
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            
            # Extraindo texto da página
            text = page.get_text()
            print(f'Texto da página {page_num + 1}: {text}')

            # Salvando a página como uma imagem
            pix = page.get_pixmap()
            image_path = os.path.join(diretorio, f"{pdf_file}_page{page_num + 1}.png")
            pix.save(image_path)
            print(f'Imagem da página {page_num + 1} salva em: {image_path}')

        doc.close()
        print(f"Concluído o processamento do arquivo: {pdf_file}\n")

    except fitz.FileNotFoundError as e:
        print(f"Erro ao abrir o arquivo {pdf_file}: {e}")
    except Exception as e:
        print(f"Erro desconhecido ao processar o arquivo {pdf_file}: {e}")
