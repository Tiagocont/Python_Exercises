#Leia numeros positivos e calcule o quadrado de cada um
print("Iremos calcular o quadrado dos números")
r =input("Deseja realizar o procedimento? (sim para 'sim' e não para 'não')").upper()
while(r == 'SIM'):
    n = int(input("Digite um número:"))
    res = n ** 2
    print("O quadrado de {0} é {1}" .format(n, res))
    r = input("Deseja realizar o procedimento novamente? (sim para 'sim' e não para 'não')").upper()

#Faça um algoritmo que imprima a tabuada de qualquer numero
i = 0
tab = int(input("digite um numero inteiro para impressão da tabuada: "))
r = 0

while(i<=10):
    r = tab * i
    print(r)
    i = i +1



#calcule a média de 2 alunos
print("Iremos calcular a média dos alunos")
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
print("Iremos calcular os numeros inteiros pares digitados (digite 0 para sair)")
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