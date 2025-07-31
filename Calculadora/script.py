def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

def menu():
    print("=== Calculadora Simples ===")
    print("Escolha a operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

def main():
    while True:
        menu()
        escolha = input("Digite a opção (1/2/3/4/5): ").strip()

        if escolha == '5':
            print("Saindo da calculadora. Até mais!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida, tente novamente.\n")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números.\n")
            continue

        if escolha == '1':
            resultado = adicionar(num1, num2)
            op = '+'
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            op = '-'
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            op = '*'
        elif escolha == '4':
            resultado = dividir(num1, num2)
            op = '/'

        print(f"\n{num1} {op} {num2} = {resultado}\n")

if __name__ == "__main__":
    main()