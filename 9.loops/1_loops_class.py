# #1

# for i in range(1,10):
#     print(i, end=(" "))


# #2

# for i in range(1,20):
#     if i%2==0:
#         print(f"{i} is even!!") 

# #3

# for leap_year in range(2000, 2030):
#     if leap_year%4==0:
#         print(f"{leap_year} is leap year")

# #4

# start= int(input("enter a starting number: "))
# end= int(input("enter a ending number: "))

# for i in range(start,end):
#     if i%2==0:
#         print(f"{i} is even!!")

# #5

# total = 0

# for i in range(1,11):
#     total= total + i
#     print(total)

# #6




# string=input("enter a string: ").strip().lower()

# string2 = ""


# length = len(string)

# for element in range (length-1,-1,-1):

#     string2 = string2 + string[element]

# if string == string2:
#     print("string is palindrom")

# else :
#     print("string is not palindrom")


# # 7

# total = 0

# for i in range(1, 6):
#     total = total + i

# print(total)

# #8 method 

# name = "Aeish"

# for character in name:
#     print(character)

# #9 tradition method

# name = "Aeish"

# length = len(name)

# for element in range (0,length):
#     print(name[element])

# #10

# word = "banana"

# count = 0

# for character in word:
#     if character == "a":
#         count = count + 1

# print("Count:", count)

# #11


# word = "banana"

# length = len(word)

# count = 0

# for character in range (0,length):

#     i = word[character]

#     if i == "a":
#         count = count + 1

# print("Count:", count)


#12

# i = 0
# j = 0

# for i in range(3):
#     i = i + 0
#     for j in range(2):
#         j = j + 0

#     print(i, j)

# #13

# for row in range(4):
#     for column in range(5):
#         print("*", end=" ")
#     print()

# 14

# for row in range(1,11):
#     for column in range(1, row+1):
#        print("*", end=" ")
#     print()
            
#15

# for row in range(5):
#     print("#",end= " ")
#     for column in range(5):
#         print("*",end= " ")
#     print()


######15

# va = ["maths","science","english","hindi","social science"]

# for i in range(len(va)):
#     print(f"{i+1}.{va[i]}")
   

    
#16

# for i in range(1,5):
#     print("*"*i)

#17

# for i in range(4,0,-1):
#     print("*"*i)

#18


# for row in range(1,6):  
#     for column in range(1, row+1):   
#         print(column,end="")
#     print()

#19

# for i in range(0,5):
#     for j in range(0,5-i):
#         print(" ",end=" ")
#     for k in range(0, i +1):
#         print("*",end=" ")
#     print()  

#20

# for i in range(5,-1,-1):
#     for j in range(5-i, 0, -1):
#         print(" ",end=" ")
#     for k in range(i+1,0,-1):
#         print("*",end=" ")
#     print()  



# #21

# for i in range(5):
#     print("*           *")
# for j in range(5):
#     print("*", end="  ")
# print()  

#orrrrrrrrrrrrr

num = int(input("enter number:"))

for i in range(1,num+1):
    for j in range(1,num+1):

        if j==1 or i==num or j==num:
                print("*",end=" ")   
        elif  i == num/2 and j == num/2:
            print("*",end=" ") 
        else:
             print("", end="  ") 
    print()
