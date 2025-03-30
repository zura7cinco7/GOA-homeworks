num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("num1 / num2=  result")
    else:
        print("შეცდომა: ნულზე გაყოფა შეუძლებელია!")
else:
    print("შეცდომა: არასწორი ოპერაცია! აირჩიეთ +, -, * ან /")

