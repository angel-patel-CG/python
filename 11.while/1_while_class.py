#1

# i=1
# while i<=10:
#         print(f

#2

# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1


#3

# i = 10

# while i >= 0:
#     print(i)
#     i = i - 1

# # 4

# number = int(input("Enter a number: "))

# while number != 0:
#     print("You entered:", number)
#     number = int(input("Enter a number: "))

# print("Loop ended")

# #5

# number = int(input("Enter a number: "))

# total = 0

# while number != 0:
#     total = total + number
#     number = int(input("Enter a number: "))

# print("Sum:", total)


# # #6

# number = input("Enter a password: ").strip()

# while number != "Angel#1234":
#     print("Invalid password!!")
#     number = input("Enter a password: ").strip()

# print("Your password is correct,login successful!!")



#7

# string = input("enter your text: ")

# while string != string[::-1]:
#     print("This word in not a palindrome")
#     string = input("enter your text: ")

# print(f"Your text is palindrome: {string} ")


#orrrrrrrrrrrr


# string= input("enter a string: ").lower().strip()

# string2 = ""

# i = len(string)-1

# while i >= 0:

#     string2 = string2 + string[i]
#     i = i - 1

# if string == string2:
#     print("string is palindrome")

# else :
#     print("string is not palindrome")



#orrrrrrrrrrrrrrrrrrrrrrr  twoooooooo pointeeeeerrrrrrr meeeeeeethhhooooddddddddd

# string= input("enter a string: ").lower().strip()

# i = 0
# j = len(string) -1
# flag = True

# while(i<j):

#     if string[i] == string[j]:
#         i+=1
#         j-=1

#     else:
#         flag = False
#         i = j #to break the loop

# if flag:
#     print("Given string is palindrome!!")
# else:
#     print("Given string is Not a palindrome!!")


#8

# num = int(input("Enter a number => "))

# while num > 0:
#     digit = num % 10
#     print(digit)
#     num = num // 10

#9         similar to 8  reverse a numberrrrrrrrrrrrrrrrrrrrrrrrrrrr

# number = int(input("Enter a number: "))

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10

# print("Reverse:", reverse)


#10

# number = int(input("Enter a number: "))

# total = 0

# while number > 0:
#     digit = number % 10
#     total = total + digit
#     number = number // 10

# print("Sum => ", total)
    

# #11 infinite looopppp

# i = 1

# while i <= 5:
#     print(i)
    

# #12 infinite to finite looppp conversion

# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1


# #13 another infinite loooppp 

# i = 10

# while i > 0:
#     print(i)
#     i = i + 1


# # 14 another infinite looop convert to finite looppp

# i = 10

# while i > 0:
#     print(i)
#     i = i - 1

# #15 nested whileee loooopppp

# row = 1

# while row <= 3:
#     column = 1

#     while column <= 4:
#         print("*", end=" ")
#         column = column + 1

#     print()
#     row = row + 1


# #16 num patternssssssssss

# row = 1

# while row <= 4:
#     column = 1

#     while column <= row:
#         print(column, end="")
#         column = column + 1

#     print()
#     row = row + 1



# #17 reverse num pattern 

# i = 5

# while i >= 1:
#     j = 5

#     while j >= 6-i:
#         print(j,end=" ")
#         j = j - 1

#     print()
#     i = i - 1






