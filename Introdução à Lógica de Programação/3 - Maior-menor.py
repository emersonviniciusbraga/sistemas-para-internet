maior = menor = 0
for i in range(10):
    numero = int(input("Informe um número: "))
    if i == 0:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
print("O maior e menor números da lista foram {} e {}, respectivamente".format(maior, menor))
