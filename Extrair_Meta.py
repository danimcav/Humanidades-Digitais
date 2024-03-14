import os
import re

def extrair_info_entrevista(conteudo):
    info = {
        'jornal': re.search(r'UMdicas', conteudo, re.IGNORECASE).group() if re.search(r'UMdicas', conteudo, re.IGNORECASE) else 'Não encontrado',
        'edicao': extrair_edicao(conteudo),
        'universidade': re.search(r'Universidade do Minho', conteudo, re.IGNORECASE).group() if re.search(r'Universidade do Minho', conteudo, re.IGNORECASE) else 'Não encontrado',
        'entrevistados': extrair_entrevistados(conteudo),
        'data': extrair_data(conteudo),
        'num_paginas': extrair_num_paginas(conteudo),
    }

    return info

def extrair_edicao(conteudo):
    match_edicao = re.search(r'(?:Edição\s+(\d+)|Edição\s*N\.º\s*(\d+)|EDIÇÃO\s*N.º\s*(\d+))', conteudo, re.IGNORECASE)
    if match_edicao:
        return match_edicao.group(1) if match_edicao.group(1) else (match_edicao.group(2) if match_edicao.group(2) else match_edicao.group(3))
    else:
        return 'Não encontrado'

def extrair_entrevistados(conteudo):
    match_entrevistados = re.findall(r'(entrevista\s+a\s+.*?|entrevista\s+ao\s+.*?)$', conteudo, re.IGNORECASE | re.MULTILINE)
    if match_entrevistados:
        return [entrevistado.strip() for entrevistado in match_entrevistados]
    else:
        return ['Não encontrado']

def extrair_data(conteudo):
    match_data1 = re.search(r'(\d+\s*(?:JAN|FEV|MAR|ABR|MAIO|JUN|JUL|AGO|SET|OUT|NOV|DEZ)\s*\d{4})', conteudo, re.IGNORECASE)
    match_data2 = re.search(r'(\d+\s*(?:janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s*\d{4})', conteudo, re.IGNORECASE)
    match_data3 = re.search(r'Edição\s+\d+\s+-\s+(?:janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s+\d{4}', conteudo, re.IGNORECASE)

    if match_data1:
        return match_data1.group(0)
    elif match_data2:
        return match_data2.group(0)
    elif match_data3:
        return re.search(r'(?:janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s+\d{4}', match_data3.group(0), re.IGNORECASE).group(0)
    else:
        return 'Não encontrado'

def extrair_num_paginas(conteudo):
    match_num_paginas = re.findall(r'PÁGINA.*?(\d+)', conteudo, re.IGNORECASE)
    if match_num_paginas:
        return max(map(int, match_num_paginas))
    else:
        return 'Não encontrado'

def formatar_markdown(info):
    markdown_formatado = f"---\n"
    markdown_formatado += f"<jornal>{info['jornal']}</jornal>\n"
    markdown_formatado += f"<edicao>{info['edicao']}</edicao>\n"
    markdown_formatado += f"<universidade>{info['universidade']}</universidade>\n"
    markdown_formatado += f"<entrevistados>{', '.join(info['entrevistados'])}</entrevistados>\n"
    markdown_formatado += f"<data>{info['data']}</data>\n"
    markdown_formatado += f"<num_paginas>{info['num_paginas']}</num_paginas>\n"
    markdown_formatado += "---\n"

    return markdown_formatado

# Diretório dos arquivos TXT
diretorio = r'D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\saida\PDF_to_TEXT'

# Arquivo de resultados
arquivo_resultados = os.path.join(diretorio, 'resultados_meta.txt')

# Lista para armazenar os resultados de todos os arquivos
resultados_meta = []

# Loop pelos arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.txt'):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                info_entrevista = extrair_info_entrevista(conteudo)
                markdown_formatado = formatar_markdown(info_entrevista)
                resultados_meta.append(markdown_formatado)

        except Exception as e:
            print(f"Erro ao processar o arquivo {caminho_arquivo}: {str(e)}")

# Salvar resultados no arquivo
with open(arquivo_resultados, 'w', encoding='utf-8') as saida:
    for resultado_meta in resultados_meta:
        saida.write(resultado_meta + "\n")

print("Processo concluído.")
