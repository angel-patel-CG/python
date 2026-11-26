# #11. Count digits (5 marks)
# # Write count_digits(n) that returns the number of digits in a non-negative integer.

# # Examples:

# # print(count_digits(5382))  # 4
# # print(count_digits(6))     # 1
# # print(count_digits(0))     # 1
# # Hint: Each recursive call removes the last digit using // 10. Be careful with 0.

# def count_digits(n):
#     if n < 10:
#         return 1

#     return 1 + count_digits(n // 10)

# print(count_digits(5382))
# print(count_digits(6))
# print(count_digits(0))


# #12. Reverse a number as a string (5 marks)
# # Write reverse_text(text) that returns the characters of a string in reverse order using recursion.

# # Examples:

# # print(reverse_text("cat"))  # "tac"
# # print(reverse_text("a"))    # "a"
# # print(reverse_text(""))     # ""
# # Hint: Take the last character and combine it with the reverse of the remaining string, or take the first character and place it after the reversed remainder.

# def reverse_text(text):
#     if text == "":
#         return ""

#     return reverse_text(text[1:]) + text[0]

# print(reverse_text("cat"))
# print(reverse_text("a"))
# print(reverse_text(""))


# #13 Fibonacci number (5 marks)
# # Write fibonacci(n) that returns the nth Fibonacci number using these definitions:

# # fibonacci(0) = 0
# # fibonacci(1) = 1
# # Otherwise, fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
# # Examples:

# # print(fibonacci(0))  # 0
# # print(fibonacci(1))  # 1
# # print(fibonacci(6))  # 8
# # Constraint: n is a non-negative integer. Test only small values because this basic recursive method repeats calculations.

# def fibonacci(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(6))


# #14. Find the maximum digit (5 marks)
# # Write max_digit(n) that returns the largest digit in a non-negative integer.

# # Examples:

# # print(max_digit(4729))  # 9
# # print(max_digit(555))   # 5
# # print(max_digit(0))     # 0
# # Constraint: Do not use max(), loops, or convert the number to a string.

# # Hint: Compare the last digit (n % 10) with the maximum digit in the remaining number (n // 10). Design the base case carefully.

# def max_digit(n):
#     if n < 10:
#         return n

#     last_digit = n % 10
#     remaining = max_digit(n // 10)

#     if last_digit > remaining:
#         return last_digit
#     else:
#         return remaining

# print(max_digit(4729))
# print(max_digit(555))
# print(max_digit(0))


# #15. Trace the return values (5 marks)
# # Without running the code, write the value returned by mystery(4) and show the return calculation.

# # def mystery(n):
# #     if n <= 1:
# #         return n

# #     return mystery(n - 1) + mystery(n - 2)
# # Also state the values returned by mystery(0), mystery(1), and mystery(2).


# def mystery(n):
#     if n <= 1:
#         return n

#     return mystery(n - 1) + mystery(n - 2)

# print(mystery(4))
# print(mystery(0))
# print(mystery(1))
# print(mystery(2))


# #16. Fix the factorial (3 marks)
# # This function gives the wrong result for factorial(0). Fix the base case.

# # def factorial(n):
# #     if n == 0:
# #         return 0

# #     return n * factorial(n - 1)

# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)

# print(factorial(0))


# #17. Make progress (3 marks)
# # The function below never changes n. Rewrite it so it counts down to 0 and stops.

# # def stop_at_zero(n):
# #     if n == 0:
# #         return

# #     stop_at_zero(n)

# def stop_at_zero(n):
#     if n == 0:
#         return

#     stop_at_zero(n - 1)

# stop_at_zero(5)


# #18. State the limitation (4 marks)
# #Explain what may happen if a recursive function makes too many nested calls. Name the Python error that can occur. Give one reason a loop may be a better choice for a very large counting task.

# print("RecursionError")
# print("A loop is better for very large counting tasks because it uses less memory.")