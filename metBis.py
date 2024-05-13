#Trabalho de Cálculo Numérico - Arthur Angelo

import math
def calculaPM (a,b ): #calcula o ponto médio
    return a + ((b-a)/2)

def func(x): #calcula a função
    return x**2 - 17

def signal(n): #verifica o sinal
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
    
maxInteracoes = 1000
    
intervaloInicial = [4,5]
epslon = 10**(-6)
i = 1
    
while i <= maxInteracoes:
    p = calculaPM(intervaloInicial[0],intervaloInicial[1])
    if abs(func(p)) < epslon:
        break
    elif signal(func(intervaloInicial[0]))*signal(func(p)) > 0:
        intervaloInicial[0] = p
    else:
        intervaloInicial[1] = p
    i+=1
    
print(intervaloInicial)