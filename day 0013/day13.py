my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("სრული სია:", my_list)

number_to_remove = int(input("შეიყვანეთ რიცხვი 1-დან 10-მდე, რომელიც უნდა წაშალოთ: "))

if number_to_remove in my_list:
    my_list.remove(number_to_remove)
    print("განახლებული სია:", my_list)
else:
    print("რიცხვი არ არის სიაში")
