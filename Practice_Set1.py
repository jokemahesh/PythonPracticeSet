# Practice program set 1:

# 1. Write a program to print * or # pattern in python.
# #
# ##
# ###
# ####
# #####
#  
# 2. Use REPL and print the table of 10 using it.
# 3. Label the program written in problem 4 with comments.

#-----------------------*****************----------------------

#Owner :- Rohit Patil
#Company :- MARK
#Created Date :- 06-Feb-2022
#Updated Date :-

# 1. Write a program to print * or # pattern in python.
# #
# ##
# ###
# ####
# #####
#Solution --->

# I.Simple Method
# print("#")
# print("##")
# print("###")
# print("####")
# print("#####")

# II. By using for loop

# for a in range(1,6,1):
#     print(a*'#')

# III. By using while loop
# i=1
# while i<=5:
#     print(i*"#")
#     i=i+1

# 2. Use REPL and print the table of 10 using it.
#
# Solution--->

# I.Simple Method 
# a=10
# print('10*1=',a*1)
# print('10*2=',a*2)
# print('10*3=',a*3)
# print('10*4=',a*4)
# print('10*5=',a*5)
# print('10*6=',a*6)
# print('10*7=',a*7)
# print('10*8=',a*8)
# print('10*9=',a*9)
# print('10*10=',a*10)

# II.By using for loop

for a in range(1,11,1):
    print('10*',a,'=',10*a)