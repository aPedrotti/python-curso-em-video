#!/usr/bin/python

frase='Curso em Video Python'
# All characters has an index starting from 0
print(frase)

# Spliting
# Curso em V i d e o   P y t h o n
# 01234567891011121314151617181920
print(frase[9])
print('from-to (except last character)')
print(frase[9:13])
print('jumping')
print(frase[9:21:2])
print('from beginin up-to select OR from until latest')
print(frase[:5])
print(frase[15:])
print(frase[8::3])

# Evaluating Strings:
# comprimento
len(frase)
# How much of an character
frase.count('P')
# Counting from to
frase.count('P',0,13)
# How much expression
frase.find('deo') #if not found, returns -1, else returns index
'Curso'in frase # Returns true or false
# Replace string
frase.replace('Python','Android')
# Caps
frase.upper()
frase.lower()
frase.capitalize()  # Lower all and only the first update to upper
frase.title()       # Capitalize first letter of all words
# Removing extra spaces at begining or end
frase.strip()
frase.rstrip()      # Only from the right
frase.lstrip()      # Only from the left

# Spliting
frase.split()           # Remove spaces and update indexes. Create a list for words
print(frase.split())
dividido = frase.split()
print(dividido[0])      # Returns the first word
print(dividido[2][3])   # Returns de fourth char of third word
# Update spaces with a charactere
'-'.join(frase)

# Printing big texts
print(""" This is an example of big
text that requires breaking lines""")

# Example combining methods in object
print(frase.upper().count('O'))
print(frase.lower().find('video')) 
# total of characters without spaces
print(len(frase.strip()))

# Strings are imutable
frase[0] = 'J' #Error - str object does not support item assignment
#You can use replace
print(frase.replace('Python','Android')) # it does not update variable / object. To that
frase = frase.replace('Python','Android')