def chatbot():
    print("Welcome to RuleBot! Type something to start chatting (type 'bye' to exit).")

    while True:
        user_input = input("You: ").lower()

        # Exit command
        if "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("Bot: Goodbye! Have a great day!")
            break

        # Rule-based responses
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! Thanks for asking.")

        elif "what is your name" in user_input:
            print("Bot: I'm RuleBot, your simple chatbot friend!")

        elif "what can you do" in user_input:
            print("Bot: I can answer simple questions and keep you company!")

        elif "who made you" in user_input:
            print("Bot: I was made by an engineering student as part of an AI internship task!")

        elif "thank you" in user_input or "thanks" in user_input:
            print("Bot: You're welcome!")

        elif "i love you" in user_input:
            print("Bot: Aww, thank you! You're sweet.")

        elif "tell me a joke" in user_input:
            print("Bot: Why don’t scientists trust atoms? Because they make up everything!")

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {now}")

        else:
            print("Bot: Hmm, I don't understand that yet. Try asking something else!")

# Start the chatbot
chatbot()
