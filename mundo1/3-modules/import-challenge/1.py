#!/usr/bin/python

from math import trunc

print('# Ler um número real e mostre sua porção inteira. Ex: 6.127, mostra 6')

num = float(input('Digite um número: '))
truncked = trunc(num)
print('O numero digitado é {} e sua porcao inteira é {}'.format(num,truncked))

# OR

num = float(input('Digite um valor: '))
print('O valor digitado é {} e a parte inteira é {}'.format(num,int(num)))