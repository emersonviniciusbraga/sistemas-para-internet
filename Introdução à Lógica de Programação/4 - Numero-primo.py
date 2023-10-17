def Primo(num):
    if num <= 1:
        return f"O número {num} não é primo."

    for i in range(2, num//2):
        if num % i == 0:
            return f"O número {num} não é primo."
    return f"O número {num} é primo."

try:
    print("TESTE DE NUMERO PRIMO")
    num = int(input("Digite um número: "))
    resultado = Primo(num)
except:
    print("ERRO! Essa não é uma opção válida!")
else:
    print(resultado)