###1

# #1.Predict the output
# # def show(n):
# #     if n == 0:
# #         print("Stop")
# #         return

# #     print(n)
# #     show(n - 1)
# #     print(n)

# show(2)
# print(2)
# print(1)
# print("Stop")
# print(1)
# print(2)

###222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222


# # 2.Find the base case (2 marks)
# # In this function, identify the base case and explain why it stops recursion.
# # def total(n):
# #     if n == 0:
# #         return 0

# #     return n + total(n - 1)

# def total(n):
#     if n == 0: #base case
#         return 0
#     return n + total(n - 1) #recursion

###333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

# #3. Find the bug (3 marks)
# # Explain why this function does not reach its base case when called with count(2). Rewrite the incorrect line.
# # def count(n):
# #     if n == 0:
# #         return

# #     count(n + 1)


# def count(n):
#     if n == 0:
#         return
#     count(n - 1)

###444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

# #4.Print or return? (3 marks)
# # What does this function return when called as answer(3)? Explain why.

# # def answer(n):
# #     if n == 0:
# #         return 0

# #     n + answer(n - 1)

# # print(answer(3))

# def answer(n):
#     if n == 0:
#         return 0
#     n + answer(n - 1)

# print(answer(3)) #return is missing so it will give "none"

###55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555

# #5. Count down (4 marks)
# # Write countdown(n) that prints every integer from n down to 1, then prints "Done!".

# # Constraint: n is a non-negative integer.

# # Examples:

# # countdown(3)
# # Output:

# # 3
# # 2
# # 1
# # Done!
# # Edge case: countdown(0) should print only Done!.

# def countdown(n):
#     if n == 0:
#         print("Done!")
#         return

#     print(n)
#     countdown(n - 1)

# countdown(3)
# countdown(0)

###666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666

# #6.Count up (4 marks)
# # Write count_up(n) that prints numbers from 1 through n in ascending order.

# # Example:

# # count_up(4)
# # Output:

# # 1
# # 2
# # 3
# # 4
# # Edge case: count_up(0) should print nothing.

# def count_up(n):
#     if n == 0:
#         return

#     count_up(n - 1)
#     print(n)

# count_up(4)
# count_up(0)

##0rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

# n = int(input("enter your number: "))

# def count_up(n):
#     def count_dw(count=1):
#         if count > n:
#             return "Done"
#         print(count)
#         return count_dw(count + 1)

#     return count_dw 

# count1 = count_up(n)
# print(count1())

##decendinggggggggggggggggggggggggggggggggggggggggggggg

# n = int(input("enter your number: "))
# def count_up(n):
#     if n == 0:
#         return n

#     print(n)
#     return count_up(n-1)

# print(count_up(n))

###77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777


# #7. Sum from 1 to n (4 marks)
# # Write sum_to(n) that returns the sum of all integers from 1 through n.

# # Examples:

# # print(sum_to(5))  # 15
# # print(sum_to(0))  # 0
# # Constraint: n is a non-negative integer.

# def sum_to(n):
#     if n == 0:
#         return 0

#     return n + sum_to(n - 1)

# print(sum_to(5))
# print(sum_to(0))

##0rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

# add = 0
# n = int(input("eneter your number: "))

# def count_up(n):
#     global add
#     add += n
#     if n == 0:
#         return add
#     return count_up(n-1)

# print(count_up(n))

###88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# #8.Factorial (4 marks)
# # Write factorial(n) that returns n!.

# # Examples:

# # print(factorial(4))  # 24
# # print(factorial(0))  # 1
# # Constraint: n is a non-negative integer.

# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)

# print(factorial(4))
# print(factorial(0))

###9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

# #9. Sum of digits (4 marks)
# # Write digit_sum(n) that returns the sum of the digits of a non-negative integer.

# # Examples:

# # print(digit_sum(583))  # 16
# # print(digit_sum(7))    # 7
# # print(digit_sum(0))    # 0
# # Hint: % 10 gets the last digit; // 10 removes the last digit.

# def digit_sum(n):
#     if n == 0:
#         return 0

#     return n % 10 + digit_sum(n // 10)

# print(digit_sum(583))
# print(digit_sum(7))
# print(digit_sum(0))

###1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101

# #10. Power (5 marks)
# Write power(base, exponent) that returns base raised to exponent.

# # Examples:

# # print(power(2, 5))  # 32
# # print(power(9, 0))  # 1
# # print(power(3, 1))  # 3
# # Constraint: exponent is a non-negative integer. Do not use ** in your function.

# def power(base, exponent):
#     if exponent == 0:
#         return 1

#     return base * power(base, exponent - 1)

# print(power(2, 5))
# print(power(9, 0))
# print(power(3, 1))


