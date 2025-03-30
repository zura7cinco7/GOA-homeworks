def filter_numbers(lst):
    new_list = []
    for number in lst:
        if number > 10:
            new_list.append(number)
    return new_list

result = filter_numbers([5, 12, 8, 15, 3])
print(result)
