#Faça um algoritmo que imprima a tabuada do 5
i = 0
c = 5
r = 0

while(i<=10):
    r = c * i
    print(r)
    i = i +1



#calcule a média de 2 alunos
i=0
qntd=2
acumulador = 0

while(i< qntd):
    n1= int(input("Nota1: "))
    n2= int(input("Nota2: "))
    med = (n1+n2)/2
    i= i +1
    acumulador = (acumulador + med)/i
    print("Média do aluno {0} foi {1}" .format(i, med))
    
print("A média da sala é: ", acumulador)


#some somente os numeros inteiros pares digitados pelo usuario
numero=int(input("Digite um numero inteiro "))
soma = 0
i = 0

while(numero!=0):
    if(numero % 2 == 0):
        soma = soma + numero
        i = i + 1
    numero = int(input("Digite um numero inteiro ="))
media = soma/i
print(media)