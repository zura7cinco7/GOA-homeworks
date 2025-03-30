def manual_find(s, char):
    for i in range(len(s)):
        if s[i] == char: 
            return i
    return -1 

text = "hello world"
char = "o"
result = manual_find(text, char)
print("სიმბოლო " + char + " მოიძებნა ინდექსზე" + result)
