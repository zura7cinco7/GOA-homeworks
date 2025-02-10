# 2. string-ების სია, გადაუარეთ for loop-ით და დაბეჭდეთ სიტყვის სიმბოლოთა რაოდენობა
strings = ["apple", "banana", "cherry", "date"]
for word in strings:
    print(word + len(word))

# 3. რიცხვების სია, while loop-ით გაიგეთ ლუწი რიცხვის ჯამი
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_sum += numbers[index]
    index += 1
print(even_sum)

# 4. სახელების სია, გადაუარეთ for loop-ით და დაბეჭდეთ მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე
names = ["Alice", "Bob", "Anna", "Charlie", "Alex"]
for name in names:
    if name.startswith("A"):
        print(name)

# 5. რიცხვების სია, სადაც დუბლიკატებია, და დაბეჭდეთ მხოლოდ ისეთი რიცხვების ჯამი, რომლებიც არ მეორდება
numbers_with_duplicates = [1, 2, 3, 2, 4, 5, 1, 6]
unique_sum = 0
seen_numbers = set()
for num in numbers_with_duplicates:
    if numbers_with_duplicates.count(num) == 1:
        unique_sum += num
print(unique_sum)

# 6. პროგრამა, რომელიც ჩაწერავს რიცხვებს და დაბეჭდავს 1-დან რიცხვამდე ყველა მარტივ რიცხვს
n = int(input("შეიყვანეთ რიცხვი: "))
primes = []
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(primes)

# 7. სია 5 ელემენტით, slicing-ის გამოყენებით დაბეჭდეთ მე-3 და მე-4 ელემენტები
my_list = [10, 20, 30, 40, 50]
print(f"7. მე-3 და მე-4 ელემენტები: {my_list[2:4]}")

# 8. რიცხვების სია, 10 ელემენტისგან, slicing-ის გამოყენებით დაბეჭდეთ სიის ყოველი მეორე ელემენტი
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::2])

# 9. string-ის ბოლო სამი სიმბოლო (მინუსიანი ინდექსებით)
my_string = "HelloWorld"
print("ბოლო სამი სიმბოლო: my_string-3:")

# 10. რიცხვების სია, დაბეჭდეთ სია slicing-ის გამოყენებით
numbers = [10, 20, 30, 40, 50]
print(numbers)
