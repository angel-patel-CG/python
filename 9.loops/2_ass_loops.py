# #1
# for i in range(5):
#     print("Hello")

# #2
# for i in range(1,10):
#     print(i, end=" ")

# #3
# for i in range(1,11):
#     print(i, end=" ")


# #6
# for i in range(2,20):
#     if i%2==0:
#         print(f"{i} is Even")


# #7
# for i in range(1,19):
#     if i%2==1:
#         print(f"{i} is Odd")

# #8

# for i in range(1,20):
#     if i%3 == 0:
#         print(i)

# #9

# for i in range(20,1,-1):
#     if i%2 == 0:
#         print(i)


# #10

# number = int(input("enter a number:"))

# for i in  range(1,number+1):
#         print(i)


# #11

# number = int(input("enter a number:"))

# for i in  range(1,number+1):
#     if i%2 == 0:
#         print(i)


# #12

# number = int(input("enter a number:"))

# for i in  range(1,number+1):
#     if i%2 != 0:
#         print(i)


# #13

# number = int(input("enter a number:"))

# for i in  range(1,number+1):
#     if i%3 == 0:
#         print(i)


# #14

# number = int(input("enter a number:"))

# for i in  range(1,number+1):
#     if i%3 == 0 and i%2 == 0 :
#         print(i)


# #15

# number = int(input("enter a number:"))
# even = 0

# for i in  range(1,number+1):
#     if i%2 == 0:
#         even += 1
# print(f"Total even numbers are {even}")


# #16


# number = int(input("enter a number:"))
# sum = 0

# for i in  range(1,number+1):
#     sum += i
# print(f"Total sum is {sum}")


# #17

# number = int(input("enter a number:"))
# sum = 0

# for i in  range(1,number+1):
#     if i%2 == 0:
#         sum += i
# print(f"Total sum of even numbers are {sum}")


# #18

# number = int(input("enter a number:"))
# sum = 0

# for i in  range(1,number+1):
#     if i%2 != 0:
#         sum += i
# print(f"Total sum of odd numbers are {sum}")


# #19


# number = int(input("enter a number:"))
# product = 1

# for i in  range(1,number+1):
#     product *= i
# print(f"Total product is {product}")


# #20

# string = input("enter your word:").strip()
# length = len(string)

# for i in range (0,length):
#     print(string[i])


# #21

# string = input("enter your word:").strip()
# length = len(string)

# for i in range (0,length):
#     print(string[i], end=" ")


# #22

# string = input("enter your word:").strip()
# length = 0

# for character in string:
#     length += 1

# print("Number of characters:", length)


# #23

# string = input("enter your word:").strip().lower()
# length = 0

# for character in string:
#     if character== "a":
#         length += 1

# print("Number of characters:", length)


# #24


# string = input("Enter your word: ").strip()

# count = 0

# for character in string:
#     if character.isupper():
#         count += 1

# print("Number of uppercase characters:", count)


# #26

# for i in range(3):
#     print("*", end="")
#     for j in range(4):
#         print("*", end="")
#     print()


# #27

# for i in range(4):
#     print("*", end="")
#     for j in range(5):
#         print("*", end="")
#     print()


# #28

# for i in range(0,5):
#     print("*", end="")
#     for j in range(0,i):
#         print("*", end="")
#     print()


# #29

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()


# #30

# num = int(input("enter a number: "))

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()
