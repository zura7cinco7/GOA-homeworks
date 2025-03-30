def filter_names(names):
    new_list = []
    for name in names:
        if name.startswith('N'):
            new_list.append(name)
    return new_list

result = filter_names(["Nika", "Luka", "Nana", "Gio"])
print(result)
