#Pulando numeros de 2 em 2
for i in range(1,10,2):
    print(i)


#Numeros multiplos de 3 entre 0 e 9
for n in range(0,9):
    if(n%2==1):
        if(n%3==0):
            print("{0}, é multiplo de 3" . format(n))


"""
#Contagem regressiva de 1 minuto
for mnt in range(1,-1,-1):
   for seg in range(59, -1, -1):
        print(mnt, ":", seg )
"""


#Contrua um programa que leia um conjunto de dados contendo altura, sexo ("M" ou "F") 
#de 7 pessoas e, depois, calcule e escreva:
#a maior e a menor altura do grupo
#a média da altura das mulheres
maior = 0
menor = 1000
altura_m = 0.0
i = 0
for n in range(1, 3):
    altura=float(input("Digite sua altura: "))
    sexo = input("Digite seu sexo (F/M)")
    if(altura> maior):
        maior = altura
    if(altura< menor):
        menor = altura
    if(sexo =="F"):
        altura_m += altura
        i += 1
        med = altura_m/i

print(maior)
print(menor)
if(altura_m> 0):
    print(med)


#Escreva um algoritmo que exiba a soma
#de todos os pares entre um limite inferior 
#e superior digitado pelo usuario
soma = 0
inf = int(input("Digite um número para traçarmos um intervalo: "))
sup = int(input("Digite o limite: "))

if(inf>sup):
    aux = sup
    sup = inf
    inf = aux 
for i in range(inf, sup+1):
    soma += i
print(soma)


#Faça uma piramide de numeros iguais
n = int(input("Digite a quantidade"))

for i in range(1, n+1):
    print(str(i)*i)
    i+=1
    