num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

num3 = num1 ** 3
num4 = num2 ** 3

sum = num3 + num4

if sum % 2 == 0:
    print("Result is Even")
else:
    print("Result is Odd")
