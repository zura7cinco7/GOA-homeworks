# 1. შექმენით სია, წავშალოთ ბოლო ორი ელემენტი
my_list = [1, 2, 3, 4, 5]
my_list = my_list[:-2]  # წაშლა ბოლო ორი ელემენტის
print("1. სია, ბოლო ორი ელემენტის გარეშე:", my_list)

# 2. შექმენით ცვლადი, სადაც შეინახავთ სტრინგს და დაბეჭდეთ ის უკუღმა
my_string = "hello"
reversed_string = my_string[::-1]
print("2. სტრინგი უკუღმა:", reversed_string)

# 3. შექმენით რიცხვების სია და დაბეჭდეთ მათი მინიმუმი და მაქსიმუმი, შემდეგ მათი ჯამი
numbers = [10, 3, 56, 1, 23, 75, 8, 14, 99, 37]
min_num = min(numbers)
max_num = max(numbers)
print("3. მინიმალური და მაქსიმალური რიცხვების ჯამი:", min_num + max_num)

# 4. შექმენით სტრინგი და გაიგეთ, არის თუ არა ის პალინდრომი
palindrome_string = "ana"
is_palindrome = palindrome_string == palindrome_string[::-1]
print("4. პალინდრომია თუ არა:", is_palindrome)

# 5. რიცხვების სია, დავთვალოთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("ლუწი რიცხვები:", even_count)
print("კენტი რიცხვები:", odd_count)

# 6. შექმენით სია 1-ანებით და 0-ანებით, შემდეგ ახალი სია რომ შეიცავდეს True თუ 1, და False თუ 0
binary_list = [1, 0, 1, 0, 1]
new_list = []

for value in binary_list:
    if value == 1:
        new_list.append(True)
    else:
        new_list.append(False)

print(" ახალი სია:", new_list)
