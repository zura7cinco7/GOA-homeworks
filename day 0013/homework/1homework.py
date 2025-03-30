fruits = ["apple", "banana", "cherry"]

favorite_fruit = input("შეიყვანეთ თქვენი საყვარელი ხილი: ")

if len(fruits) % 2 == 0:
    fruits.append(favorite_fruit)
    print("ახალი სია:", fruits)
else:
    print("სიის ბოლო ელემენტის ინდექსი არის კენტი, ხილი არ დაემატა.")
