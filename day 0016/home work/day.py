# 2) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხი
numbers = [10, 5, 8, 22, 15]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print("ყველაზე დიდი რიცხვი:", max_number)

# 3) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი
import math
numbers = [3, 4, 5]
for number in numbers:
    print(f"{number} ფაქტორიალი: {math.factorial(number)}")

# 4) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხი
numbers = [10, 5, 8, 22, 15]
min_number = numbers[0]
for number in numbers:
    if number < min_number:
        min_number = number
print("ყველაზე პატარა რიცხვი:", min_number)

# 5) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).
numbers = [10, -5, 8, -22, 15, -3]
negative_numbers = []
index = 0
while index < len(numbers):
    if numbers[index] < 0:
        negative_numbers.append(numbers[index])
    index += 1
print("უარყოფითი რიცხვები:", negative_numbers)

# 6) შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])

# 7) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
characters = ['a', 'b', 'c', 'a', 'b', 'd']
unique_characters = []
for char in characters:
    if char not in unique_characters:
        unique_characters.append(char)
print("უნიკალური სიმბოლოები:", unique_characters)

# 8) შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის
original_string = "Hello, World!"
reversed_string = original_string[::-1]
print("შემოტრიალებული სტრინგი:", reversed_string)

# 9) დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი
number = int(input("შეიყვანეთ რიცხვი: "))
divisors = [i for i in range(1, number + 1) if number % i == 0]
print("გამყოფები:", divisors)

# 10) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის
year = int(input("შეიყვანეთ წელი: "))
century = (year - 1) // 100 + 1
print(year + "წელი არის century საუკუნე.")
