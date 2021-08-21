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
print('Analisando o numero {}, seu antecessor é {} e seu sucessor é {}'.format(n1,n1-1,n1+1))

print('Ler um numero e mostre seu dobro, triplo e raiz quadrada')
n1 = int(input('Digite um numero '))
print('O dobro do número digitado é {}, \nO triplo é {}\nA raiz quadrada é {:.2f} arredondando em 2 casas'.format((n1*2),(n1*3),(n1**(1/2))))
print('Raiz quadrada pode ser calculada com a função pow(num,(1/2)) = {:.4f}'.format(pow(n1,(1/2))))

print('Ler valores e calcular a média aritimética')
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
print('A média da nota {} e {} é '.format(n1,n2,(n1+n2)/2))

print('Ler um numero em metros e exiba convertido em centimetros e milímetros')
n1 = float(input('Digite quantos metros '))
print('Os metros digitados equivalem a \n{}km\n{}hm\n{}dam\n{}cm\n{:.0f}mm'.format((n1/1000),(n1/100),(n1/10),(n1*100),(n1*1000)))

print('Ler um numero e faça a sua tabuada')
n1 = int(input('Digite um numero para tabuada '))
print('-'*10)
print('A tabuada do número digitado é \n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n1,n1*1,n1,n1*2,n1,n1*3,n1,n1*4,n1,n1*5,n1,n1*6,n1,n1*7,n1,n1*8,n1,n1*9,n1,n1*10))
print('-'*10)

dolar=float(5.5)
print('Ler um numero de quanto ela tem na carteira e converter em dólares ')
n1 = int(input('Digite seus pilas: R$'))
print('Os seus pilas equivalem a {:.2f} dólares'.format(n1/dolar))

print('Ler altura e largura da parede e calcular a quantidade de tinta para pintar | 1L/2m²')
n1 = float(input('Digite a altura '))
n2 = float(input('Digite a largura '))
m = n1*n2
print('Você precisará de {:.3f}L de tinta para cobrir esses {:.2f}m²'.format((m/2),m))

print('Ler um preço e calcule o desconto')
n1 = float(input('Digite o preço: '))
d1 = float(input('Digite numero percentual de desconto: '))
print('O preço digitado com desconto é igual a {:.2f}'.format(((100-d1)*n1)/100))
print('O preço digitado com desconto é igual a {:.2f}'.format(n1-n1*d1/100))

print('Ler um salario e calcule um aumento de')
n1 = float(input('Digite o salario: '))
a1 = float(input('Digite o percentual de aumento: '))
print('O novo salário com o aumento é {:.2f}'.format((n1+((a1*n1)/100))))

print('Ler uma temperatura em graus Celsius e converta para graus Fahrenheit.')
n1 = float(input('Digite a temperatura em Celcius: '))
print('{1}ºC é equivalenete a {0}ºF'.format(n1*9/5+32,n1)) #you can define ordering by your index

print('Ler quantos dias e quantos km foram rodados com um carro para calcular o valor do aluguel')
dias = int(input('Digite quantos dias ficastes com o carro: '))
km = int(input('Digite quantos km rodastes: '))
diaria = float(input('Digite o valor da diária: '))
rskm = float(input('Digite o valor do km rodado: '))
print('O valor total do aluguel para {} dias e {}km rodados é de {}'.format(dias,km,(dias*diaria)+(km*rskm)))