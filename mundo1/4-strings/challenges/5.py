#!/usr/bin/python

word = "A"
print("""Create a program that reads a sentence and tells:
- How much times word '{}' appears
- Which position it appears for the first time
- Which position it appears the last time 
""".format(word))

sentense = str(input("Enter a sentence to be evaluated: ")).strip().upper()

print("The word '{}' appears: {} times".format(word,sentense.count(word)))

print("Appears at position '{}' for the FIRST time".format(sentense.find(word)+1))
print("Appears at position '{}' for the LAST time".format(sentense.rfind(word)+1))
