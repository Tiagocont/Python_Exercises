#Apresentando vetores
cores = ["nose", "oi", "shh"]
tam = len(cores) 
print("O tamanho é {0}" .format(tam))

i = int(input("digite o indice"))
print('cores['+i+'] = ' +cores[i])


#Atribui 1 para pares e 0 aosa impares
vetor = [] 

for i in range(0, 101, 1):
    if (i%2==0):
        vetor.append([i])==1
    else:
        vetor.append([i])==0



#calcula soma de 10 numeros
vetor=[0]*10
soma = 0 
for i in range (0,10):
    soma += vetor[i]
print(soma)


#multiplicacao de vetores
"""vetorA = [1, 2, 3, 4, 5]
vetorB = [6, 7, 8, 9, 10]
vetorC = [x*y for x in vetorA for y in vetorB]"""
vetorA = []
vetorB = [0,1,2,3,4,5,6,7]
vetorC = []

for i in range(0, 8):
    vetorA.append(int(input("digite:")))

for i in range(-1, len(vetorA)):
    soma = vetorA[i] + vetorB[i]
    vetorC.append(soma)

print(vetorC)

