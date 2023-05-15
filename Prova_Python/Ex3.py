#Verificação dp número se é ou não primo
x = int(input("Digite um número a seguir para verificação se é ou não primo"))
acm = 0

for i in range(2, x, 1):
    if(x%i==0):
        acm = 1
if(acm ==1):
    print("Não é um numero primo")
else:
    print("É um número primo")

        
        


