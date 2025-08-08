def bot_reply(message):
    msg = message.lower()
    if msg in ("greetings", "yo", "hola", "hi there"):
        return "Hey"
    elif msg in ("how's it going", "you okay", "how u doing", "how's life"):
        return "Doing great, thanks"
    elif msg in ("see ya", "farewell", "end", "stop"):
        return "Catch you later"
    elif msg == "assist":
        return "Try 'greetings', 'how's it going', 'see ya'"
    else:
        return "Not sure what you mean."
def start():
    print("Bot: Yo! Type 'see ya' to quit")
    while True:
        user_msg = input("User: ")
        response = bot_reply(user_msg)
        print("Bot:", response)
        if user_msg.lower() in ("see ya", "farewell", "end", "stop"):
            break
if __name__ == "__start__":
    start()
