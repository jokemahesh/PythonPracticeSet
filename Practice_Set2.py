# Practice program set 2:

# 1.Write a python program to print the contents of a directory using os module.Search online for the function which does that.
# 2.Install an external module and use it to perform an operation of your interest.(e.g. play MP3 audio)  
# 3.Write a Python program to add two numbers.
# 4.Write a Python program to find the remainder when a number is divided by Z(Integer).
# 5.Check the type of the variable assigned using the input() function.
# 6.Use a comparison operator to find out whether a given variable a is greater than b or not.(Take a=34 and b=80)
# 7.Write a Python program to find the average of two numbers entered by the user.
# 8.Write a Python program to calculate the square of a number entered by the user.


#-------------------------**************--------------------------------------------------------------------------------

# 1.Write a python program to print the contents of a directory using os module.Search online for the function which does that.

# Solution--->
# import os
# print('Current Directory:-',os.getcwd())

# print('Content of Directory:-',os.listdir())

# 2.Install an external module and use it to perform an operation of your interest.(e.g. play MP3 audio) 

# from playsound import playsound

# playsound('F:\Songs\WhatsApp Audio 2022-02-02 at 18.32.38.mpeg')

# 3.Write a Python program to add two numbers.

# Solution --->

# I.Simple Method
# Num1=10
# Num2=20
# print("Addition of two numbers:-",(Num1+Num2))

# II.By using input function
# Num1=eval(input("Enter the first number:-"))
# Num2=eval(input("Enter the second number:-"))
# result=(Num1+Num2)
# print("Addition of two Numbers:-",result)

# 4.Write a Python program to find the remainder when a number is divided by Z(Integer).

# Solution --->

# Simple Method
# 1

# By using input function
# Num1=eval(input("Enter the Dividend:-"))
# Num2=eval(input("Enter the Divisor:-"))
# Result=Num1%Num2
# print("Remainder:-",Result)

# 5.Check the type of the variable assigned using the input() function.

# Solution --->

# a= input("Enter the Variable:-")
# a=int(a)
# print("Type of the Variable:-",type(a))


# 6.Use a comparison operator to find out whether a given variable a is greater than b or not.(Take a=34 and b=80)

# Solution -->
# # I
# a=34
# b=80
# print(f"a is greater than b:{a>b}")

# # II
# a=34
# b=80
# if a>b:
#     print("a is greater than b")

# else:
#     print("a is lesser than b")

# 7.Write a Python program to find the average of two numbers entered by the user.
# Solution -->

# a= int(input("Enter the value1:-"))
# b= int(input("Enter the value2:-"))
# print("Average of two numbers:-",(a+b)/2)


# 8.Write a Python program to calculate the square of a number entered by the user.
# Solution -->
# I
aSquare = int(input("Enter the number:-"))
b=aSquare**2
print(f"Square of number:{b}")

# II
aSquare = int(input("Enter the number:-"))
b=aSquare*aSquare
print(f"Square of number:{b}")