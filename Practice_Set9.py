# Chapter 9 – Practice Set
# 1.Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.
# 2.The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.
# 3.Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13- year old boy.
# 4.A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.
# 5.Repeat program 4 for a list of such words to be censored.
# 6.Write a program to mine a log file and find out whether it contains ‘python’.
# 7.Write a program to find out the line number where python is present from question 6.
# 8.Write a program to make a copy of a text file “this.txt.”
# 9.Write a program to find out whether a file is identical and matches the content of another file.
# 10.Write a program to wipe out the contents of a file using python.
# 11.Write a python program to rename a file to “renamed_by_python.txt.”

# --------------------------*************************-----------------------------------

# Owner :- Rohit A. Patil
# Company :- MARK
# Created Date :- 22-02-2022
# Updated Date :-


# 1.Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.

# poem = open("F:\Automation Testing\poem.txt",'r')
# contentpoem = poem.read()
# if 'Twinkle' in contentpoem:
#     print('Poem :-',contentpoem)
# else:
#     print('Twinkle Word Not Present in poem')
# poem.close()


# 2.The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.

# def game(val : int):
#     game_score = open("F:\Automation Testing\Hiscore.txt",'r')
#     hi_score =  game_score.read()
#     hi_score = int(hi_score)
#     game_score.close()

#     print('My_Score :',val)

#     if val > hi_score:
#         game_score = open("F:\Automation Testing\Hiscore.txt",'w')
#         new_game_score = game_score.write(str(val))
#         # hi_score1 = game_score.read()
#         print('Highest_Score: ', val)
#         game_score.close()
#     else:
#         print('Highest_Score: ',hi_score)
         
    
    
# game(150)

# a = '10'
# b = int(a)
# print(b,type(b))


# 3.Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13- year old boy.




# for n in range(2,21):
#     a = open(f"F:\Automation Testing\For 13-year old boy\Tableof{n}.txt",'r+')
#     num = n
#     for multi in range(1,11):
#         b = str(num,'*', multi, '=', num*multi)
#         # c = str(b)
#         multiplication = a.write(b)
#     # print(a.read())
#             # a.close()
#     # c = a.read()
# a.close()
#     # print(c)    

# 4.A file contains the word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.

# # replacedonkeyto = '######'
# replacedonkey = open("F:\Automation Testing\Donkey.txt",'r+')
# beforereplace = replacedonkey.read()
# # print(beforereplace)
# if 'Donkey'in beforereplace:
#     d=beforereplace.replace('Donkey',"######")
#     replacedonkey = open("F:\Automation Testing\Donkey.txt",'r+')
#     afterreplace = replacedonkey.write(d)   
#     beforereplace = replacedonkey.read()
#     print(beforereplace)
# else:
#     print(beforereplace)
# print(beforereplace)
# replacedonkey.close()


#  5.Repeat program 4 for a list of such words to be censored.


# listofcensorwords = ['Shit','Donkey','Swear']

# a = open('F:\Automation Testing\Listofcensore.txt','r+')
# b = a.read()

# for n in range(3):
#     if listofcensorwords[n] in b:
#         a = open('F:\Automation Testing\Listofcensore.txt','w')
#         b = b.replace(listofcensorwords[n],'*****')
#         a.write(b)
         
#     else:
#         print('Censor word not present')
        
# a.close()

   
a = open("F:\Automation Testing\Donkey.txt",'r')
b = a.readlines()
print(b)
c = b.index('python\n')+1
print(c)


# a = ['Rohit','PAtil','python']
# b = a.index('python')
# print(b)

# aList = [1, 2, 4, 5, 6, 7, 8, 9, 10]
# print(aList)
# a = aList[0]
# # aList[0] = aList[-1]
# # aList[-1] = a
# # print(aList)

# for n in range(9):
#     aList[n] = aList[-1-n]
# aList[-1] = a
# print(aList)

# for n in range(1,101):
#     print(f"Square of first {n} numbers :{n**2}")

# normal_List = [[1,2,3],[4,5,6],[7,8,9,10]]
# flat_LIst = [item for sublist in normal_List for item in sublist ]
# print(normal_List)
# print(flat_LIst)
    