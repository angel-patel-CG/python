# #  1

# marks = int(input("Enter your marks: "))
# while marks<=0 or marks>=100:
#     marks = int(input("Enter your marks: "))
# print("Accepted marks:", marks)    



# #  2

# integer = int(input ("Enter your marks:"))
# while integer<=0:
#     integer = int(input ("Enter your marks:"))
# print("Accepted marks:", integer)    



# #  3

# age= int(input ("Enter your age:"))
# while age<=0 or age>=120:
#     print("This is invalid input")
#     age = int(input ("Enter your age:"))
# print("Accepted age:", age)  



# #  4

# while True:
#     print("1. View profile")
#     print("2. Edit profile")
#     print("3. Settings")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     match choice:
#         case 1:
#             print("View profile")
#             break
#         case 2:
#             print("Edit profile")
#             break
#         case 3:
#             print("Settings")
#             break
#         case 4:
#             print("Exit")
#             break
#         case _:
#             print("Invalid choice. Try again.")



# #  5

# password= input ("Enter your password:").strip() 
# while len(password)<8:
#     print("Password must contain at least 8 characters")
#     password = input("Enter password: ").strip()
  
# print("Password accepted")           

# #  6

# temp= float(input ("Enter your Temperature:"))
# while temp<=-20 or temp>=45:
#     print("This is invalid input")
#     temp = float(input ("Enter your temperature:"))
# print("Valid temperature")  



# #  7

# balance = 5000

# amount = float(input("Enter withdrawal amount: "))

# while amount <= 0 or amount > balance:
#     print("Invalid amount. Try again.")
#     amount = float(input("Enter withdrawal amount: "))

# balance = balance - amount

# print("Remaining balance: ", balance)



# #  8

# username = input("Enter username: ").strip()

# while len(username) < 5 or " " in username:
#     print("Invalid username. Try again.")
#     username = input("Enter username: ").strip()

# print("Accepted username:", username)



# #  9

# number = int(input("Enter a positive integer: "))

# while number <= 0 or number % 3 != 0 or number % 5 != 0:
#     print("Invalid number. Try again.")
#     number = int(input("Enter a positive integer: "))

# print("Accepted number:", number)

# # Que 10
# pin = 2468
# attempts = 1

# while attempts <= 3:
#     entered_pin = int(input("Enter PIN: "))

#     if entered_pin == pin:
#         print("Access granted")
#         break
#     else:
#         print("Incorrect PIN")
#         attempts = attempts + 1

# if attempts > 3:
#     print("Access denied")



# #  11
    
# number = int(input("Enter a number between 10 and 50: "))

# while number < 10 or number > 50:
#     print("Invalid number. Try again.")
#     number = int(input("Enter a number between 10 and 50: "))

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")



# #  12  

# balance = 2000

# amount = float(input("Enter deposit amount: "))

# while amount <= 0:
#     print("Invalid amount. Enter a positive amount.")
#     amount = float(input("Enter deposit amount: "))

# balance = balance + amount

# print("New balance: ", balance)     



# #  13

# number = int(input("Enter an integer between 1 and 100: "))

# while number < 1 or number > 100:
#     print("Invalid number. Try again.")
#     number = int(input("Enter an integer between 1 and 100: "))

# print("Accepted number:", number)



# #  14

# marks = int(input("Enter marks (0-100): "))

# while marks < 0 or marks > 100:
#     print("Invalid marks. Try again.")
#     marks = int(input("Enter marks (0-100): "))

# if marks >= 75:
#     print("Distinction")
# elif marks >= 60:
#     print("First Class")
# elif marks >= 35:
#     print("Pass")
# else:
#     print("Fail")



# #  15  
   
# username = input("Enter username: ").strip()
# password = input("Enter password: ")

# while len(username) < 5 or " " in username or len(password) < 8 or password.strip() == "":
#     print("Invalid username or password. Try again.")

#     username = input("Enter username: ").strip()
#     password = input("Enter password: ")

# print("Registration successful!")
# # Que 16
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")

# while operator != "+" and operator != "-" and operator != "*" and operator != "/":
#     print("Invalid operator. Try again.")
#     operator = input("Enter operator (+, -, *, /): ")

# num2 = float(input("Enter second number: "))

