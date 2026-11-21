#1
# num = int(input("Enter the number of the item you want to order:"))
# match num:
#     case 1:
#         print("ordered a Pizza")

#     case 2:
#         print("ordered a Burger")
#     case 3:
#         print("ordered a Sandwich")
#     case 4:
#         print("ordered a Pasta")
#     case _:
#         print("Invalid item number")

#2
# num = int(input("Enter the number of the setting you want to change:"))
# match num:
#     case 1:
#         print("You have changed the wi-fi settings")

#     case 2:
#         print("You have changed the bluetooth settings")
#     case 3:
#         print("You have changed the mobiledata settings")
#     case 4:
#         print("You have changed the airplanemode settings")
#     case 5:
#         print("exit")
#     case _:
#         print("Invalid setting number")

#3
# menu=int(input("Enter the number of the ATM menu task you want to perform:"))
# match menu:
#     case 1:
#         print("Check Balance")
#     case 2:
#         print(" Withdraw Money")
#     case 3:
#         print("Deposit Money")
#     case 4:
#         print("Change PIN")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid menu number")

#4
# colour = input("Enter the colour of the traffic light:")
# match colour:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Get Ready")
#     case "green":
#         print("Go")
#     case _:
#         print("Invalid colour")


#5
# num = int(input("Enter the number of menu you want to select: "))
# match num:
#     case 1:
#         print("VIEW PROFILE")
#     case 2:
#         print("VIEW COURCES")
#     case 3:
#         print("VIEW RESULTS")
#     case 4:
#         print("VIEW ATTENDANCE")
#     case 5:
#         print("VIEW LOGOUT")
#     case _:
#         print("Invalid menu number")


#6
# menu = int(input("Enter the number of the menu you want to select: "))
# match menu:
#     case 1:
#         print("Electronics")
#     case 2:
#         print("Clothing")
#     case 3:
#         print("Books")
#     case 4:
#         print("Grocery")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid menu number")

#7
# num = int(input("Enter the number of the item you want to order:"))
# match num:
#     case 1:
#         print("YAccount Balance")
#     case 2:
#         print("Mini Statement")
#     case 3:
#         print("Fund Transfer")
#     case 4:
#         print("Bill Payment")
#     case 5:
#         print("Customer Support")
#     case _:
#         print("Invalid item number")

#8
# num = int(input("Enter the number of the operation you want to perform:"))
# match num:
#     case 1:
#         print("Morning Show")
#     case 2:
#         print("Afternoon Show")
#     case 3:
#         print("Evening Show")
#     case 4:
#         print("Night Show")
#     case _:
#         print("Invalid operation number")

# #Q1

# print("Our Menu \n1==> Pizza\n2==> Burger\n3==> Pasta\n4==> Sandwich")
# num = int(input("Enter your choice: "))

# match num:
#     case 1:
#         print("You selected Pizza")
#     case 2:
#         print("You selected Burger")
#     case 3:
#         print("You selected Pasta")
#     case 4:
#         print("You selected Sandwich")
#     case _ :
#         print("Invalid Input")

# #Q2

# print("1 ==> Wif - Fi\n2 ==> Bluetooth\n3 ==> Mobile Data\n4 ==> Airplane Mode\n5 ==> Exit")
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Wi - Fi selected")
#     case 2:
#         print("Bluetooth selected")
#     case 3:
#         print("Mobile data selected")
#     case 4:
#         print("airplane mode selected")
#     case 5:
#         print("Exited!")
#     case _:
#         print("Invalid Input")

# #Q3

# print("\t1 ==> Check Balance\n\t2 ==> Withdraw Money\n\t3 ==> Deposit Money\n\t4 ==> Change PIN\n\t5 ==> Exit")
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Checking Balance")
#     case 2:
#         print("Withdrawing Money")
#     case 3:
#         print("Depositing Money")
#     case 4:
#         print("Changing PIN")
#     case 5:
#         print("Exited!")
#     case _:
#         print("Inavlid Input")

# #Q4

# ligth = input("Enter the colour of Ligth at signal: ").lower()

# match ligth:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _ :
#         print("Invalid Input")

