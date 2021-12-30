#!/usr/bin/python

word = "SANTO"
print("""Create a program that reads a city name and tells if 
start with word '{}'
""".format(word))

city = str(input('Enter a name of a city from Brasil: ')).strip()

city = city.upper()
ocurrence = city.count(word)

print("City you've enter has {} ocurrence of the word '{}' ".format(ocurrence,word))
if ocurrence > 0:
    print("Does start with {}? {}".format(word,city[:5] == word))