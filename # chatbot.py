# chatbot.py

print("ChatBot: Hello! I'm your friendly chatbot.")
print("Type 'bye' to end the chat.")
print("--------------------------------------------")

while True:
    user_input = input("You: ").lower()

    # exit condition
    if "bye" in user_input:
        print(" ChatBot: Goodbye! Have a nice day ")
        break

    # greetings
    elif "hi" in user_input or "hello" in user_input:
        print("ChatBot: Hello there! How are you doing?")
    
    # feeling
    elif "how are you" in user_input:
        print("ChatBot: I'm doing great! Thanks for asking.")
    
    elif "your name" in user_input:
        print(" ChatBot: I'm Chatty, your simple rule-based chatbot!")
    
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f" ChatBot: The current time is {current_time}")

    elif "date" in user_input:
        from datetime import date
        today = date.today()
        print(f" ChatBot: Today's date is {today.strftime('%B %d, %Y')}")

    elif "weather" in user_input:
        print(" ChatBot: I can’t check weather yet, but it looks like a great day!")

    elif "joke" in user_input:
        print(" ChatBot: Why don't programmers like nature? It has too many bugs! ")

    elif "who made you" in user_input:
        print(" ChatBot: I was created by a smart human like you using Python!")

    elif "love" in user_input:
        print(" ChatBot: Love is a beautiful thing️ But I only know Python!")

    else:
        print(" ChatBot: I'm not sure how to respond to that. Try something else!")