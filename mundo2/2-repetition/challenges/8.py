#!/usr/bin/python
print ("""
Read a sentense and say if it is a palindrome, discarting spaces
ex: APOS A SOPA
A SACADA DA CASA 
A TORRE DA DERROTA 
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
""")

sentence = str(input("Enter a sentence to check if it is a palindrome ")).strip().upper()
words=sentence.split()
togheter="".join(words)
inverse = ""

for i in range(len(togheter) -1, -1, -1):
    inverse += togheter[i]
# OR
# inverse = [::-1]
print(inverse," ", togheter)
if inverse == togheter: 
    print("Your sentense IS a Palindrome")
else:
    print("Your sentense is NOT Palindrome")