while True:
    print("Go on")
    user_input = input("Enter your question or 'exit' to quit: ").lower()

    if user_input == "how are you?":
        print("I'm doing well, thank you!")
    elif user_input == "what's the weather like?":
        print("It's sunny and warm today.")
    elif user_input == "give me bitcoin":
        print("I'm sorry, but I can't give you bitcoin.")
    elif user_input == "hack nasa":
        print("I'm not hacking NASA, I'm a Python programmer.")
    elif user_input == "exit":
        print("Goodbye!")
        break
    else:
        print("I'm not sure how to answer that.")
        