# Verificando se um número é par ou ímpar

def verificar_par_impar(numero):
    """
    Verifica se um número é par ou ímpar.
    
    Args:
        numero: Número inteiro a ser verificado
    
    Returns:
        String indicando se o número é "par" ou "ímpar"
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def main():
    """Função principal que recebe entrada do usuário e exibe o resultado."""
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado}")


if __name__ == "__main__":
    main()
