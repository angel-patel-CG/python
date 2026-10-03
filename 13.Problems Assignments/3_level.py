# # 21
# n = int(input())

# n = abs(n)

# if n == 0:
#     print(1)
# else:
#     count = 0

#     while n > 0:
#         count += 1
#         n //= 10

#     print(count)


# # 22
# n = abs(int(input()))
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10

# print(sum)


# # 23
# n = abs(int(input()))
# product = 1

# if n == 0:
#     print(0)
# else:
#     while n > 0:
#         digit = n % 10
#         product *= digit
#         n //= 10

#     print(product)


# # 24
# n = int(input())

# sign = -1 if n < 0 else 1
# n = abs(n)

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# print(reverse * sign)


# # 25
# n = int(input())

# original = n
# n = abs(n)
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# if abs(original) == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")


# # 26
# n = int(input())
# is_prime = True

# if n < 2:
#     is_prime = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("true")
# else:
#     print("false")


# # 27
# n = int(input())

# for number in range(2, n + 1):
#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(number, end=" ")


# # 28
# n = int(input())

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# # 29
# a = int(input())
# b = int(input())

# a = abs(a)
# b = abs(b)

# gcd = 1

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

# print(gcd)


# # 30
# a = int(input())
# b = int(input())

# a = abs(a)
# b = abs(b)

# gcd = 1

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

# lcm = (a * b) // gcd

# print(lcm)