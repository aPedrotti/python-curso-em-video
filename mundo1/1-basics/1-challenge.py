#!/usr/local/bin/python
# Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado

print('==== Desafio 1 ====')
nome=input('Por favor, digite o seu nome: ')

#print('Seja muito bem vindo ao fantástico mundo do python, ',nome,'!') or
print('Seja muito bem vindo ao fantástico mundo do python, {}!'.format(nome))