# Humanidades-Digitais
# Folha 8 - Análise de Texto

## Descrição
Este projeto consiste em um conjunto de scripts em Python para análise de texto do arquivo "folha8.OUT.txt". Ele realiza diversas tarefas, incluindo contagem de publicações, extração de tags e análise das classes gramaticais das palavras presentes nessas tags.

## Tarefas Realizadas

### Exercício #1: Contagem de Publicações
O script realiza a contagem do número total de publicações na base de dados.

### Exercício #2: Extração de Tags
As tags são extraídas do texto, com destaque para aquelas presentes entre chaves `{}`.

### Exercício #3: Contagem de Tags
A contagem e a frequência das tags são calculadas.

### Exercício #4: Análise de Classes Gramaticais
As classes gramaticais das palavras presentes nas tags `{}` são identificadas e suas frequências são visualizadas em um gráfico de barras.

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

## Uso
1. Certifique-se de ter o arquivo `folha8.OUT.txt` no diretório do projeto.
2. Execute o script principal `analise_texto.py`:

    ```
    python analise_texto.py
    ```

3. O script realizará a análise do texto e exibirá um gráfico mostrando a frequência das classes gramaticais das palavras presentes nas tags `{}`.

## Estrutura do Projeto
- `folha8.OUT.txt`: Arquivo de texto a ser analisado.
- `analise_texto.py`: Script principal para análise do texto.
- `README.md`: Documentação do projeto.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto e enviar pull requests para melhorias, correções de bugs ou novos recursos.


