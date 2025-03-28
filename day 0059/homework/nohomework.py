password = "zuka"
attempts = 3

while attempts > 0:
    user_input = input("გთხოვთ, შეიყვანეთ პაროლი: ")
    
    if user_input == password:
        print("პაროლი სწორი!")
        break 
    else:
        attempts -= 1
        if attempts == 0:
            print("შესვლის მცდარი ცდა. არ გაქვთ მეტი შანსი!")
        else:
            print("პაროლი არასწორია. დარჩა", attempts, "შანსი.")