# #Q5

# numb = 1
# while numb != 5:

#     print("\t1 ==> View Profile\n\t2 ==> View Courses \n\t3 ==> View Marks\n\t4 ==> View Attendance\n\t5 ==> Logout")

#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Your Profile:")
#         case 2:
#             print("Courses:")
#         case 3:
#             print("Your Marks:")
#         case 4:
#             print("Your Attendance")
#         case 5:
#             print("Logged Out")
#         case _ :
#             print("Invalid Input")

# #Q6

# print("\t1 ==> Electronics \n\t2 ==> Clothing\n\t3 ==> Books\n\t4 ==> Grocery\n\t5 ==> Exit")
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Electronics")
#     case 2:
#         print("Clothing")
#     case 3:
#         print("Books")
#     case 4:
#         print("Grocery")
#     case 5:
#         print("Exited!")

# #Q7

# numb = 1
# while numb != 6:

#     print("\t1 ==>Account Balance\n\t2 ==> Mini Statement \n\t3 ==> Fund Transfer\n\t4 ==> Bill Payment\n\t5 ==> Customer Support\n\t6 ==> Exit")

#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Balance:")
#         case 2:
#             print("Mini Statement:")
#         case 3:
#             print("Fund Transfer:")
#         case 4:
#             print("Bill Payments")
#         case 5:
#             print("Customer Support")
#         case 6:
#             print("Exited!")
#         case _ :
#             print("Invalid Input")

# #Q8

# numb = 1
# while numb != 5:

#     print("\t1 ==> Morning Show\n\t2 ==> Afternoon Show \n\t3 ==> Evening Show\n\t4 ==> Nigth Show\n\t5 ==> Exit")

#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Morning Show Details are as follows:")
#         case 2:
#             print("Afternoon Show Details are as follows:")
#         case 3:
#             print("Evening Show Details are as follows:")
#         case 4:
#             print("Night Show Details are as follows:")
#         case 5:
#             print("Exited!")
#         case _ :
#             print("Invalid Input")

# #Q9

# print("\t1 ==> Sunny \n\t2 ==> Rainy\n\t3 ==> Cloudy\n\t4 ==> Snowy")
# numb = int(input("Enter your Weather: "))

# match numb:
#     case 1:
#         print("Wear Sunglasses")
#     case 2:
#         print("Carry an Umbrella")
#     case 3:
#         print("Weather may Change")
#     case 4:
#         print("Wear warm clothes")
#     case _:
#         print("Unkown Weather")

# #Q10

# print("\t1 ==> UPI \n\t2 ==> Card\n\t3 ==> Cash\n\t4 ==> Wallet")
# numb = int(input("Enter your Payment method: "))

# match numb:
#     case 1:
#         print("UPI Payment selected")
#     case 2:
#         print("Card Payment selected")
#     case 3:
#         print("Cash Payment selected")
#     case 4:
#         print("Wallet Payment selected")
#     case _:
#         print("Invalid Payment method ")

# #Q11

# print("\t1 ==> pdf -> Document \n\t2 ==> jpg -> Image\n\t3 ==> png -> Image\n\t4 ==> mp3 -> Audio\n\t5 ==> mp4 -> Video")
# numb = int(input("Enter Extension: "))

# match numb:
#     case 1:
#         print("Document File")
#     case 2:
#         print("Image File")
#     case 3:
#         print("Image File")
#     case 4:
#         print("Audio File")
#     case 5:
#         print("Video File")
#     case _:
#         print("Unknown File Type")

# #Q12

# print("\t1 ==> Admin \n\t2 ==> Teacher\n\t3 ==> Student\n\t4 ==> Guest")
# numb = int(input("Enter your role: "))

# match numb:
#     case 1:
#         print("Full Access")
#     case 2:
#         print("Teacher Dashboard")
#     case 3:
#         print("Student Dashboard")
#     case 4:
#         print("Limited Access")
#     case _:
#         print("Unkown Role")

#Q13

# day_number=int(input("Enter the Day Number: "))

