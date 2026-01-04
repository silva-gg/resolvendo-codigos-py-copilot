# Vamos solicitar uma string e um número inteiro como entrada e retornar a string repetida

def repetir_texto(texto, vezes):
    """
    Repete um texto o número de vezes especificado.
    
    Args:
        texto: String a ser repetida
        vezes: Número inteiro de repetições
    
    Returns:
        String repetida o número de vezes informado
    """
    return texto * int(vezes)


def main():
    """Função principal que recebe entrada do usuário e exibe o resultado."""
    texto = input("Digite o texto: ")
    vezes = int(input("Digite o número de repetições: "))
    resultado = repetir_texto(texto, vezes)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()