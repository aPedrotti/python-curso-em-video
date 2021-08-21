#!/usr/local/bin/python

## Operadores Aritiméticos
# + Adicao
# - Subtracao
# * Multiplicacao - 
# / Divisao -
# ** potencia -
# // divisao inteira
# % resto da divisao
# **(1/2) Raiz Quadrada
# ## Prioridades
# 1 = ()
# 2 = **
# 3 = *, /, //, %
# 4 = +, -
# 
# #

print('='*10,'Formating Strings')
nome = input('Qual é seu nome ')
print('Prazer em te conhecer {} !'.format(nome))
print('='*4,'Com espaçamento')
print('Prazer em te conhecer {:20} !'.format(nome))
print('='*4,'Alinhado a direita')
print('Prazer em te conhecer {:>20}'.format(nome))
print('='*4,'Com definição de centralizadores e caractere disso')
print('Prazer em te conhecer {:=^20}'.format(nome))

print('='*10,'Calculating values')
n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('RESULTADOS => Soma = {} Multiplicação = {} Divisão = {} Div Inteira = {} Exponenciaçao = {}'.format(s,m,d,di,e))

print('='*4,'Quebrando linha')
print('Soma = {} \nMultiplicação = {}\nDivisão = {} \nDiv Inteira = {} \nExponenciaçao = {}'.format(s,m,d,di,e))


print('='*10,'CHALLENGES')
print('Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor')
n1 = int(input('Digite um numero '))
print('')

print('Ler um numero e mostre seu dobro, triplo e raiz quadrada')
n1 = int(input('Digite um numero '))
print('')

print('Ler um numero em metros e exiba convertido em centimetros e milímetros')
n1 = int(input('Digite quantos metros'))
print('')

print('Ler um numero e faça a sua tabuada')
n1 = int(input('Digite um numero para tabuada '))
print('')

dolar=float(5.5)
print('Ler um numero de quanto ela tem na carteira e converter em dólares ')
n1 = int(input('Digite seus pilas '))
print('')
print('Ler altura e largura da parede e calcular a quantidade de tinta para pintar | 1L/2m²')
n1 = int(input('Digite a altura '))
n2 = int(input('Digite a largura '))
print('')

desconto=float(5/100)
print('Ler um preço e calcule um desconto de',desconto)
n1 = int(input('Digite o preço: '))
print('')

aumento=float(5/100)
print('Ler um salario e calcule um aumento de',aumento)
n1 = int(input('Digite o salario: '))
print('')