# Practice Program Set :- 6

# 1.Write a program to find the greatest of four numbers entered by the user.
# 2.Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.
# 3.A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
# 4.Write a program to find whether a given username contains less than 10 characters or not.
# 5.Write a program that finds out whether a given name is present in a list or not.
# 6.Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100  Ex
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F
# 7.Write a program to find out whether a given post is talking about “Harry” or not.



# --------------------------*************************-----------------------------------

# Owner :- Rohit A. Patil
# Company :- MARK
# Created Date :- 14-Feb-2022
# Updated Date :- 


# 1.Write a program to find the greatest of four numbers entered by the user.

# Solution -->

# I
# a=[]
# for n in range(4):
#     b=int(input('Enter the number:-'))
#     a.append(b)
# if a[0]>=a[1] and a[0]>=a[2] and a[0]>=a[3]:
#     print(a[0])
# elif a[1]>=a[0] and a[1]>=a[2] and a[1]>=a[3]:
#     print(a[1])
# elif a[2]>=a[0] and a[2]>=a[1] and a[2]>=a[2]:
#     print(a[2])
# elif a[3]>=a[0] and a[3]>=a[1] and a[3]>=a[2]:
#     print(a[3])
# else:
#     print('All numbers are same')

# ----------------------**************************-----------------------------

# II
# a=[]
# for n in range(4):
#     b=int(input('Enter the number:-'))
#     a.append(b)
# print(f'Largest number is :{max(a)}')

# ----------------****************************--------------------------
# III 

# a=[]
# for n in range(4):
#     b = int(input('Enter the number:-'))
#     a.append(b)
# max = a[0]
# for n in a:
#     if n > max:
#         max = n
# print(max)

# ----------------------***************------------------



# 2.Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.

# Solution -->

# I   
# a=[]

# for n in range(1):
#     b = int(input('Subject Name Physics\nMarks:-'))
#     a.append(b)
#     c = int(input('Subject Name Chemistry\nMarks:-'))
#     a.append(c)
#     d = int(input('Subjetc Name Mathematics\nMarks:-'))
#     a.append(d)

# Total = sum(a)
# Average = Total/len(a)
# print('Average :-',Average)

# if a[0] > 33:
#     if a[1] > 33:
#         if a[2] > 33:
#             if Average >= 40:
#                 print('PASS')
#             else:
#                 print('FAIL')
#         else:
#             print('FAIL')
#     else:
#         print('FAIL')
# else:
#     print('FAIL')


# a=[]

# for n in range(3):
#     e = input('Enter the Student Name :-')
#     b = int(input('Subject Name Physics\nMarks:-'))
#     a.append(b)
#     c = int(input('Subject Name Chemistry\nMarks:-'))
#     a.append(c)
#     d = int(input('Subjetc Name Mathematics\nMarks:-'))
#     a.append(d)
    
#     Total = sum(a)
#     Average = Total/len(a)
#     print('Average :-',Average)

#     if a[0] > 33:
#         if a[1] > 33:
#             if a[2] > 33:
#                 if Average >= 40:
#                    print('PASS')
#                 else:
#                     print('FAIL')
#             else:
#                 print('FAIL')
#         else:
#             print('FAIL')
#     else:
#         print('FAIL')


# 3.A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# a = input('Enter the message:-')

# if 'make a lot of money'  in a or 'buy now' in a or 'subscribe this' in a or 'click this' in a:
#     print('spam')
# # if 'buy now' in a:
# #     print('spam')
# # if 'subscribe this' in a :
# #     print('spam')
# # if 'click this' in a:
# #     print('spam')
# else:
#     print(a)

    
# elif 'buy now' in a :
#     print('spam')
# elif 'subscribe this':
#     print('spam')
# elif 'click this' in a:
#     print('spam')
# else:
#     print(a)

# 4.Write a program to find whether a given username contains less than 10 characters or not.

# a = input('Enter the username :-')

# if len(a)>10:
#     print('Username contains more than 10 character')
# else:
#     print(a)


# 5.Write a program that finds out whether a given name is present in a list or not.


# 6.Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100  Ex
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F

# a = input('Enter the student name:')
# b = int(input('Enter the marks:'))

# if b > 90 and b < 100 :
#     print('Grade - Ex')
# elif b > 80 and b < 90:
#     print('Grade - A')
# elif b > 70 and b < 80:
#     print('Grade - B')
# elif b > 60 and b < 70:
#      print('Grade - C')
# elif b > 50 and b < 60:
#     print('Grade - D')
# elif b < 50:
#     print('Grade - F')
# else:
#     print('Student is Absent')

# 7.Write a program to find out whether a given post is talking about “Harry” or not.

# a = input('Enter the post :-')

# if 'Harry' in a:
#     print('The given post is talking about "Harry"')