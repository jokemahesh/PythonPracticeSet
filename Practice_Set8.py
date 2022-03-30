# Chapter 8 – Practice Set

# 1.Write a program using the function to find the greatest of three numbers.
# 2.Write a python program using the function to convert Celsius to Fahrenheit.
# 3.How do you prevent a python print() function to print a new line at the end?
# 4.Write a recursive function to calculate the sum of first n natural numbers.
# 5.Write a python function to print the first n lines of the following pattern.
# ***

# **       #For n = 3

# *
# Copy
# 6.Write a python function that converts inches to cms.
# 7.Write a python function to remove a given word from a list and strip it at the same time.
# 8.Write a python function to print the multiplication table of a given number.
# Project 1: Snake, Water, Gun Game
# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a Python program capable of playing this game with the user.


# --------------------------*************************-----------------------------------

# Owner :- Rohit A. Patil
# Company :- MARK
# Created Date :- 19-Feb-2022
# Updated Date :-

# 1.Write a program using the function to find the greatest of three numbers.

# a = [10, 11, 2, 5, 6, 90, 75, 85]
# d = []
# for n in range(3):
#     b = a.index(max(a))
#     c = a.pop(b)
#     d.append(c)
# print(d)

# def printgreatestNumber (val):
#     list(val)
#     e = val.copy()
#     d = []
#     for n in range(3):
#         b = e.index(max(e))
#         c = e.pop(b)
#         d.append(c)
#     for n in range(3):
#         print(d[n],end = ' ')

# a = [58,96,23,56,63,78,63,26,56]
# print(a)
# printgreatestNumber(a)


# 2.Write a python program using the function to convert Celsius to Fahrenheit.

# def printCtoF(c):
#     f = (c * (9/5)) + 32
#     b=round(f,3)
#     print(b)

# a = eval(input('Enter the temperature in degree Celsius :-'))
# printCtoF(a)

# 3.How do you prevent a python print() function to print a new line at the end?

# def printatend(val):
#     print(val, end = ' ')
    
    
# printatend('Rohit')
# printatend('Patil')

# 5.Write a python function to print the first n lines of the following pattern.
# ***

# **       #For n = 3

# *

# Solution -->

def printstar(val):
    for n in range(val,0,-1):
        print(n*'*')
    for n in  range(2,val+1):
        print(n*'*')

# printstar()

# 6.Write a python function that converts inches to cms.

# Solution -->

# def conInctoCms(val):
#     cms = val/0.39370
#     print(cms)

# conInctoCms(12)

# 8.Write a python function to print the multiplication table of a given number.

# Solution -->

# def printtable(val):
#     for n in range(1,11):
#         print(val,'*',n,'=',val*n)

# printtable(5)
# printtable(12)
# def printstar(val):
#     for n in range(val,0,-1):
#         if n == 10:
#             print(n*'*')
#         if n == 4:
#             print(n*'*','',n*'*')
#         if n == 3:
#             print(n*'*','  ',n*'*')
#         if n == 2:
#             print(n*'*','    ',n*'*')
#         if n == 1:
#             print(n*'*','      ',n*'*')
#     for n in range(1,val+1):
#         if n == 1:
#             print(n*'*','      ',n*'*')
#         if n == 2:
#             print(n*'*','    ',n*'*')
#         if n == 3:
#             print(n*'*','  ',n*'*')
#         if n == 4:
#             print(n*'*','',n*'*')
#         if n == 10:
#             print(n*'*')

printstar(5)
   