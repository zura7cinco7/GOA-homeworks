#2) მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ, რამდენჯერ შედის შემოტანილი რიცხვი 100-ში.
#  გააკეთეთ ყველაზე მოკლე გზით(ამისათვის გამოიყენეთ გაყოფის სწორი ტიპი)

number = int(input("შეიტანეთ რიცხვი: "))
result = 100 // number - 2
print(number + result)

#4)მომხარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ ის, რომელიც არის
 #მეტი. თუ ორივე რიცხვი ტოლია დაბეჭდეთ "Both numbers are equal"

num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
num2 = float(input("შეიტანეთ მეორე რიცხვი: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Both numbers are equal")

#მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. შემდეგ დაბეჭდეთ
# შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი

number = int(input("შეიტანეთ რიცხვი: "))

sum = 0

for i in range(1, number + 1):
    sum = sum + i * 2

print(sum)

