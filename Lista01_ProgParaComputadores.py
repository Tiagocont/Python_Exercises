#LISTA DE EXERCÍCIOS EM PYTHON

#Exercício que diz qual o maior número digitado

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if(n1>= n2 and n1>=n3):
    print("o maior número digitado foi: {0}" .format(n1))
elif(n2>= n1 and n2>=n3):
    print("o maior número digitado foi: {0}" .format(n2))
else:
    print("o maior número digitado foi: {0}" .format(n3))

#Exercício que diz se o número inteiro é par ou impar

num1 = int(input("Digite um número: "))

if(num1%2==0):
    print("O número é par")
else:
    print("O número é ímpar")


#Exercício das coordenadas para saber se está dentro ou não do país

print("Digite suas coordenadas")
nmbx = float(input("Digite x: "))
nmby = float(input("Digite y: "))

if(nmbx >= -800 and nmbx <= 22 and nmby>=-20 and nmby<=35):
    print("As coordenadas correspondem ao seu próprio país")
else:
    print("As coordenadas NÃO correspondem ao seu próprio país")

