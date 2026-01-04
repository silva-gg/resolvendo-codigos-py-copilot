# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

def concatenar_dados(dado1, dado2):
    """
    Concatena dois dados em uma única string.
    
    Args:
        dado1: Primeiro dado a ser concatenado
        dado2: Segundo dado a ser concatenado
    
    Returns:
        String com os dois dados concatenados
    """
    return str(dado1) + str(dado2)


def main():
    """Função principal que recebe entrada do usuário e exibe o resultado."""
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = concatenar_dados(dado1, dado2)
    print(f"Resultado da concatenação: {resultado}")


if __name__ == "__main__":
    main()