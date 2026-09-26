#1



total = 0
passed = True
grade = ""

subject = ["maths","science","english","hindi","social science"]


for i in range(1):
    for j in range(len(subject)):
        marks = int(input(f"{j+1}. marks in {subject[j]}: "))

        total = total + marks

    if marks < 35:
        passed = False

percentage = total / 5

if passed:
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
else:
    grade = "F"

print(total)
print(percentage)
print(grade)

if passed:
    print("pass")
else:
    print("fail")



#2