# match day_number:
#     case 1 | 2 | 3 | 4 | 5 :
#         print("Weekday")
#     case 6 | 7 :
#         print("Weekend")
#     case _ :
#         print("Invalid Day")

# #Q14

# print("\t1 ==> Low \n\t2 ==> Medium\n\t3 ==> High\n\t4 ==> Critical")
# numb = int(input("Enter priority number: "))

# match numb:
#     case 1 | 2:
#         print("Normal")
#     case 3 | 4:
#         print("Urgent")
#     case _:
#         print("Unkown Priority number")

#Q15

# print("\t1 ==> Bronze \n\t2 ==> Silver\n\t3 ==> Gold\n\t4 ==> Platinium")
# numb = int(input("Enter Your Membership Level: "))

# match numb:
#     case 1 | 2:
#         print("Basic Membership")
#     case 3 | 4:
#         print("Premium Membership")
#     case _:
#         print("Unkown Membership Level")   


# Q16

# account = input("Enter your account type:-").strip().lower()
# choice = int(input("Enter your choice number:-"))

# match account:

#     case "student":

#         match choice:
#             case 1:
#                 print("View Courses")
#             case 2:
#                 print("View Marks")
#             case 3:
#                 print("View Attendance")
#             case _:
#                 print("Invalid Choice")

#     case "teacher":

#         match choice:
#             case 1:
#                 print("View Students")
#             case 2:
#                 print("Enter Marks")
#             case _:
#                 print("Invalid Choice")

#     case _:
#         print("Invalid Account Type")


# Q17

# account = input("Enter your account type:-").strip().lower()
# choice=int(input("Enter your choice number:-"))

# match account:
#     case "savings":


#         match choice:
#             case 1: 
#                 print("Check Balance")
#             case 2:
#                 print("Deposit")
#             case 3:
#                 print("Withdraw")


#     case "current":


#         match choice:
#             case 1:
#                 print("Check Balance")
#             case 2:
#                 print("Deposit")
#             case 3:
#                 print("Withdraw")

#     case _:
#         print("Invalid Account type")                                            


# Q18

# category = input("Enter your category:-").strip().lower()
# choice=int(input("Enter your choice number:-"))
# match category:
#     case "electronics":
#         match choice:
#             case 1:
#                 print("Mobile")
#             case 2:
#                 print("Laptop")
#             case 3:
#                 print("Headphones")
#     case "clothing":
#         match choice:
#             case 1:
#                 print("Shirt")
#             case 2:
#                 print("Jeans")
#             case 3:
#                 print("Shoes")
#     case _:
#         print("Invalid category")   

#Q19


# category = int(input("Enter category: "))
# food = int(input("Enter food: "))

# match category:
#     case 1:
#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")

#     case 2:
#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")

#     case _:
#         print("Invalid Category")  

#Q20

# print("\t1 ==> Addition \n\t2 ==> Subtraction\n\t3 ==> Multiplication\n\t4 ==> Division\n\t5 ==> Floor Division")
# number=int(input("Enter your choice number:-"))
# a=int(input("Enter your first integer:-"))
# b=int(input("Enter your 2nd integer:-")) 
# match number:
#     case 1:
#         print(f"Addition is {a+b}")
#     case 2:
#         print(f"Subtraction is {a-b}")          
#     case 3:
#         print(f"Multiplication is {a*b}")
#     case 4:
#         print(f"Division is {a/b}")
#     case 5:
#         print(f"Floor Division is {a//b}")
#     case _:
#         print("Invalid choice number")




#Q21


# print("\t1 ==> Celcius to Fahrenheit \n\t2 ==> Fahrenheit to Celsius")
# choice=int(input("Enter your choice number:-"))   
# temp=int(input("Enter your temperature:-"))

# match choice:
#     case 1:
#         fahrenheit = (temp * 9/5) + 32
#         print(f"{temp}°C is equal to {fahrenheit}°F")


#     case 2:
#         celsius = (temp - 32) * 5/9
#         print(f"{temp}°F is equal to {celsius}°C")

#     case _:
#         print("Invalid choice number") 




#Q22   

