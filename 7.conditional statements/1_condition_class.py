 # age = 20

# if age >= 18:
#     print("You are an adult.")

##practical for movie ticket booking

# age = int(input("Enter your age: ").split()[0])

# gender = input("Enter your gender (Male/Female): ").split()[0]

# gender = gender.lower().strip()

# print(f"Age: {age}, Gender: {gender}")

# if age >= 18 :

#     if gender == "male":
#         print("seat is unavailable .")

#     if gender == "female":
#         print("seat is available for you.")

# else:
#         print("Invalid age. You must be 18 or older to check seat availability.")

# #practical for login page 

# username = input("Enter your username: ").strip().lower()
# password = input("Enter your password: ").strip()

# if username == "angell.1716" and password == "password123":
#     print("Login successful.")
# else:
#     print("Invalid username or password.")

# #create a bank account with a minimum balance of 1000 and check if the user can withdraw money or not

# balance = 1000
# withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

# if withdrawal_amount <= balance:
#     print("Withdrawal successful.")
#     balance -= withdrawal_amount
#     print(f"Remaining balance: ${balance}")
# else:
#     print("Insufficient funds.")

# #elif learning 

# marks = int(input("enter marks:"))

# if marks>=90 :
#     print("A")
# elif marks >= 60 :
#     print("B")
# else:
#     print("better luck  next time")


## calculator

number_1 = int(input("enter number 1 :"))
number_2 = int(input("enter number 2 :"))

print (" 1.addition  2.substraction  3.multiplication  4.devision  5.floordevision")

operation = input( "what do you want to perform,enter number or name of operation: ").lower().strip()

if operation == "addition" or operation== str(1) :
    print(f"addition is : {number_1+number_2}")
elif operation == "substraction" or operation == str(2) :
    print(f"substraction is : {number_1-number_2}")
elif operation == "multiplication" or operation == str(3) :
    print(f"multiplication is : {number_1*number_2}")
elif operation == "devision " or operation == str(4) :
    print(f"devision is : {number_1/number_2}")
elif operation == "fllordevision" or operation == str(5) :
    print(f"floordevision is : {number_1//number_2}")
else:
    print("invalid operation")