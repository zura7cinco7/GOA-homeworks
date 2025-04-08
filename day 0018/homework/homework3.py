numbers_with_duplicates = [1, 2, 3, 2, 4, 5, 1, 6]
unique_sum = 0
seen_numbers = set()
for num in numbers_with_duplicates:
    if numbers_with_duplicates.count(num) == 1:
        unique_sum += num
print(unique_sum)