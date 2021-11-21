#!/usr/bin/python

from random import shuffle

print('# Ler quatro nomes e ordenar randomicamente')

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4]

shuffle(lista)
print('A sequencia dos alunos para limpara é: ')
print(lista)