# print("1 ==> Kilometers to meters \n 2==> Meters to Kilometers \n 3==> Kilograms to Grams \n 4==> Grams to Kilograms") 

# choice=int(input("Enter your choice number:-")) 
# num=int(input("Enter your value:-"))

# match choice:
#     case 1:
#         meters = num*1000 
#         print(f"{num} kms  is equal to {meters} meters") 
#     case 2:
#         kilometers=num/1000
#         print(f"{num} meters is equal to {kilometers} kms") 
#     case 3:
#         grams=num*1000
#         print(f"{num} kilograms is equal to {grams} grams.")
#     case 4:
#         kilograms=num/1000
#         print(f"{num} grams is equal to {kilograms} kgs.") 
#     case _:
#         print("Invalid choice number") 



# Q23

# Account_type=input("Enter your account type:-").strip().lower() 
# amount=int(input("Enter your amount:-"))

# match Account_type:
#     case "savings": 
#         if amount>0:
#             print("Withdrawal Request Accepted") 
#         else:
#             print("Invalid amount") 
#     case "current":
#         if amount>0:
#             print("Withdrawal request Accepted")
#         else:
#             print("Invalid Amount") 
#     case _:
#         print("Invalid CAccount Type")




# Q24] 

# print(" 1 ==> Start Exam \n 2==> View Result \n 3 ==> Exit")
# choice=int(input("Enter your choice Number:-"))
# age=int(input("Enter your age:-"))

# match choice:
#     case 1:
#         if age>=18:
#             print("You can start the exam")
#         else:
#             print("You are under threshold age")
#     case 2:
#         print("You can see your result")
#     case 3:
#         print("Exam ended")
#     case _:
#         print("Invalid choice number")               
    


#Q25]
# print(" 1 ==> Regular \n 2 ==> Premium \n 3 ==> VIP  ")

# ticket_type = int(input("Enter ticket type: "))
# age = int(input("Enter your age: "))
# match ticket_type:
#     case 1:
#         if age<=5:
#          print("Free Ticket")
#         else:
#             print("Your selected ticket type is ", ticket_type)
#     case 2:
#         if age<=5:
#             print("Free Ticket")
#         else:
#             print("Your selected ticket type is ", ticket_type)
#     case 3:
#          if age<=5:
#                      print("Free Ticket")
#          else:
#                      print("Your selected ticket type is ", ticket_type)
#     case _:
#        print("Invalid ticket type") 



# Q26]

# print("1 → Light\n2 → Fan\n3 → AC\n4 → TV")

# choice = int(input("Enter device: "))

# match choice:
#     case 1:
#         print("Light Controller Opened")
#     case 2:
#         print("Fan Controller Opened")
#     case 3:
#         print("AC Controller Opened")
#     case 4:
#         print("TV Controller Opened")
#     case _:
#         print("Invalid Device")



# Q27]

# print("1 → General Medicine\n2 → Cardiology\n3 → Orthopedics\n4 → Pediatrics\n5 → Emergency")

# choice = int(input("Enter department: "))

# match choice:
#     case 1:
#         print("General Medicine Selected")
#     case 2:
#         print("Cardiology Selected")
#     case 3:
#         print("Orthopedics Selected")
#     case 4:
#         print("Pediatrics Selected")
#     case 5:
#         print("Emergency Selected")
#     case _:
#         print("Invalid Department")


# Q28]

# print("1 → Book Ticket\n2 → Cancel Ticket\n3 → Check PNR\n4 → Train Schedule\n5 → Exit")

# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Book Ticket Selected")
#     case 2:
#         print("Cancel Ticket Selected")
#     case 3:
#         print("Check PNR Selected")
#     case 4:
#         print("Train Schedule Selected")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# Q29]

# print("1 → Search Book\n2 → Issue Book\n3 → Return Book\n4 → View Issued Books\n5 → Exit")

# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Search Book Selected")
#     case 2:
#         print("Issue Book Selected")
#     case 3:
#         print("Return Book Selected")
#     case 4:
#         print("View Issued Books Selected")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")



# Q30]

# print("placed\nconfirmed\npreparing\nout_for_delivery\ndelivered\ncancelled")

