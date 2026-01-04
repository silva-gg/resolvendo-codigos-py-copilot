# Calculando a média de três notas

def calcular_media(nota1, nota2, nota3):
    """
    Calcula a média de três notas.
    
    Args:
        nota1: Primeira nota
        nota2: Segunda nota
        nota3: Terceira nota
    
    Returns:
        Float com a média das três notas
    """
    return (nota1 + nota2 + nota3) / 3


def main():
    """Função principal que recebe entrada do usuário e exibe o resultado."""
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media = calcular_media(nota1, nota2, nota3)
    print(f"A média das notas é: {media:.2f}")


if __name__ == "__main__":
    main()
