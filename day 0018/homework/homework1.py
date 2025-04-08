numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_sum += numbers[index]
    index += 1
print(even_sum)
