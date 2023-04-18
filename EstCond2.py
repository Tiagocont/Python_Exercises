#Faça um programa que leia os lados de um triangulo e retorne se é um triangulo e o tipo.
a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if(a+b>c) and (a+c>b) and (b+c>a):
    print("é um triangulo")
    if(a==b) and (a==c):
        print("É um triângulo equilátero")
    elif(a!=b and a!=c):
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Não é um triângulo")

#Calcule a média aritmética, caso a média seja insatisfatória (menor que 6), pergunte se quer realizar a recuperação
a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
rec = float
med = (a+b)/2

if(med >= 5):
    print("parabéns, você atingiu a nota necessária. Sua média foi de: {0}" .format(med))
else:
    print("xiii, suas notas não atingiu a média necessária, com o total de {0}" .format(med))
    d = input("Deseja realizar a recuperação?").upper()
    if(d == "SIM"):
        rec=float(input("digite a nota da recuperação: "))
        if(a >= b):
            med = (a+rec)/2
            if(med >= 5):
                print("Sua recuperação o fez atingir a média, parabéns! Sua média foi de {0}" .format(med))
            else:
                print("Sinto muito... Sua média foi de {0}" .format(med))
        else:
            med = (rec+b)/2
            if(med >= 5):
                print("Sua recuperação o fez atingir a média, parabéns! Sua média foi de {0}" .format(med))
            else:
                print("Sinto muito... Sua média foi de {0}" .format(med))
    elif(d == "NÃO" or d == "NAO"):
        print("Tudo bem, até a próxima")
    else:
        print("Valor inválido")

#Faça um exercício que retorne a formatação de horas
type = input("digite o tipo de horário (AM ou 24H)")

if(type =="AM"):
    turno = input("Digite o turno (AM ou PM)")
    hour = int(input("Escreva a hora"))
    m = int(input("Escreva a minutagem"))
    print("{0}h:{1}m {2}" .format(hour, m, turno))
elif(type =="24h"):
    hour = int(input("Escreva a hora"))
    m = int(input("Escreva a minutagem"))
    print("{0}h:{1}m" .format(hour, m))