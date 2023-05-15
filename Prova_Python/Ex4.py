# Verificação se um número natural é triangular
x = int(input("Digite um número para verificação se é ou não triangular"))
acm = 0

for i in range(1, x, 1):
    if((i)*(i+1)*(i+2) == x):
        acm = 1


if(acm ==1):
    print("É um número triangular")
else:
    print("Não é um número triangular")



