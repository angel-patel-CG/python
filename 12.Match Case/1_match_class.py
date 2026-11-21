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



# #5

# num = 1

# while num != 0:
#     num = int(input(" 1 for English \n 2 for Hindi \n 3 for Gujarati \n 0 for Exit \n select a number : "))

#     match num:
#         case 1:
#             print("Hello,Can you please tell me what Yproblem You are facing? ")
#             num1 = int(input("1 for network issue \n 2 for software issue \n 3 for hardware issue \n 0 for Exit \n select a number : "))
#             match num1:
#                 case 1: 
#                     print("For Network issue restart your router and check the cables. If the problem persists, contact your Internet Service Provider.")
#                 case 2:
#                     print("For Software issue, try reinstalling the software or updating it to the latest version. If the problem persists, contact the software vendor for support.")
#                 case 3:
#                     print("For Hardware issue, check if the device is properly connected and powered on. If the problem persists, contact the manufacturer or a certified technician for assistance.")
#                 case 0:
#                     print("Exit")
#                 case _:
#                     print("Invalid Choice")
#         case 2:
#             print("Namaste, kya aap mujhe bata sakte hain ki aapko kis samasya ka samna karna pad raha hai?")
#             num2 = int(input("1 network samasya ke liye \n 2 software samasya ke liye \n 3 hardware samasya ke liye \n 0 exit ke liye \n number chune : "))
#             match num2:
#                 case 1:
#                     print("Network samasya ke liye, apne router ko restart karein aur cables ko check karein. Agar samasya bani rahe, to apne Internet Service Provider se sampark karein.")
#                 case 2: 
#                     print("Software samasya ke liye, software ko reinstall karein ya ise latest version mein update karein. Agar samasya bani rahe, to software vendor se support ke liye sampark karein.")
#                 case 3:
#                     print("Hardware samasya ke liye, device ko properly connected aur powered on check karein. Agar samasya bani rahe, to manufacturer ya certified technician se assistance ke liye sampark karein.")
#                 case 0:
#                     print("Exit")
#                 case _:
#                     print("Invalid Choice")
#         case 3:
#             print("Namaste, tamne shu samasya chhe te mane kahi sako chho?")
#             num3 = int(input("1 network samasya mate \n 2 software samasya mate \n 3 hardware samasya mate \n 0 exit mate \n number pasand karo : "))
#             match num3:
#                 case 1:
#                     print("Network samasya mate, tamara router ne restart karo ane cables ne check karo. Jo samasya chalu rahe, to tamara Internet Service Provider sathe sampark karo.")
#                 case 2:
#                     print("Software samasya mate, software ne reinstall karo ke latest version ma update karo. Jo samasya chalu rahe, to software vendor sathe support mate sampark karo.")
#                 case 3:
#                     print("Hardware samasya mate, device ne properly connected ane powered on check karo. Jo samasya chalu rahe, to manufacturer ke certified technician sathe assistance mate sampark karo.")
#                 case 0:
#                     print("Exit")
#                 case _:
#                     print("Invalid Choice")
#         case 0:
#             print("Exit")
#         case _:
#             print("Invalid Choice")

