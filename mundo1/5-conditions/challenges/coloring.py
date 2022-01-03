#!/usr/bin/python


print("ANSI Escape")
print('Format: \\033[style;text;backmYourText')
print('\033[0;33;44mANSI Escape\033[m\n')

print("""Style:
0 - None
1 - Bold
4 - Underline
7 - Negative
""")

print("""Text:
30 - White
31 - Red
32 - Green
33 - yellow
34 - Blue medium
35 - Purple
36 - Blue Soft
37 - Gray
""")

print("""Bagrounds:
40 - White
41 - Red
42 - Green
43 - yellow
44 - Blue medium
45 - Purple
46 - Blue Soft
47 - Gray
""")

print('For more you have to import other libraries')


print('\033[0;30;41mHello World!\033[m')
print('\033[4;33;44mHello World!\033[m')
print('\033[1;35;43mHello World!\033[m')
print('\033[30;42mHello World!\033[m')
print('\033[mHello World as it is!')
print('\033[7;30mHello World!\033[m')

a=3
b=5
print('Mixturing for values like \033[1;40;42m{}\033[m and \033[1;34;40m{}\033[m !!!'.format(a,b))
print('You can place your colors into the format: ')
name = "Andre"
print("Nice to meet you {}{}{} !!! ".format('\033[1;34m', name, '\033[m'))

print('You can place your colours into variables:')
colours = {'clean':'\033[m',
        'white':'\033[7m',
        'warning':'\033[0;30;43m',
        'alert':'\033[0;30;41m',
        'blacknwhite':'\033[;30;40m'}

print("Nice to meet you {}{}{} !!! ".format(colours['white'], name, colours['clean']))