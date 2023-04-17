#Faça um exercício que calcule a média aritmética entre duas notas
n1 = float(input("Digite a primeira nota "))

if(n1<=10 and n1>=0):
    n2 = float(input("Digite a segunda nota "))
    md= (n1+n2)/2
    if(n2<=10 and n2>=0):
        if(md>=5):
            print("Parabéns! Você foi aprovado, sua média foi {0}!" .format(md))
        else:
            print("Média insatisfatória... Você foi reprovado.")
else: 
    print("nota inválida")
    exit()


#Faça um exercício que leia e retorne qual a idade do usuário a partir do mês e ano 
aa = int(input("Escreva o ano atual "))
am = int(input("Escreva o mês "))
a = int(input("Escreva o ano do seu nascimento "))
m = int(input("Escreva o mês do seu nascimento "))

if(a>0):
    if(am<m):
        idAtual = (aa - 1) - a
        print("Você possui {0} anos" .format(idAtual))
    else:
        idAtual = aa - a
        print("Você possui {0} anos" .format(idAtual))


#Faça um programa que calcule o IMC e retorne se a pessoa está ou não dentro do peso ideal
nm = input("Olá! Por favor, digite seu nome: ")
s = input("digite seu sexo, digite M para masculino e F para feminino: ").upper()
h = float(input("Digite sua altura"))

if(s=="M"):
    pi = (72.7 * h) - 58
    print("{0}, seu peso ideal é {1}" .format(nm, pi))
elif(s == "F"):
    pi = (62.1 * h) - 58
    print("{0}, seu peso ideal é {1}" .format(nm, pi))
else:
    print("valor inválido")











    