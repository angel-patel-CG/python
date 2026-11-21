# #1

# a = 0
# b = 0

# def print_line():
#     print("--------------------")

# def add():
#     print_line()
#     print("addition:",a+b)
#     print_line()
# def sub():
#     print_line()
#     print("subtraction:",a-b)
#     print_line()
# def product():
#     print_line()
#     print("product:" ,a*b)
#     print_line()
# def divide():
#     print_line()
#     print("divide:" ,a/b)
#     print_line()
# def floor():
#     print_line()
#     print("floor division:" ,a/b)
#     print_line()



# a = int(input("Enter First number:"))
# b = int(input("Enter Second number:"))
# add()




# #2 

# def print_line():
#     print("--------------------")

# def even():
#     print_line()
#     if a%2 ==0:
#         print("Number is Even")
#     print_line()

# def odd():
#     print_line()
#     if a%2 !=0:
#         print("Number is Odd")
#     print_line()

# a = int(input("Enter number:"))
# even()
# odd()


# #3

# greet()

# def greet():
#     print("Hello")


# #4

# def addition(a,b):
#     c = a+b
#     print("Addition => ", c)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# addition(a,b)


#5

# a = 10 
# b =20
# c =40

# def add(a,b):
#     c = a + b
#     return

# def sub(a,b):
#     return a-b

# result = add(a,b)
# print(result)


# #6

# a=10
# b=20
# c=40

# def mul(a,b):
#     c = a*b
#     return c
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

# result= mul(sub(add(a,b),c),a)
# print(result)
    

# #6

# a=10
# b=20
# c=40

# def mul(a,b):
#     c = a*b
#     return c
# def add(a,b):
#     c = a+b
#     return c
# def sub(a,b):
#     c = a-b
#     return c

# result= mul(sub(a,b),add(b,c))
# print(result)



# #7 


# def double(number):
#     return number * 2

# def add_five(number):
#     return number + 5

# result = add_five(double(10))
# print(result)


# #8

# def calculate(a, b):

#     return a - b, a + b

# answer = calculate(10, 4)
# print(answer)
    


# #orrrrrrrrrrrrrrr


# def calculate(a, b):
#     print(a + b)
#     print(a - b)

# answer = calculate(10, 4)
# print(answer)


# #orrrrrrrrrrrrrrrrrrrrrrrrrr

# def add(a,b):
#     total= a + b
#     sub = a-b
#     return print(total,sub)

# add(2,3)


#9

# def function(a,b):
#     add= a+b
#     sub= a-b
#     mul= a*b
#     div= a/b
#     return add,sub,mul,div

# add,sub,mul,div = function(24,12)
# print(f"addition: {add} \nsubtraction: {sub} \nproduct: {mul} \ndivision: {div}")


# #10

# def describe(name, age, city):
#     print(name, age, city)

# describe("Pune", name="Asha", age=21)


#11

# def counter_fun(count):

#     count = count + 1

#     if(count == 20):
#         return
#     counter_fun(count)


# counter_fun(2)

############0rrrrrrrrrrrrrrrrrr

# def counter_fun(count):

#     count = count + 1

#     if(count == 20):
#         return count
    
#     return counter_fun(count)


# print(counter_fun(1))



# # 12

# def info(a,b,c,d,*arags,e=22):
#     print(a,b,c,d,e,arags)

# info(1,2,3,4,5,6,7,8,9)


# #13

# def info(a=4,b=2,/,*,c=6,d=8):
#     return a/b , c-d

# print(info(8,4,c=5,d=4))


# #14


# def info(*args):
#     print(args)
#     print(type(args))

# info()
# info(a=1,b=2,c=3)




# #15


# def info(k,j,p,*args,f=30,**kwargs):
#     print(kwargs,args)
#     print(j,k,p,f)
#     print(type(args))
#     print(type(kwargs))

# info(10,20,60,80,90,a=1,b=2,c=3)



# #16

# def factorial(n):
#     if n<0:
#         return "Factorial is not defined for negative numbers"
    
#     result = 1

#     for i in range(1,n+1):
#         result *= i
#     return result

# number = int(input("Enter your number: "))
# print(f"The factorial of {number} is {factorial(number)}")


# #17

# def add(a,b,c):
#     return a+b+c

# number = 10,20,30    # ye tupple ki tarah hi behave karegaaa until koi mapping naah hooo!!!!!!!
# print(add(*number))


# #18


# def calculate_area(length, width):

  

#     """
#     Calculate the area of a rectangle.

#     Args:
#         length: The rectangle's length.
#         width: The rectangle's width.

#     Returns:
#         The area of the rectangle.
#     """
#     return length * width


# print(calculate_area(12,24))
# print(calculate_area.__doc__)


# #19

# total = 12
# total =13

# def func():
#     # return total
#     print(total)
#     total = 17

# print(func())
# print(total)
# func()


#20

# list = [1, 2, 3, 4, 5]

def outer():
    # list = [1, 2, 3, 4, 5]
    def inner():
        # list = [1, 2, 3, 4, 5]
        print(list("hello"))
    inner()
outer()
print(list)