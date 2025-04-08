password = "zura777"

attempts = 3

while attempts > 0:
    user_input = input("შეიყვანეთ პაროლი: ")
    
    if user_input == password:
        print("წვდომა მიღებულია")
        break 
    else:
        attempts -= 1  
        print("სცადეთ ხელახლა. დარჩენილი მცდელობები:", attempts)

if attempts == 0:
    print("მცდელობები ამოიწურა, გთხოვთ სცადოთ მოგვიანებით.")

    