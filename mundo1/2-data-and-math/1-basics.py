#!/usr/local/bin/python

# Description of Types of Vars
# int   = 7 -4 0 9875
# float = 4.5 0.0876 -15.499 7,0
# bool  = true false
# str   = 'Ola ' '7.5' ''

print('==== Validate Var Type with saying')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('1o valor é ',type(n1))
sum=n1+n2
print('A soma entre ',n1,'e',n2,'é',sum)

print('==== How printing in an advanced way / from python 3. Before it was with percent')
print('A soma é {}'.format(sum))
print('A soma entre {} e {} é {}'.format(n1,n2,sum))

# print(n1.isnumeric()) doesn't work