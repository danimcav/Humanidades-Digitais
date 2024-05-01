import os
import re

def extract_interview_info(content):
    info = {
        'date': extract_date(content),
        'interviewer': extract_interviewer(content),
        'interviewee': extract_interviewee(content),
        'heading': extract_heading(content),
        'position': extract_position(content)
    }
    return info

def extract_interviewer(content):
    match_interviewer = re.search(r'<interviewer>(.*?)</interviewer>', content, re.IGNORECASE | re.DOTALL)
    if match_interviewer:
        return match_interviewer.group(1).strip()
    else:
        return None

def extract_interviewee(content):
    match_interviewee = re.search(r'<interviewee>(.*?)</interviewee>', content, re.IGNORECASE | re.DOTALL)
    if match_interviewee:
        return match_interviewee.group(1).strip()
    else:
        return None

def extract_date(content):
    match_date = re.search(r'<date>(.*?)</date>', content, re.IGNORECASE | re.DOTALL)
    if match_date:
        return match_date.group(1).strip()
    else:
        return None

def extract_heading(content):
    match_heading = re.search(r'<heading>(.*?)</heading>', content, re.IGNORECASE | re.DOTALL)
    if match_heading:
        return match_heading.group(1).strip()
    else:
        return 'Interview with Professor Farelo'

def extract_position(content):
    match_position = re.search(r'<position>(.*?)</position>', content, re.IGNORECASE | re.DOTALL)
    if match_position:
        return match_position.group(1).strip()
    else:
        return None

def extract_interview_content(content):
    return re.findall(r'<interview>(.*?)</interview>', content, re.IGNORECASE | re.DOTALL)

def save_to_md(info, interview_content, filename):
    md_content = "---\n"
    for key, value in info.items():
        md_content += f"{key}: {value}\n"
    md_content += "---\n\n"
    md_content += "\n".join(interview_content)

    md_filename = os.path.join(r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\Entrevista Prof Mario Farelo\Code", filename)
    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

# Caminho do arquivo específico
caminho_arquivo_especifico = r"D:\Users\lfher\Dani\UMinho\Processamento de Linguagem  Prof João\Entrevista Prof Mario Farelo\Transcrições\Entrevista_Professor_Mario_Farelo_por_Daniella_Monteiro_Cavalheiro_Editado.txt"

# Processar apenas o arquivo específico
try:
    with open(caminho_arquivo_especifico, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        info_entrevista = extract_interview_info(conteudo)
        interview_content = extract_interview_content(conteudo)
        save_to_md(info_entrevista, interview_content, "Interview_Prof_Farelo.md")

except Exception as e:
    print(f"Erro ao processar o arquivo {caminho_arquivo_especifico}: {str(e)}")

print("Processo concluído para o arquivo Interview_Prof_Farelo.md.")
