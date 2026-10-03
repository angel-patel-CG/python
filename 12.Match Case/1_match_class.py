# #1

# operation = 1

# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter a num2: "))

# while operation != 0:

#     operation  = int(input(" 0.Exit \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n Enter a number to perform operation :"))

#     match operation :
#         case 0:
#             print("")
#         case 1:
#             print("Add: " , num1 + num2)
#         case 2:
#             print("Subtract: " , num1 - num2)
#         case 3:
#             print("Multiply: " , num1 * num2)
#         case 4:
#            if num2 != 0:
#                print("Divide: " , num1 / num2)  
#         case _:
#             print("Invalid Choice")

# print("Exit")



# #0rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr


# operation = 1

# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter a num2: "))

# while True:

#     operation  = int(input(" 0.Exit \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n Enter a number to perform operation :"))

#     match operation :
#         case 0:
#             break
#         case 1:
#             print("Add: " , num1 + num2)
#         case 2:
#             print("Subtract: " , num1 - num2)
#         case 3:
#             print("Multiply: " , num1 * num2)
#         case 4:
#            if num2 != 0:
#                print("Divide: " , num1 / num2)             
#         case _:
#             print("Invalid Choice")

# print("Exit")


# #orrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

# operation = 1

# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter a num2: "))

# flag = True

# while flag:

#     operation  = int(input(" 0.Exit \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n Enter a number to perform operation :"))

#     match operation :
#         case 0:
#             flag = False
#         case 1:
#             print("Add: " , num1 + num2)
#         case 2:
#             print("Subtract: " , num1 - num2)
#         case 3:
#             print("Multiply: " , num1 * num2)
#         case 4:
#             if num2 != 0:
#                 print("Divide: " , num1 / num2)
#         case _:
#             print("Invalid Choice")

# print("Exit")





# #2

# operation = 1

# while operation != 0:

#     num = int(input("Enter a number: "))

#     operation  = int(input(" 0.Exit \n 1.PRIME \n 2.EVEN \n 3.ODD \n Enter a number to perform operation :"))

#     match operation :
#         case 0:
#             print("")
#         case 1:
#             prime = True

#             for i in range (2,num):

#                 if num%(i) == 0 :
#                     prime = False

#             if prime:
#                 print("Given number is a PRIME NUMBER")
#             else:
#                 print("Gien number is not a PRIME NUMBER ")

#         case 2:
#             if num%2 ==0 :
#                 print("Given number is a EVEN NUMBER")
#         case 3:
#             if num%2 != 0:
#                 print("Given number is a ODD NUMBER")
#         case _:
#             print("Invalid Choice")

# print("Exit")




# #3

# marks = int(input("Enter your marks: "))

# match marks:
#     case x if x >= 90:
#         print("A")
#     case x if x >= 75:
#         print("B")
#     case x if x >= 60:
#         print("C")
#     case x if x >= 40:
#         print("D")
#     case _:
#         print("Fail")



# #4 

# day = int(input("Enter a day number: "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")            
#     case 6 | 7:
#         print("Weekend")    
#     case _:
#         print("Invalid Day")



