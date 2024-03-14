import re
import os

diretorio = r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\saida\PDF_to_TEXT"

padrao_entrevistado = r"<entrevistado>(.?)</entrevistado>|<entrevistada>(.?)</entrevistada>"
padrao_entrevista = r'<Entrevista>(.*?)</Entrevista>'
padrao_assunto = r"<assunto>(.*?)</assunto>"
padrao_cargo = r"<cargo>(.*?)</cargo>"
padrao_universidade = r"<universidade>(.*?)</universidade>"
padrao_numero_paginas = r"<nr\. pag\.>(.*?)<\/nr\. pag\.>"
padrao_numero_edicao = r"<edição>(.*?)</edição>"
padrao_data = r"<data>(.*?)<\/data>"

# formatar os metadados
def formatar_metadados(metadados):
    return f"Jornal: UMdicas\n" + \
           f"Edição: {metadados['edicao']}\n" + \
           f"Universidade: {metadados['universidade']}\n" + \
           f"Entrevistado(s): {', '.join(metadados['entrevistado'])}\n" + \
           f"Assunto: {metadados['assunto']}\n" + \
           f"Cargo: {metadados['cargo']}\n" + \
           f"Data: {metadados['data']}\n" + \
           f"Número de Páginas: {metadados['numero_paginas']}\n" + \
           "==============================\n"

# armazenar todas as entrevistas e metadados
entrevistas_meta = []

# loop para arquivos de UMdicas-100.txt até UMdicas-150.txt
for i in range(101, 151):
    nome_arquivo = f"UMdicas-{i}.txt"
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()

                # extrai info
                entrevista = re.search(padrao_entrevista, conteudo, re.IGNORECASE)
                entrevistados = re.findall(padrao_entrevistado, conteudo, re.IGNORECASE)
                assunto = re.search(padrao_assunto, conteudo, re.IGNORECASE)
                cargo = re.search(padrao_cargo, conteudo, re.IGNORECASE)
                universidade = re.search(padrao_universidade, conteudo, re.IGNORECASE)
                numero_paginas = re.search(padrao_numero_paginas, conteudo, re.IGNORECASE)
                numero_edicao = re.search(padrao_numero_edicao, conteudo, re.IGNORECASE)
                data = re.search(padrao_data, conteudo, re.IGNORECASE)

                # metadados
                metadados = {
                    'edicao': numero_edicao.group(1) if numero_edicao else 'Não encontrado',
                    'entrevistado': [entrevistado[0] for entrevistado in entrevistados],
                    'assunto': assunto.group(1) if assunto else 'Não encontrado',
                    'cargo': cargo.group(1) if cargo else 'Não encontrado',
                    'universidade': universidade.group(1) if universidade else 'Não encontrado',
                    'numero_paginas': numero_paginas.group(1) if numero_paginas else 'Não encontrado',
                    'data': data.group(1) if data else 'Não encontrado'
                }

                # colar as entrevistas com os meta
                entrevistas_meta.append(formatar_metadados(metadados) + (entrevista.group(1) if entrevista else 'Entrevista não encontrada'))

        except Exception as e:
            print(f"Erro ao processar o arquivo {caminho_arquivo}: {str(e)}")
    else:
        print(f"Arquivo não encontrado: {caminho_arquivo}")

# caminho do arquivo de saída no mesmo diretório dos arquivos de entrada
caminho_saida = os.path.join(diretorio, "entrevistas_meta.txt")

# salvar em arquivo
with open(caminho_saida, "w", encoding="utf-8") as saida:
    for entrevista_meta in entrevistas_meta:
        saida.write(entrevista_meta + "\n\n")

print("Processo concluído. Resultados salvos em:", caminho_saida)
