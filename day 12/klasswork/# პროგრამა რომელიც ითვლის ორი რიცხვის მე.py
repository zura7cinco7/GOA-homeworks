# პროგრამა რომელიც ითვლის ორი რიცხვის მე-3 ხარისხს და მათ ჯამს

# მომხმარებლისგან ორი რიცხვის შეყვანა
num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

# რიცხვების მე-3 ხარისხში აყვანა
num3 = num1 ** 3
num4 = num2 ** 3

# რიცხვების ჯამის გამოთვლა
sum = num3 + num4

# შედეგის გამოხატვა
if sum % 2 == 0:
    print("Result is Even")
else:
    print("Result is Odd")