# status = input("Enter status: ").strip().lower()

# match status:
#     case "placed":
#         print("Your order has been placed")
#     case "confirmed":
#         print("Your order has been confirmed")
#     case "preparing":
#         print("Your order is being prepared")
#     case "out_for_delivery":
#         print("Your order is on the way")
#     case "delivered":
#         print("Your order has been delivered")
#     case "cancelled":
#         print("Your order has been cancelled")
#     case _:
#         print("Invalid Order Status")


# Q31]

# print("1 → Personal Banking\n2 → Business Banking")

# banking_type = int(input("Enter banking type: "))

# match banking_type:

#     case 1:
#         print("1 → Balance\n2 → Transfer\n3 → Loan")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Personal Banking - Balance Selected")
#             case 2:
#                 print("Personal Banking - Transfer Selected")
#             case 3:
#                 print("Personal Banking - Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → Balance\n2 → Payroll\n3 → Business Loan")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Business Banking - Balance Selected")
#             case 2:
#                 print("Business Banking - Payroll Selected")
#             case 3:
#                 print("Business Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Banking Type")


# 32]

# print("1 → Student\n2 → Teacher\n3 → Parent")

# role = int(input("Enter role: "))

# match role:

#     case 1:
#         print("1 → Marks\n2 → Attendance\n3 → Homework")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Student Marks Selected")
#             case 2:
#                 print("Student Attendance Selected")
#             case 3:
#                 print("Student Homework Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → Enter Marks\n2 → Attendance\n3 → Assign Homework")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Enter Marks Selected")
#             case 2:
#                 print("Teacher Attendance Selected")
#             case 3:
#                 print("Assign Homework Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 → Child Marks\n2 → Child Attendance\n3 → Contact Teacher")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Child Marks Selected")
#             case 2:
#                 print("Child Attendance Selected")
#             case 3:
#                 print("Contact Teacher Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")



# 33]

# print("1 → Flight\n2 → Train\n3 → Bus")

# transport = int(input("Enter transport: "))

# match transport:

#     case 1:
#         print("1 → Economy\n2 → Business")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Economy Selected")
#             case 2:
#                 print("Business Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → Sleeper\n2 → AC")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Sleeper Selected")
#             case 2:
#                 print("AC Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 → Ordinary\n2 → Volvo")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Ordinary Selected")
#             case 2:
#                 print("Volvo Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Transport")


# Q 34]

# print("1 → Start Game\n2 → Load Game\n3 → Settings\n4 → Exit")

# choice = int(input("Enter choice: "))

# match choice:

#     case 1:
#         print("Game Started")

#     case 2:
#         print("Game Loaded")

#     case 3:
#         print("1 → Sound\n2 → Graphics\n3 → Controls")
#         option = int(input("Enter setting: "))

#         match option:
#             case 1:
#                 print("Sound Settings Opened")
#             case 2:
#                 print("Graphics Settings Opened")
#             case 3:
#                 print("Controls Settings Opened")
#             case _:
#                 print("Invalid Setting")

#     case 4:
#         print("Exit")

#     case _:
#         print("Invalid Choice")



# Q 35]

# print("1 → Starters\n2 → Main Course\n3 → Desserts\n4 → Drinks")

# category = int(input("Enter category: "))

# match category:

#     case 1:
#         print("1 → Soup\n2 → Spring Roll\n3 → Garlic Bread")
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Soup Selected")
#             case 2:
#                 print("Spring Roll Selected")
#             case 3:
#                 print("Garlic Bread Selected")
#             case _:
#                 print("Invalid Item")

#     case 2:
#         print("1 → Pizza\n2 → Pasta\n3 → Biryani")
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Pizza Selected")
#             case 2:
#                 print("Pasta Selected")
#             case 3:
#                 print("Biryani Selected")
#             case _:
#                 print("Invalid Item")

#     case 3:
#         print("1 → Ice Cream\n2 → Cake\n3 → Gulab Jamun")
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Ice Cream Selected")
#             case 2:
#                 print("Cake Selected")
#             case 3:
#                 print("Gulab Jamun Selected")
#             case _:
#                 print("Invalid Item")

