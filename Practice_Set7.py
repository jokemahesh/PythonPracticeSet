# Chapter 7 – Practice Set

# 1.Write a program to print the multiplication table of a given number using for loop.
# 2.Write a program to greet all the person names stored in a list l1 and which starts with S.
# l1 = [“Harry”, “Sohan”, “Sachin”, “Rahul”]
# Copy
# 3.Attempt problem 1 using a while loop.
# 4.Write a program to find whether a given number is prime or not.
# 5.Write a program to find the sum of first n natural numbers using a while loop.
# 6.Write a program to calculate the factorial of a given number using for loop.
# 7.Write a program to print the following star pattern.
#     *

#   ***  

# ***** for n=3
# Copy
# 8.Write a program to print the following star pattern:
# *

# **

# *** for n = 3
# Copy
# 9.Write a program to print the following star pattern:
# * * *
# *   *             #For n=3
# * * * 
# Copy
# 10. Write a program to print the multiplication table of n using for loop in reversed order.

# --------------------------*************************-----------------------------------

# Owner :- Rohit A. Patil
# Company :- MARK
# Created Date :- 14-Feb-2022
# Updated Date :- 

# 1.Write a program to print the multiplication table of a given number using for loop.

# a = int(input('Enter the number:-'))

# for n in range(1,11):
#     print(a,'*',n,'=',a*n)

# 2.Write a program to greet all the person names stored in a list l1 and which starts with S.
# l1 = [“Harry”, “Sohan”, “Sachin”, “Rahul”]

# Solution -->

# I.
# a = ['Harry', 'Sohan', 'Sachin', 'Rahul']
# b = a[0]
# c = a[1] 
# d = a[2] 
# e = a[3]

# if b[0] == 'S':
#     print(b)
# if c[0] == 'S':
#     print(c)
# if d[0] == 'S':
#     print(d)
# if e[0] == 'S':
#     print(e)

# II
# a = ['Harry', 'Sohan', 'Sachin', 'Rahul']

# sublist = 0

# for n in range(4):
#     sublist = a[n]
#     if sublist[0] == 'S':
#         print(sublist)


# 3.Attempt problem 1 using a while loop.

# Solution -->

# a = int(input('Enter the number :-'))
# i = 1
# while i <= 10:
#     print(a,'*',i,'=',a*i)
#     i+=1
        

# 4.Write a program to find whether a given number is prime or not.

# Solution -->

# a = int(input('Enter the number:-')
# # for n in range(2,int(a/2)+1):
#     if (a % n) == 0:
#        print('This is not a prime number:-',a)
#        break
# else: 
#     print('This is a prime number:-',a)

# 5.Write a program to find the sum of first n natural numbers using a while loop.

# Solution -->

# a = int(input('Enter the natural number :-'))
# i = 0
# b = 0
# while i <= a:
#     b = b+i
#     i+=1
# print(b)

# 6.Write a program to calculate the factorial of a given number using for loop.

# Solution -->

# 7.Write a program to print the following star pattern.
#     *

#   ***  

# ***** for n=3
# Copy

# Solution -->

for n in range(6):
    # print(n*'*')
    if n == 1:
        print(n*'    *')
    elif n == 3:
        print(' ',n*'*')
    elif n == 5:
        print(n*'*')


# 8.Write a program to print the following star pattern:
# *

# **

# *** for n = 3
# Copy

# Solution -->

# for n in range(4):
#     print(n*'*')


# 9.Write a program to print the following star pattern:
# * * *
# *   *             #For n=3
# * * * 

# Solution -->


# for n in range(1,4):
#     if n == 1:
#         print(3*n*'* ')
#     if n == 2:
#         print(n*'*   ')
#     if n == 3:
#         print(n*'* ')
    
    
# 10. Write a program to print the multiplication table of n using for loop in reversed order.

# Solution -->

# a = int(input('Enter the number :-'))
# for n in range(10,0,-1):
#     print(a,'*',n,'=',a*n)


# def factorial(n : int):
#     print(type(n))
#     print(n)

# num = 'Hello'
# factorial(num)


# num = 10
# divisor = int(input('Enter the divisor:-'))
# Division = (num/divisor)

# try:
#     print(Division)
# except Exception as e:
#     print("Excepation Occured:",e) 








