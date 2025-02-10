#1) შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. გადაუარეთ ამ საის while loop-ის გამოყენებით. გაიგეთ 
#ცალკე ლუწი და კენტი რიცხვების ჯამი, საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი

numbers = [1, 7, 9, 21, 4, 88, 15, 6, 333, 10]

even_sum = 0
odd_sum = 0

index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_sum += numbers[index]
    else: 
        odd_sum += numbers[index]
    index += 1

sum = even_sum = odd_sum 

print("უდიდესი ჯამი არის:",sum)


#2) შექმენით სიმბოლოების სია, გადაუარეთ მას for loop-ით და სიიდან ყველა სიმბოლოს შორის
# მოახდინეთ კონკადინაცია. ციკლის გარეთ დაგჭირდებათ ცვლადი სადაც შაამატებთ ამ სთრინგებს
#კონკადინაცია - სტრინგის, სტრინგზე დამატებე(შეერთება)

characters = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

result_string = ""

for i in characters:
    result_string += i 

print("კონკადინაცია:", result_string)
