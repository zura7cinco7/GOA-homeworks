num = 1
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print(f"FizzBuzz {num}")
    elif num % 3 == 0:
        print(f"Fizz {num}")
    elif num % 5 == 0:
        print(f"Buzz {num}")
    num += 1
