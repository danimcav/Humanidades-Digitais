texto = """WebGitHub is where over 100 million developers 
# shape the future of software, together. Contribute to 
# the open source community, manage your Git repositories, 
# review code like."""

def main():
    # Contar o número total de caracteres no texto
    total_caracteres = len(texto)
    print("Número total de caracteres:", total_caracteres)

    # Dividir o texto em linhas
    linhas = texto.splitlines()
    numero_linhas = len(linhas)
    print("Número de linhas:", numero_linhas)

    # Dividir o texto em palavras
    palavras = texto.split()
    numero_palavras = len(palavras)
    print("Número de palavras:", numero_palavras)
    
    # Substituir "GitHub" por "Git Hub" no texto
    texto_substituido = texto.replace("GitHub", "Git Hub")
    print("Texto com substituição:")
    print(texto_substituido)

    # Transformar o texto em letras minúsculas
    texto_minusculo = texto.lower()
    print("Texto em letras minúsculas:")
    print(texto_minusculo)

    # Juntar as palavras em uma única string usando espaço como separador
    texto_junto = ' '.join(palavras)
    print("Texto após juntar as palavras:")
    print(texto_junto)

    # Contar o número de frases dividindo o texto por pontos
    frases = texto.split(".")
    numero_frases = len(frases)
    print("Número de frases:", numero_frases)

if __name__ == "__main__":
    main()
