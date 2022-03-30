
# from googletrans import Translator

# Translator = Translator()

# out=Translator.translate("I love paython ",dest='mr')

# # print(out.text)


# 1.Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide the user with an option to look it up!

from fnmatch import translate
from googletrans import Translator

Translator = Translator()

out=Translator.translate("Rohit",dest='mr')
In=Translator.translate(out,dest='en')

print(out.text)
print(In.text)

# EnglishDictionary ={
#                      out: 
     
#                     }
# print(out)