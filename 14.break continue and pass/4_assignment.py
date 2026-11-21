# #challenge 1

# i = 1

# while i != 0:

#     i = int(input("Enter your number: "))

#     if i > 0:
#         print(i)
#     elif i < 0:
#         continue
#     elif i == 0:
#         break


# #challenge 2

# numbers = [12, 5, -4, 18, 0, 25, 30]

# for char in numbers:

#     if char > 0:
#         print(char)
#     elif char < 0:
#         continue
#     elif char == 0:
#         break



# #challenge 3

# numbers = [12, 5, -4, 18, 0, 25, 30]

# i = int(input("Find your number: "))
# for char in numbers:

#     if char == i:
#         print("Number Found")
#         break
# else:
#     print("Number not found")




###------------------------------------------------------------------------------------------------------------


# #1

# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")

# #1,2,3,4,Finished


# #2

# word = "skyline"

# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)

# #skyl


# #3

# n = 2

# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2


# #2 4 6


# #4

# limit = int(input("Enter a Limit: "))

# for i in range(1,limit):
#     if i == 7:
#         break
#     print(i)


# #5

# string = input("enter your value:").strip().lower()

# target = input("enter your target latter: ").strip().lower()

# for char in string:
#     if char == target:
#         break
#     print(char)



# #6

# numbers = input("Enter your numbers: ").split( " ")

# for char in numbers:
#     if int(char) < 0:
#         break
#     print(int(char))


# #7

# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)

# #(1,1);(1,2);(2,1);(2,2);(3,1);(3,2)


# #8

# numbers = input("Enter your sentence: ").split( " ").lower()
# target = input("Enter your target word:").lower()

# for char in numbers:
#     if char == target:
#         break
#     print(char)



# #9

# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)

# # 1 2 3 5 6


# #10

# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")

# #dctn


# #11

# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# # 1 2 4 5


# #12

# limit = int(input("Enter limit: "))

# for i in range (1,limit):
#     if i%3==0:
#         continue
#     print(i)


# #13

# numbers = input("Enter your word: ").lower()
# target = input("Enter your target character:").lower()

# for char in numbers:
#     if char == target:
#         continue
#     print(char)


#14

# marks = list(map(int, input("Enter marks separated by spaces: ").split()))

# for mark in marks:
#     if mark < 40:
#         continue
#     print(mark)

#15
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)

# output:A1 B1 A3 B3 A4 B4

#16
# n = 1

# while n <= 5:
#     if n == 3:
#         n+=1
#         continue
#     print(n)
#     n += 1

# output: 1 2 4 5


# 17
# count=0
# word = input("Enter any word here:")
# for char in word:
#     if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
#         count+=1   
#         continue
# print(char,end="")
# print(count)



#18
# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")


# output: 1 2 3 Done


#19
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")

# output: 1 3 4 completed



#20
# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")

# outside: 1 2 outside loop

# #21
# for item in []:
#     print("Inside")
# else:
#     print("Else block")
# output:else block

# #22
# numbers = list(map(int, input("Enter any number: ").split()))
# target = int(input("Enter your target number: "))
# for num in numbers:
#     if num == target:
#         print("Found")
#         break
# else:
#     print("Not found")

# #23
# text = input("Input any character:")
# target = input("Input your target:")

# for char in text:
#     if char == target:
#         print("Character exists")
#         break
# else:
#     print("Character missing")


#24
# n = int(input("Enter any number:"))

# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")


#25
# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# output:All are even

#26
# for x in range(3):
#     continue
# else:
#     print("A")

# output:A

# #26
# for x in range(3):
#     break
# else:
#     print("B")
# output:--

#26
# for x in range(0):
#     print(x)
# else:
#     print("C")
# output:C

#27
# count=0
# string=input("Enter your string here:")
# for char in string:
#     if char == "a":
#         print(char)
#         break
# print(count)

#28
# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)
# output: 2 3 

#29
# x = 10

# if x > 5:
#     pass

# print("Finished")

# output:Finished

#30
# for letter in "cat":
#     pass

# print("Loop ended")
# output: cat

#31