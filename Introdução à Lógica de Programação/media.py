nome = str(input("Informe o nome do aluno: "))
n1 = int(input("informe a nota do 1º Bimestre (0 a 100): "))
n2 = int(input("informe a nota do 2º Bimestre (0 a 100): "))
n3 = int(input("informe a nota do 3º Bimestre (0 a 100): "))
n4 = int(input("informe a nota do 4º Bimestre (0 a 100): "))

mp = int(((n1*2)+(n2*2)+(n3*3)+(n4*3))/(2+2+3+3))
if mp >= 60:
    print("\033[1;0;42mO aluno {} obteve a média {} e está aprovado.\033[m".format(nome, mp))
elif mp >= 20 and mp <= 59:
    print("\033[1;31;43mO aluno {} obteve a média {} e está em recuperação.\033[m".format(nome, mp))
else:
    print("\033[1;30;41mO aluno {} obteve a média {} e está reprovado.\033[m".format(nome, mp))

