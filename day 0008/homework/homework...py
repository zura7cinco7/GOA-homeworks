num = int(input("შეიყვანეთ რიცხვი: "))
for i in range(num + 1):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
