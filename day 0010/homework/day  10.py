hidden_number = 12  

user_guess = 0

while user_guess != hidden_number:
    user_guess = int(input("გამოიცანით რიცხვი 1-დან 20-მდე: "))

    if user_guess > hidden_number:
        print("Too high!")
    elif user_guess < hidden_number:
        print("Too low!")

print("You win! 🎉")
