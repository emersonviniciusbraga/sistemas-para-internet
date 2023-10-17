saque = int(input("Qual valor deseja sacar? "))
while saque < 1:
    print("O valor informado deve ser maior ou igual a 1!")
    saque = int(input("Qual valor deseja sacar? "))


valor = int(input("Qual o valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)?"))
while valor != 1 and valor != 2 and valor != 5 and valor != 10 and valor != 20 and valor != 50 and valor != 100:
    print("A cédula informada não existe, informe um novo valor de cédula.")
    valor = int(input("Qual o valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)?"))

if valor == 100:
    resto1 = (saque % 100)
    resto2 = (resto1 % 50)
    resto3 = (resto2 % 20)
    resto4 = (resto3 % 10)
    resto5 = (resto4 % 5)
    resto6 = (resto5 % 2)
    resto7 = (resto6 % 1)

    nota100, nota50, nota20, nota10, nota5, nota2, nota1 = saque // 100, resto1 // 50, resto2 // 20, resto3 // 10, resto4 // 5, resto5 // 2, resto6 // 1

    print("O valor sacado foi de R$ {}".format(saque))
    print("Cédulas:")
    print("{} de R$ 100".format(nota100))
    print("{} de R$ 50".format(nota50))
    print("{} de R$ 20".format(nota20))
    print("{} de R$ 10".format(nota10))
    print("{} de R$ 5".format(nota5))
    print("{} de R$ 2".format(nota2))
    print("{} de R$ 1".format(nota1))

elif valor == 50:
    resto2 = (saque % 50)
    resto3 = (resto2 % 20)
    resto4 = (resto3 % 10)
    resto5 = (resto4 % 5)
    resto6 = (resto5 % 2)
    resto7 = (resto6 % 1)

    nota50, nota20, nota10, nota5, nota2, nota1 = saque // 50, resto2 // 20, resto3 // 10, resto4 // 5, resto5 // 2, resto6 // 1

    print("O valor sacado foi de R$ {}".format(saque))
    print("Cédulas:")
    print("{} de R$ 50".format(nota50))
    print("{} de R$ 20".format(nota20))
    print("{} de R$ 10".format(nota10))
    print("{} de R$ 5".format(nota5))
    print("{} de R$ 2".format(nota2))
    print("{} de R$ 1".format(nota1))

elif valor == 20:
    resto3 = (saque % 20)
    resto4 = (resto3 % 10)
    resto5 = (resto4 % 5)
    resto6 = (resto5 % 2)
    resto7 = (resto6 % 1)

    nota20, nota10, nota5, nota2, nota1 = saque  // 20, resto3 // 10, resto4 // 5, resto5 // 2, resto6 // 1

    print("O valor sacado foi de R$ {}".format(saque))
    print("Cédulas:")
    print("{} de R$ 20".format(nota20))
    print("{} de R$ 10".format(nota10))
    print("{} de R$ 5".format(nota5))
    print("{} de R$ 2".format(nota2))
    print("{} de R$ 1".format(nota1))

elif valor == 10:
    resto4 = (saque % 10)
    resto5 = (resto4 % 5)
    resto6 = (resto5 % 2)
    resto7 = (resto6 % 1)

    nota10, nota5, nota2, nota1 = saque // 10, resto4 // 5, resto5 // 2, resto6 // 1

    print("O valor sacado foi de R$ {}".format(saque))
    print("Cédulas:")
    print("{} de R$ 10".format(nota10))
    print("{} de R$ 5".format(nota5))
    print("{} de R$ 2".format(nota2))
    print("{} de R$ 1".format(nota1))

elif valor == 5:
    resto5 = (saque % 5)
    resto6 = (resto5 % 2)
    resto7 = (resto6 % 1)

    nota5, nota2, nota1 = saque // 5, resto5 // 2, resto6 // 1

    print("O valor sacado foi de R$ {}".format(saque))
    print("Cédulas:")
    print("{} de R$ 5".format(nota5))
    print("{} de R$ 2".format(nota2))
    print("{} de R$ 1".format(nota1))

elif valor == 2:
    resto6 = (saque % 2)
    resto7 = (resto6 % 1)

    nota2, nota1 = saque // 2, resto6 // 1

    print("O valor sacado foi de R$ {}".format(saque))
    print("Cédulas:")
    print("{} de R$ 2".format(nota2))
    print("{} de R$ 1".format(nota1))

elif valor == 1:
    resto7 = (saque % 1)
    nota1 = saque // 1

    print("O valor sacado foi de R$ {}".format(saque))
    print("Cédulas:")
    print("{} de R$ 1".format(nota1))
