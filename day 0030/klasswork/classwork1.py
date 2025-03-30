def manual_count(lst, num):
    count = 0
    for n in lst:
        if n == num:
            count += 1 
    return count

numbers = [1, 2, 3, 2, 5, 2, 6, 2]
number_to_find = 2
result = manual_count(numbers, number_to_find)
print(f"რიცხვი {number_to_find} გამოჩნდა სიაში {result} ჯერ.")
