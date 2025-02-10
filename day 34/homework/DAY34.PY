def manual_replace(input_string):
    # შევქმნათ ცარიელი სია, რომელშიც ჩვენ დავაგროვებთ სიმბოლოებს
    result = []
    
    # გავატაროთ ყველა სიმბოლო ინპუტ სტრინგში
    for char in input_string:
        if char == ' ':  # თუ სიმბოლოა space
            result.append('-')  # დავამატოთ - (ტირე)
        else:
            result.append(char)  # სხვა შემთხვევაში დავამატოთ იგივე სიმბოლო
    
    # ვბრუნავთ ახალ სტრინგს, რომელიც შექმნილია სიის ელემენტების გაერთიანებით
    return ''.join(result)

# ტესტი
input_text = "Hello world this is a test"
output_text = manual_replace(input_text)
print(output_text)  # უნდა Print-ვდეს: "Hello-world-this-is-a-test"


def manual_range(*args):
    # პირველ რიგში, ვადგენთ start, end და step
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    else:
        raise TypeError("manual_range() expected at most 3 arguments, got more")

    # მოვწესრიგებთ პროცედურას, რომ მივაღწიოთ სწორ შედეგს
    result = []
    if step > 0:
        while start < end:
            result.append(start)
            start += step
    elif step < 0:
        while start > end:
            result.append(start)
            start += step

    return result

# ტესტები
print(manual_range(5))       # უნდა დაბრუნდეს [0, 1, 2, 3, 4]
print(manual_range(2, 8))    # უნდა დაბრუნდეს [2, 3, 4, 5, 6, 7]
print(manual_range(1, 10, 2)) # უნდა დაბრუნდეს [1, 3, 5, 7, 9]
print(manual_range(10, 0, -2)) # უნდა დაბრუნდეს [10, 8, 6, 4, 2]
