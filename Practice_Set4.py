# Chapter 4 – Practice Set
# 1.Write a program to store seven fruits in a list entered by the user.
# 2.Write a program to accept the marks of 6 students and display them in a sorted manner.
# 3.Check that a tuple cannot be changed in Python.
# 4.Write a program to sum a list with 4 numbers.
# 5.Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)

# ----------------------******************************-----------------------------------------

#Owner :- Rohit Patil
#Company :- MARK
#Created Date :- 10-Feb-2022
#Updated Date :-


# 1.Write a program to store seven fruits in a list entered by the user.

# Solution -->
# I

# a=[]
# i=1
# while i<=7:
#     b=input('Enter the fruit name:-')
#     a.append(b)
#     i+=1
# print(f'List of fruits:-{a}',type(a))


# II
# a=[]
# for i in range(0,7):
#     b = input('Enter the fruit name:-')
#     a.append(b)

# print(a,type(a))

# 2.Write a program to accept the marks of 6 students and display them in a sorted manner.
# Solution -->

# # I

# f=[]
# a=1
# while a<=6:
#       b=(input('Enter the student Name:-'),int(input()))
#       f.append(b)
#       a+=1

# def sortSecond(val):
#     return val[1]
# f.sort(key = sortSecond, reverse=True)
# for n in range(0,6):
#     print(f[n])


# 4.Write a program to sum a list with 4 numbers.
# Solution -->
# I
# l=[1,2,3,4]
# sum=l[0] + l[1] +l[2] +l[3]
# print(sum)

# II
# l=[10,20,40,50,30]
# print(sum(l))
# b=l.sort()
# print(l)

# III
# a=[8,6,9,5]
# for n in a :
#      print(a[a.index(n)])
# sum = 0
# for n in a:
#     sum = sum + n
# print(sum)

# IV
# a=[]
# sum = 0
# for n in range(4):
#     b = int(input('Enter the number:-'))
#     a.append(b)
# for n in a:
#     sum = sum + n
#     addition = sum
# print(addition)



# 5.Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
# Solution-->
# I
# a=(7, 0, 8, 0, 0, 9)
# print(f'Number of zero Count in tuple:-{a.count(0)}')


# def sortSecond(val):
#     return val[1]
# a=[['Rohit',55],['Madhuri',85],['Rajveer',95],['Saee',45]]
# # b=sorted(a,key=int)
# a.sort(key = sortSecond)
# print(a)

# 1.Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide the user with an option to look it up!


# 6.Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. 
# Assume that the names are unique.

# a={}
# i=1
# while i<=4:
#       b=input('Enter the friend name:-')
#       c=input('Enter the language name:-')
#       a[b]=c
#       i+=1
# print(a,type(a))
# print(a.keys())

# def simplefunction():
#       print('Welcome to Credence')

# simplefunction()


# 2.Write a program to input eight numbers from the user and display all the unique numbers (once).

a=[]
i=1
while i<=8:
      b=int(input('Enter the values:-'))
      a.append(b)
      i+=1
c=set(a)
print(f'Display all unique numbers:{c},{type(c)}')