# 51
array = [1, 2, 3]

for element in array:
    print(element, end=" ")


# 52
array = [1, 2, 3]
sum = 0

for element in array:
    sum += element

print(sum)


# 53
array = [3, 7, 2, 9]
maximum = array[0]

for element in array:
    if element > maximum:
        maximum = element

print(maximum)


# 54
array = [3, 7, 2, 9]
minimum = array[0]

for element in array:
    if element < minimum:
        minimum = element

print(minimum)


# 55
array = [1, 2, 3, 4, 5, 6]
count = 0

for element in array:
    if element % 2 == 0:
        count += 1

print(count)


# 56
array = [1, 2, 3, 4, 5]
count = 0

for element in array:
    if element % 2 != 0:
        count += 1

print(count)


# 57
array = [-1, 0, 5, 3, -2]

for element in array:
    if element > 0:
        print(element, end=" ")


# 58
array = [-1, 0, 5, 3, -2]

for element in array:
    if element < 0:
        print(element, end=" ")


# 59
array = [5, 12, 7, 20, 3]

for element in array:
    if element > 10:
        print(element, end=" ")


# 60
array = [1, 2, 3, 4]
sum = 0

for element in array:
    sum += element

average = sum / len(array)

print(average)