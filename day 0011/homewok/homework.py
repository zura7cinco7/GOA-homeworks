even_count = 0

for num in range(1, 51):
    if num % 2 == 0: 
        even_count += 1  

print(f"ლუწი რიცხვების რაოდენობა 1-დან 50-მდე არის: {even_count}")


num = 1
even_sum = 0
even_count = 0

while num <= 100:
    if num % 2 == 0: 
        even_sum += num  
        even_count += 1 
    num += 1 

average = even_sum / even_count 
print(f"ლუწი რიცხვების საშუალო არითმეტიკული 1-დან 100-მდე არის: {average}")


num = 1

while num <= 30:
    if num % 3 == 0: 
        print(num)
    num += 1


num = int(input("შეიყვანეთ რიცხვი: "))

if num > 0:
    print("ეს რიცხვი დადებითია.")
elif num < 0:
    print("ეს რიცხვი უარყოფითია.")
else:
    print("ეს რიცხვი არის 0.")
