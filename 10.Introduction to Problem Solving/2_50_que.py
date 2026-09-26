# #2

# fail_count = 0
# pass_count = 0
# good_count = 0
# excellent_count = 0

# for i in range(1, 11):
#     marks = int(input(f"enter marks for student {i} (0-100): "))

#     if marks < 35:
#         print("Fail")
#         fail_count += 1
#     elif marks <= 49:
#         print("Pass")
#         pass_count += 1
#     elif marks <= 74:
#         print("Good")
#         good_count += 1
#     elif marks <= 100:
#         print("Excellent")
#         excellent_count += 1
#     else:
#         print("invalid marks entered.")


# print("Fail:", fail_count)
# print("Pass:", pass_count)
# print("Good:", good_count)
# print("Excellent:", excellent_count)



# #5

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# short_count = 0
# medium_count = 0
# long_count = 0


# for word in words:
   
#     clean_word = word.strip(".,!?;:\"'")
#     word_length = len(clean_word)
    
#     if word_length <= 3:
#         category = "Short"
#         short_count += 1
#     elif word_length <= 6:
#         category = "Medium"
#         medium_count += 1
#     else:
#         category = "Long"
#         long_count += 1
        
#     print(f"Word: '{clean_word}' . Length: {word_length} . Category: {category}")

# print("Short words:", short_count)
# print("Medium words:", medium_count)
# print("Long words:", long_count)


# #3
 
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# vovels = "aeiou"
# consonant = "qwrtypsdfghjklzxcvbnm"

# highest_score = -1
# highest_word = ""


# for word in words:
   
#     clean_word = word.strip(".,!?;:\"'").lower()
    

#     vowel_count = 0
#     consonant_count = 0
#     digit_count = 0
#     special_character_count = 0


#     for char in clean_word:


#         if char in vovels:
#             vowel_count += 1
#         elif char in consonant:
#             consonant_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         else:
#             special_character_count += 1

        
#     score_v = vowel_count * 2
#     score_c = consonant_count * 1
#     score_d = digit_count * 3
#     score_s = special_character_count * 4

#     word_score = score_v + score_c + score_d + score_s

#     print(f"word : {clean_word} . points : {word_score} ")


# if word_score > highest_score:
#         highest_score = word_score
#         highest_word = clean_word
    
# print(f"Highest scoring word: '{highest_word}' with {highest_score} points.")


# #1

# string = input("enter a value: ")
# count1 = 0
# count2 =0
# count3 =0
# count4 = 0
# count5 = 0



# for character in string:
#     if character.isupper():
#         count1 += 1
#     elif character.islower():
#         count2 += 1
#     elif character.isdigit():
#         count3 += 1
#     elif character == " ":
#         count4 += 1
#     else :
#         count5 =+ 1

# print(f"count for uppercase letters {count1},\n count for lowercase letters {count2} , \n  count for digits  {count3},\n  count for white spaces  {count4}, \n count for special character {count5}" )

# if count1 > count2 and count1 > count3 and count1 > count4 and count1 > count5:
#     print (f" uppercase count is highest => {count1}")
# elif count2 > count1 and count2 > count3 and count2 > count4 and count2 > count5: 
#     print (f" lowercase count is highest => {count2}")
# elif count3 > count1 and count3 > count2 and count3 > count4 and count3 > count5: 
#     print (f" digit count is highest => {count3}") 
# elif count4 > count1 and count4 > count3 and count4 > count2 and count4 > count5: 
#     print (f" whitespace count is highest => {count4}") 
# elif count5 > count1 and count5 > count3 and count5 > count4 and count5 > count2: 
#     print (f" special character count is highest => {count5}")
# else :
#     print("Tie")



#4


for i in range(1,6):
    print(i,".")
    password = input("enter your password => ")

    uppercase_char = 0
    lowercase_char = 0
    digit_char = 0
    special_char = 0


