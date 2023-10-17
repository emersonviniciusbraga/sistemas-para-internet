numero = int(input("Escreva um número inteiro: "))
print("Tabuada de {}:" .format(numero))
for i in range(1, 11):
    resultado = numero * i
    print("{} X {} = {}".format(numero, i, resultado))