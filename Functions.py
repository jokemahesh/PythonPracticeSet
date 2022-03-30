
# def getfactorial(a:int):
#     if a == 1 or a == 0:
#         return  1
#     else:
#         return a * getfactorial(a-1)

# print(getfactorial(5))


a =  int(input("Enter the number:-"))
fact = 1
for n in range(a,1,-1):
    fact = n * fact
print(fact)