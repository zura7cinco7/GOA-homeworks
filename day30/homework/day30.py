def manual_len(item):
    length = 0
    if isinstance(item, list):
        for _ in item:
            length += 1
    elif isinstance(item, str):
        for _ in item:
            length += 1
    return length

# ტესტირება
print(manual_len([1, 2, 3, 4]))  # 4
print(manual_len("Hello"))       # 5

def manual_len(item):
    length = 0  # სტარტით სიგრძე 0
    for _ in item:  # ვიტოვებთ ციკლს, რომელიც გადის თითოეულ ელემენტზე
        length += 1  # ყოველ ჯერზე სიგრძე იზრდება
    return length

# ტესტირება
print(manual_len([1, 2, 3, 4]))  # უნდა დაბრუნდეს 4
print(manual_len("Hello"))       # უნდა დაბრუნდეს 5
