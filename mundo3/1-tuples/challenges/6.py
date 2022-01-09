#!/usr/bin/python
print ("""077
tuple with multiples words and then shows the vogals for each word 
""")

words = (str(input("Enter a word: ")).upper(),str(input("Enter a word: ")).upper(),str(input("Enter a word: ")).upper(),
        str(input("Enter a word: ")).upper(),str(input("Enter a word: ")).upper(),)
# vowels tuple
vowels = ('A', 'E', 'I', 'O', 'I', 'U')

for word in words:
    print(f"\nIn word {word} vowels are: ",end="")
    for c in word:
        if c in "AEIOU":
            print(c,end=" ")
