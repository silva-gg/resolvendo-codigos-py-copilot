# Verificando se uma palavra é um palíndromo

def verificar_palindromo(palavra):
    """
    Verifica se uma palavra é um palíndromo.
    
    Args:
        palavra: String a ser verificada
    
    Returns:
        Boolean - True se for palíndromo, False caso contrário
    """
    # Remove espaços e converte para minúsculas para comparação consistente
    palavra_limpa = palavra.replace(" ", "").lower()
    # Inverte a palavra e compara com a original
    palavra_invertida = palavra_limpa[::-1]
    return palavra_limpa == palavra_invertida


def main():
    """Função principal que recebe entrada do usuário e exibe o resultado."""
    palavra = input("Digite uma palavra: ")
    
    if verificar_palindromo(palavra):
        print(f'"{palavra}" é um palíndromo!')
    else:
        print(f'"{palavra}" não é um palíndromo.')


if __name__ == "__main__":
    main()
