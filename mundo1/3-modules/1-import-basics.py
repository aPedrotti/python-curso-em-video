#!/usr/bin/python
# import something - will import all from that library - You have to mention function father
# --- something = math.sqrt(number)
# from something import something_specific - import only what you need - You don't need to mention function father
# -- something = sqrt(number)

# Source of modules
#https://docs.python.org/3.8/py-modindex.html
# In the editor = Ctrl + Space, after the import
from math import sqrt, floor, ceil
# import math

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))
print('A raiz de {} é igual a {}, arredondado para cima'.format(num,ceil(raiz)))
print('A raiz de {} é igual a {}, arredondado para baixo'.format(num,floor(raiz)))
print('A raiz de {} é igual a {:.2f}, definindo 2 casas decimais'.format(num,raiz))
