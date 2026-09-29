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

#9

number = int(input("Enter a number: "))

total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum => ", total)
    








