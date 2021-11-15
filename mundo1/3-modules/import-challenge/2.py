#!/usr/bin/python

from math import hypot

print('# Ler comprimento do cateto oposto e do adjacente e calcule a hipotenusa')

opo = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjasente: '))

hipo = hypot(opo,adj)
#hipo = ((opo ** 2 + adj ** 2 ) ** (1/2))
print('A hipotenusa vai medir {:.2f}'.format(hipo))