# while operator == "/" and num2 == 0:
#     print("Division by zero is not allowed.")
#     num2 = float(input("Enter second number: "))

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# else:
#     result = num1 / num2

# print("Result:", result) 



# #  17

# balance = 10000

# while True:
#     print("1. Check balance")
#     print("2. Deposit money")
#     print("3. Withdraw money")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         print("Balance: ₹", balance)

#     elif choice == "2":
#         amount = float(input("Enter deposit amount: "))

#         if amount > 0:
#             balance = balance + amount
#             print("Deposit successful")
#             print("Balance: ₹", balance)
#         else:
#             print("Amount must be greater than zero")

#     elif choice == "3":
#         amount = float(input("Enter withdrawal amount: "))

#         if amount > 0 and amount <= balance:
#             balance = balance - amount
#             print("Withdrawal successful")
#             print("Balance: ₹", balance)
#         else:
#             print("Invalid withdrawal amount")

#     elif choice == "4":
#         print("Thank you for using our bank")
#         break

#     else:
#         print("Invalid menu choice")



# #  18

# month = int(input("Enter month (1-12): "))

# while month < 1 or month > 12:
#     print("Invalid month")
#     month = int(input("Enter month (1-12): "))

# day = int(input("Enter day (1-31): "))

# while day < 1 or day > 31:
#     print("Invalid day")
#     day = int(input("Enter day (1-31): "))

# print("Valid month and day")



# #  19

# quantity = int(input("Enter quantity: "))

# while quantity <= 0:
#     print("Quantity must be positive")
#     quantity = int(input("Enter quantity: "))

# price = float(input("Enter unit price: "))

# while price <= 0:
#     print("Price must be greater than zero")
#     price = float(input("Enter unit price: "))

# total = quantity * price

# print("Total cost: ₹", total)



# #  20

# count = int(input("How many numbers (1-20)? "))

# while count < 1 or count > 20:
#     print("Invalid count")
#     count = int(input("How many numbers (1-20)? "))

# total = 0
# i = 1

# while i <= count:
#     number = float(input("Enter a number: "))
#     total = total + number
#     i = i + 1

# average = total / count

# print("Average:", average)



# #  21

# while True:
#     password = input("Enter password: ")

#     upper = False
#     lower = False
#     digit = False
#     space = False

#     for ch in password:
#         if ch.isupper():
#             upper = True
#         if ch.islower():
#             lower = True
#         if ch.isdigit():
#             digit = True
#         if ch.isspace():
#             space = True

#     valid = True

#     if len(password) < 8:
#         print("Password must have at least 8 characters")
#         valid = False

#     if not upper:
#         print("Password needs an uppercase letter")
#         valid = False

#     if not lower:
#         print("Password needs a lowercase letter")
#         valid = False

#     if not digit:
#         print("Password needs a digit")
#         valid = False

#     if space:
#         print("Password must not contain whitespace")
#         valid = False

#     if valid:
#         print("Password accepted")
#         break



# #  22

# number = int(input("Enter an integer (1-10): "))

# while number < 1 or number > 10:
#     print("Invalid number")
#     number = int(input("Enter an integer (1-10): "))

# print("Valid number:", number)



# #  23

# score1 = float(input("Enter score 1: "))

# while score1 < 0 or score1 > 100:
#     print("Invalid score")
#     score1 = float(input("Enter score 1: "))

# score2 = float(input("Enter score 2: "))

# while score2 < 0 or score2 > 100:
#     print("Invalid score")
#     score2 = float(input("Enter score 2: "))

# score3 = float(input("Enter score 3: "))

# while score3 < 0 or score3 > 100:
#     print("Invalid score")
#     score3 = float(input("Enter score 3: "))

# total = score1 + score2 + score3
# average = total / 3

# print("Total:", total)
# print("Average:", average)



# #  24

# balance = 10000

# amount = int(input("Enter withdrawal amount: ₹"))

# while amount <= 0 or amount > balance or amount % 100 != 0:
#     print("Invalid amount")
#     print("Amount must be positive, within balance,")
#     print("and a multiple of ₹100")
#     amount = int(input("Enter withdrawal amount: ₹"))

# balance = balance - amount

# print("Withdrawn amount: ₹", amount)
# print("Remaining balance: ₹", balance)