# Conversão de segundos para horas, minutos e segundos.
#segundo = 59
#3600s = 1h
#862400 = 24h
print(60*60)
print(3600 *24)
x = int(input("Digite o tempo em segundos"))
horas = x //3600
minutos = (x%3600)//60
s = x%60

print("{0}:{1}:{2}".format(horas, minutos, s))