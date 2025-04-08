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