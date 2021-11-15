#!/usr/bin/python


from math import acos, asin, atan, radians
# Eles lêm em graus radianos

print('Ler um ângulo e mostre o valor do seu seno, cosseno e tangente') 

angulo = float(input('Digite um angulo: '))
# Converte para radianos
rad = radians(angulo)
# Agrupando
# seno = math.sin(math.radians(angulo))

seno = asin(rad)
cosseno = acos(rad)
tangente = atan(rad)

print('A partir do angulo {} digitado em radianos {:.4f} seu seno é {:.4f}, cosseno {:.4f}, tangente {:.4f}'.format(angulo,rad,seno,cosseno,tangente))