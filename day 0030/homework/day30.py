def manual_len(item):
    length = 0
    if isinstance(item, list):
        for _ in item:
            length += 1
    elif isinstance(item, str):
        for _ in item:
            length += 1
    return length

print(manual_len([1, 2, 3, 4]))  
print(manual_len("Hello"))       

def manual_len(item):
    length = 0  
    for _ in item: 
        length += 1  
    return length

print(manual_len([1, 2, 3, 4])) 
print(manual_len("Hello"))      
