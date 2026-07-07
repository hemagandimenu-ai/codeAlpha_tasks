# ============================================
# Basic Rule-Based Chatbot
# Developed using Python
# Concepts Used:
# - Functions
# - if-elif statements
# - while loop
# - input/output
# ============================================

def chatbot(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "good morning", "good evening"]:
        return "Hello! Nice to meet you."

    # Asking chatbot status
    elif user_input in ["how are you", "how are you?"]:
        return "I'm doing great! Thanks for asking."

    # Asking user's name
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {name.title()}!"

    # Asking chatbot name
    elif user_input in ["what is your name", "who are you"]:
        return "I am a Basic Python Chatbot."

    # College
    elif user_input == "which college are you from":
        return "I am a virtual chatbot, so I don't study in any college."

    # Age
    elif user_input in ["how old are you", "your age"]:
        return "I don't have an age like humans."

    # Time
    elif user_input == "what time is it":
        return "Sorry, I cannot tell the current time."

    # Date
    elif user_input == "what is today's date":
        return "Sorry, I cannot access today's date."

    # Programming
    elif user_input == "which programming language do you know":
        return "I know Python, Java, C, C++, JavaScript and more."

    # Python
    elif user_input == "what is python":
        return "Python is a popular, high-level programming language."

    # Java
    elif user_input == "what is java":
        return "Java is an class based  object-oriented programming language."

    # AI
    elif user_input == "what is ai":
        return "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."

    # Joke
    elif user_input == "tell me a joke":
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    # Motivation
    elif user_input == "motivate me":
        return "Believe in yourself. Every expert was once a beginner."

    # Thanks
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! Happy to help."

    # Help
    elif user_input == "help":
        return ("You can ask me:\n"
                "- Hello\n"
                "- How are you\n"
                "- What is your name\n"
                "- What is Python\n"
                "- What is Java\n"
                "- What is AI\n"
                "- Tell me a joke\n"
                "- Motivate me\n"
                "- Bye")

    # Goodbye
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a wonderful day."

    # Default
    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."


# ===============================
# Main Program
# ===============================

print("=" * 50)
print("      WELCOME TO BASIC CHATBOT")
print("=" * 50)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    response = chatbot(user)

    print("Chatbot:", response)

    if user.lower() in ["bye", "exit", "quit"]:
        print("\nChatbot session ended.")
        break