# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def somar(num1, num2):
    """Retorna a soma de dois números."""
    return num1 + num2


def subtrair(num1, num2):
    """Retorna a subtração de dois números."""
    return num1 - num2


def multiplicar(num1, num2):
    """Retorna a multiplicação de dois números."""
    return num1 * num2


def dividir(num1, num2):
    """Retorna a divisão de dois números."""
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida"
    return num1 / num2


def main():
    """Função principal que recebe entrada do usuário e exibe o resultado."""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    print(f"\nResultados:")
    print(f"Soma: {somar(num1, num2)}")
    print(f"Subtração: {subtrair(num1, num2)}")
    print(f"Multiplicação: {multiplicar(num1, num2)}")
    print(f"Divisão: {dividir(num1, num2)}")


if __name__ == "__main__":
    main()