#     case 4:
#         print("1 → Coffee\n2 → Tea\n3 → Juice")
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Coffee Selected")
#             case 2:
#                 print("Tea Selected")
#             case 3:
#                 print("Juice Selected")
#             case _:
#                 print("Invalid Item")

#     case _:
#         print("Invalid Category")



# Q36

# print("1 → UPI\n2 → Card\n3 → Wallet")

# payment = int(input("Enter payment type: "))

# match payment:

#     case 1:
#         print("1 → Scan QR\n2 → Enter UPI ID")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Scan QR Selected")
#             case 2:
#                 print("Enter UPI ID Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → Credit Card\n2 → Debit Card")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Credit Card Selected")
#             case 2:
#                 print("Debit Card Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 → Add Money\n2 → Pay Using Wallet")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Add Money Selected")
#             case 2:
#                 print("Pay Using Wallet Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Payment Type") 



# Q37]

# print("1 → Programming\n2 → Mathematics\n3 → Communication")

# subject = int(input("Enter subject: "))

# match subject:

#     case 1:
#         print("1 → Python\n2 → Java\n3 → C++")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Python Selected")
#             case 2:
#                 print("Java Selected")
#             case 3:
#                 print("C++ Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → Algebra \n2 → Calculus \n3 → Statistics")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Algebra Selected")
#             case 2:
#                 print("Calculus Selected")
#             case 3:
#                 print("Statistics Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 → English\n2 → Presentation\n3 → Interview Skills")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("English Selected")
#             case 2:
#                 print("Presentation Selected")
#             case 3:
#                 print("Interview Skills Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Subject")




# Q 38

# print("1 → Engine\n2 → Lights\n3 → Music\n4 → Navigation")

# choice = int(input("Enter choice: "))

# match choice:

#     case 1:
#         print("1 → Start\n2 → Stop")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Engine Started")
#             case 2:
#                 print("Engine Stopped")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → Headlights\n2 → Indicators\n3 → Hazard Lights")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Headlights Selected")
#             case 2:
#                 print("Indicators Selected")
#             case 3:
#                 print("Hazard Lights Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 → Play\n2 → Pause\n3 → Next\n4 → Previous")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Music Playing")
#             case 2:
#                 print("Music Paused")
#             case 3:
#                 print("Next Song")
#             case 4:
#                 print("Previous Song")
#             case _:
#                 print("Invalid Option")

#     case 4:
#         print("1 → Start Navigation\n2 → Stop Navigation")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Navigation Started")
#             case 2:
#                 print("Navigation Stopped")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Choice")



# Q39

# print("1 → Employee\n2 → Manager")

# role = int(input("Enter role: "))

# match role:

#     case 1:
#         print("1 → View Profile\n2 → Apply Leave\n3 → View Salary")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("View Profile Selected")

#             case 2:
#                 leave_days = int(input("Enter number of leave days: "))

#                 if leave_days > 0:
#                     print("Leave Request Submitted")
#                 else:
#                     print("Invalid Leave Days")

#             case 3:
#                 print("View Salary Selected")

#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → View Team\n2 → Approve Leave\n3 → View Reports")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("View Team Selected")
#             case 2:
#                 print("Approve Leave Selected")
#             case 3:
#                 print("View Reports Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")


# Q40

# print("1 → Student\n2 → Teacher\n3 → Administration")

# role = int(input("Enter role: "))

# match role:

#     case 1:
#         print("1 → Profile\n2 → Marks\n3 → Attendance\n4 → Courses")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Student Profile")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case 4:
#                 print("Opening Student Courses")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         print("1 → Students\n2 → Enter Marks\n3 → Attendance\n4 → Courses")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Students")
#             case 2:
#                 print("Opening Enter Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case 4:
#                 print("Opening Teacher Courses")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         print("1 → Fees\n2 → Admissions\n3 → Notices\n4 → Departments")
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Fees")
#             case 2:
#                 print("Opening Admissions")
#             case 3:
#                 print("Opening Notices")
#             case 4:
#                 print("Opening Departments")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")

   