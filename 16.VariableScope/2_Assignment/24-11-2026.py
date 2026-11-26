# # 1.Create a function with a local variable city and print it.

# def cities():
#     city = "Pune"
#     return city
# print(cities())


# # 2.Create a global variable school. Read it inside a function.

# school = "ABC School"

# def school_name():
#     return school   

# print(school_name())


# # 3.Assign a variable inside an if block and print it outside the block.

# if True:
#     x = 10
# print(x)

# # 0rrrrrrrrrrrrrrrrr

# if False:
#     x = 10
# print(x)


# # 4.Use a for loop to assign a loop variable. Print it after the loop.

# for i in range(1,5):
#     i = i + 1
# print(i)


# 5.Explain the difference between scope and lifetime in your own words.

# Scope refers to the region of the code where a variable is accessible, 
# while lifetime refers to the duration for which a variable exists in memory.


# # 6.Predict the output:
# # value = 100
# # def test():
# #     value = 200
# #     print(value)
# # test()
# # print(value)

# OUTPUT: 200


# # 7.Fix this code so it increments the global variable:
# # clicks = 0
# # def click():
# #     clicks += 1

# clicks = 0
# def click():
#     global clicks
#     clicks += 1
#     print(clicks)
# click()


# 8.Explain why this code raises an error:
# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()

# The code raises an error because the variable 'name' is being assigned a value inside the function 'show()', 
# which makes it a local variable. However, the function tries to print the value of 'name' before it has been assigned, 
# leading to an UnboundLocalError.


# # 9.Write a nested function that reads a variable from its enclosing function.

# def outer_function():
#     name = "enclosing"
#     def inner_function():
#         print(name)
#     inner_function()

# outer_function()


# # 10.Write a function that returns a list. Show that the returned list can be changed by the caller.

# def outer():
#     list = "Hi"
#     def inner():
#         global list
#         print(list("Helllo"))
#     inner()
# outer()


# # 11.Use nonlocal to create a counter that returns 1, 2, 3 across three calls.

# def make_counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# counter = make_counter()
# print(counter())
# print(counter())
# print(counter())


# # 12.Predict the output:
# # x = 1
# # def outer(): 
# #     x = 2
# #     def inner():
# #         x = 3
# #         print(x)
# #     inner()
# #     print(x)
# # outer()
# # print(x)

# OUTPUT: 3 2 1


# # 13.Explain why the loop variable in a normal for loop can remain available after the loop, 
# # but a list-comprehension variable in Python 3 does not overwrite an outer variable.

# for i in range(0,5):
#     i+=1
# print(i)


# # 14.Create a function that returns another function. Explain which variable remains available and why.

# # innnnnnnnnnnn notebook


# #15 Explain why variable names such as list, str, and sum should usually be avoided.

# Beacuse list , str and sum are built-in function,
# So it cause error whenever we use built-in function and variable named by built-in function. 