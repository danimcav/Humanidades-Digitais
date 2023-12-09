# Análise de Texto - Folha 8 Final

Este código em Python realiza uma análise básica de um arquivo de texto chamado "folha8.OUT.txt". Ele oferece funcionalidades para contagem de publicações, extração de tags do texto e geração de gráficos baseados nas classes gramaticais das palavras presentes nessas tags.

## Funcionalidades

1. **Leitura do Arquivo Fonte**
    - A função `le_arquivo_fonte(nomearquivo)` lê o conteúdo do arquivo especificado.
   
2. **Quebra por Matérias**
    - A função `quebra_por_materias(folha)` separa o texto em matérias, utilizando o marcador "<pub>" como referência.

3. **Exercício #1: Contagem de Publicações**
    - A função `exercicio_01(lista_materias)` calcula o total de matérias presentes no arquivo.

4. **Exercício #2: Extração das Tags**
    - A função `extrair_tags(materia)` extrai as tags presentes em cada matéria usando expressões regulares.

5. **Exercício #3: Contagem das Tags**
    - A função `calcular_contagem_tags(materias)` calcula e exibe a contagem das tags presentes no texto.

6. **Exercício #4: Análise de Classes Gramaticais**
    - O código utiliza a biblioteca spaCy para analisar as classes gramaticais das palavras presentes nas tags. No entanto, detalhes específicos sobre a geração do gráfico baseado nessas classes não foram implementados.

## Uso

1. Certifique-se de ter o arquivo `folha8.OUT.txt` no mesmo diretório que o script.
2. Execute o script Python para analisar o arquivo e obter as informações desejadas.

## Pré-requisitos
- Python 3.x
- Instalação do spaCy (`pip install spacy`)
- Modelo em português do spaCy (`python -m spacy download pt_core_news_sm`)

## Configuração
1. Clone o repositório ou faça o download do arquivo `folha8.OUT.txt` para o diretório do projeto.
2. Instale as dependências necessárias usando o `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```
    
## Estrutura do Projeto
- `folha8.OUT.txt`: Arquivo de texto a ser analisado.
- `analise_texto.py`: Script principal para análise do texto.
- `README.md`: Documentação do projeto.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto e enviar pull requests para melhorias, correções de bugs ou novos recursos.


