#!/usr/bin/python

frase='Curso em Video Python'
# All characters has an index starting from 0
print(frase)

# Spliting
# frase = "Curso em V i d e o   P y t h o n"
#          01234567891011121314151617181920
print(frase[9]) #V
print('from-to (except last character)')
print(frase[9:13]) #Vide
print('jumping')
print(frase[9:21:2]) #VdoPto
print('from beginin up-to select OR from until latest')
print(frase[:5]) #Curso
print(frase[15:]) #Python
print(frase[8::3]) # d tn

# Evaluating Strings:
# comprimento
len(frase) #21
# How much of an character
frase.count('P') #1
# Counting from to
frase.count('P',0,13) #0
# How much expression
frase.find('deo') #11 #if not found, returns -1, else returns index
'Curso'in frase #True # Returns true or false
# Replace string
frase.replace('Python','Android') #'Curso em Video Android'
# Caps
frase.upper()       #'CURSO EM VIDEO PYTHON'
frase.lower()       #'curso em video python'
frase.capitalize()  #'Curso em video python'    # Lower all and only the first update to upper
frase.title()       #'Curso Em Video Python'    # Capitalize first letter of all words
# Removing extra spaces at begining or end
frase.strip()       #'Curso em Video Python'
frase.rstrip()      #'Curso em Video Python' # Only from the right
frase.lstrip()      #'Curso em Video Python' # Only from the left

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
print(frase.upper().count('O'))     #3
print(frase.lower().find('video'))  #9
# total of characters without spaces
print(len(frase.strip()))           #21

# Strings are imutable
frase[0] = 'J' #Error - str object does not support item assignment
#You can use replace
print(frase.replace('Python','Android')) # it does not update variable / object. To that
frase = frase.replace('Python','Android')