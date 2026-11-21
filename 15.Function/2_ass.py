#1
# def greet():
#     print("Hello")

# print("Start")
# output:Start

#2
# def greet():
#     print("Hello")

# greet()
# greet()

# output:Hello Hello

#3
# def first():
#     print("A")

# def second():
#     print("B")

# second()
# first()
# second()

# output:B A B

#4
# def show():
#     print("Inside")

# print("One")
# show()
# print("Two")
# show()


# output: One Inside two Inside


# #5
# def outer():
#     print("Start")
#     print("Middle")

# print("A")
# outer()
# print("B")

# # output:A Start Middle B

# #6
# def task():
#     print("Task")

# task
# print("Done")

# # output:Done

#7
# def greet():
#     print("Hello")

# Greet()

# # output:Nameerror

# #8
# def show():
#     print("A")
#     print("B")

# print("C")
# show()

# # output:C A B

##################################13. Coding Practice Problems###############################################



##1 Define a function named greet that prints Hello, Python!. Call it once.

# def greet():
#     print("Hello,Python!")

# greet()



##2 Define a function named show_name that prints your name. Call it three times.

# def show_name():
#     print("Pavitra")
# show_name()
# show_name()
# show_name()



##3 Define a function named print_line that prints 20 hyphens. Call it before and after a heading.

# def print_line():
#     print("--------------------")
# print_line()
# print("Hello World!")
# print_line()




##4 Define a function named show_rules that prints three classroom rules, one per line.

# def show_rules():
#     print("Maintain silence in your Lab")
#     print("Uniform and id card is compulsory!!")
#     print("Maintain disclipline!!")
# show_rules()




##5 Define a function named show_square that prints a 4-by-4 square of * characters using four print("****") statements. Call it once.

# def show_square():
#     for i in range(1,5):
#         for j in range(1,5):
#             print("*",end=" ")
#         print("")
# show_square()



##6 Define a function named show_menu that prints three menu options. Call it twice.\

# def show_menu():
#     print("Pizza")
#     print("Maggie")
#     print("Burger")

# show_menu()
# show_menu()



##7 Define two functions, morning_message and evening_message. Call them in the reverse order of their definitions.

# def morning_message():
#     print("Good morning! Let's have some tea!!")
# def evening_message():
#     print("Good Evening!")
# evening_message()
# morning_message()



##8 Define a function named show_student_card that prints a heading, a student name, and a roll number. Call it once.

# def show_student_card():
#     print("Institute name:Coding Gita x SU")
#     print("Name:Angel")
#     print("Roll no:17")

# show_student_card()



##9 Define a function named print_numbers that prints the numbers 1 through 5 using five print statements. Call it twice.

# def print_numbers():
#     print(1)
#     print(2)
#     print(3)
#     print(4)
#     print(5)

# print_numbers()
# print_numbers()



## 10 Define a function named show_pattern that prints:

## *
## **
## ***

# def show_pattern():
#     for i in range(1,4):
#         for j in range(1,i+1):
#             print("*",end="")
#         print()
# show_pattern()



##11 Create three functions: show_header, show_body, and show_footer. Call them in the correct order to print a simple report.

# def show_header():
#         print("<html>")
# def show_body():
#         print("<body>")
# def show_footer():
#         print("<body>")

# show_header()
# show_body()
# show_footer()



##12 Create a function named show_separator that prints ====================. Use it between sections of a report.

# def show_separator():
#     print("====================")

# print("hello everyone my name is Angel")
# show_separator()
# print("I am a first year CSE student!!")



##13 Define functions named step_one, step_two, and step_three. Each should print its step name. Call them in the order 3, 1, 2.

# def step_one():
#     print(1)
# def step_two():
#     print(2)
# def step_three():
#     print(3)
# step_three()
# step_one()
# step_two()



##14 Create a function named show_table_heading that prints column headings for a student table. 
## Call it before printing two student rows.

# def show_table_heading():
#     print("Student name      Student surname")

# show_table_heading()
# print("Angel             Patel")



##15 Define a function that prints five stars on one line. Call it four times to create four rows.

# def stars():
#     for i in range(1,6):
#         print("*",end="")
#     print()
# stars()
# stars()
# stars()
# stars()



##16 Create a function named show_welcome that prints a welcome message and course name.
##  Call it at the start of a simple program.

# def show_welcome():
#     print("Welcome to Coding gita!! Would you like to experiance the CSE-AI course with us?")
# show_welcome()
# print("Coding Gita")



##17 Define a function named show_help that prints instructions for a simple calculator. 
## Call it before printing the calculator menu.

# def show_help():
#     print("perform simple calculations like:")
#     print(" Addition \n Subtraction \n Multiplication\n Division")

# show_help()



##18 Create two functions that print the opening and closing lines of a receipt. Call them around the receipt details.

# def print_lines():
#     print("-----------------------------")
# print_lines()
# print("Reciept details shown below:")
# print_lines()



##19 Define a function named print_box that prints a fixed three-line text box. Call it twice.

# def print_box():
#     print("Hello everyone welcome back to my chenal\nToday's vlog going to be crazyy\nSo, We are going on trip!!")
# print_box()
# print_box()



##20 Create functions for a program's title, menu, and closing message.
# # Arrange the calls to produce a readable program flow.

# def title():
#     print("Coding gita")
# def menu():
#     print('''
#     University work
#     job affairs
#     examination''')
# def closing_message():
#     print("Thank you for visiting our website")
# title()
# menu()
# closing_message()

#################################Debugging and Reasoning#############################################

##21

# def greet():
#     print("Hello")



##22

# def welcome():
#     print("Welcome")
# welcome()



##23

# def show():
#     print("Hello")
# show()
# previously the function was called before declaring it so it raised error



# #24
# def print_report():
#     print("Report")

# print_report()



##25

# def a():
#     print("A")

# def b():
#     print("B")

# a()
# b()
# a()

# # output:A B A

# #26

# def message():
#     print("Python")

# message()
# message()
# message()
# message()

# # #########the function body will run four times########

# #27

# def example():
#     print("One")
#     print("Two")

# print("Three")
# # ------function body:  print("One")
# #     print("Two")



## 28

# show_menu
# do_task
# student_details
# menu_card (assume it displays a menu)


# #29 Write a program with two function definitions but call only one. Predict the output.

# def fun_def1():
#     print("hello everyone")
# def fun_def2():
#     print("welcome to coding gita")
# fun_def2()



##30 Write a program that defines one function, prints a message outside it,
# # calls the function, and prints another message after the call.

# def greet():
#     print("Inside the function")

# print("Before function call")
# greet()
# print("After function call")



