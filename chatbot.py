def chatbot_reply(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! Nice to meet you. 😊"

    elif message == "how are you":
        return "I'm fine, thank you! How are you?"

    elif message == "what is your name":
        return "I am a simple Python chatbot."

    elif message == "what can you do":
        return "I can reply to some basic messages."

    elif message == "thank you" or message == "thanks":
        return "You're welcome! 😊"

    elif message == "bye" or message == "goodbye":
        return "Goodbye! Have a nice day! 👋"

    else:
        return "Sorry, I don't understand that message."


def start_chat():
    print("================================")
    print("       SIMPLE CHATBOT")
    print("================================")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_message = input("You: ")

        reply = chatbot_reply(user_message)
        print("Bot:", reply)

        if user_message.lower().strip() in ["bye", "goodbye"]:
            break


start_chat()