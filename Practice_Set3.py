# Practice program set 3:

# 1.Write a program to detect double spaces in a string. (count of double space or count of any char)
# 2.Write a program to format the following letter using escape sequence characters.
# [Dear  Candidate, 
# 	We are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.
# Thank you,
# HR]
# 3.From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function
# 4.Replace the double spaces from problem 3 with single spaces.

# -----------------------------*********************------------------------------------------------------- 

# 1.Write a program to detect double spaces in a string. (count of double space or count of any char)

# Solution --->

# I.
# a= "Wel come"
# b=a.count(' ')
# print(b)

# II.
# a= "Rajveer"
# b=  a.count('R',-7,-1)
# print(b)


# 2.Write a program to format the following letter using escape sequence characters.

# Solution -->

a=("Dear Candidate,\n\tWe are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.\nThank you,\nHR")
print(a)

# 3.From above solution (2) replace ‘Candidate’ with your name and HR name with some other name. By using some string operation function

# Solution

a=("Dear  Candidate,\n\tWe are delight to inform you that you have cleared all rounds of interview and we are extending offer to join us.\nThank you,\nHR")
b=a.replace('Candidate','Rohit A. Patil')
b=b.replace('HR','Mahesh Joke')
print(b)


# 4.Replace the double spaces from problem 3 with single spaces.

c=b.replace('  ',' ')
print(c)