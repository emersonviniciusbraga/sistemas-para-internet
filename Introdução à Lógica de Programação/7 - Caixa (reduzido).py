saque = int(input("Qual valor deseja sacar? "))
while saque < 1:
    print("O valor informado deve ser maior ou igual a 1!")
    saque = int(input("Qual valor deseja sacar? "))

cedula = int(input("Qual o valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)?"))
while cedula != 1 and cedula != 2 and cedula != 5 and cedula != 10 and cedula != 20 and cedula != 50 and cedula != 100:
    print("A cédula informada não existe, informe um novo valor de cédula.")
    cedula = int(input("Qual o valor máximo das cédulas (1 - 2 - 5 - 10 - 20 - 50 - 100)?"))

total = saque
total_cedulas = 0

print("O valor sacado foi de R$ {}".format(saque))
print("Cédulas:")

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} de R$ {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break