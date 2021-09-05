#!/usr/bin/python

#If an import is not found execute: pip install <module_name>
#pip install emoji
import emoji 

print(emoji.emojize("Ola Mundo 🌎"))
print(emoji.emojize("Ola Mundo :earth_americas:",use_aliases=True)) # Use_aliases to convert from cheat sheet