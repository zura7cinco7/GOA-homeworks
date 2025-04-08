numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]

average = sum(even_numbers) / len(even_numbers)

print(even_numbers)
print(average)
