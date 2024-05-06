import re

# List of possible responses
responses = {
    "hello|hi|hey": ["Hello! How can I assist you today?"],
    "how are you": ["As an AI assistant, I don't have personal feelings or a subjective experience of being. However, "
                    "I'm functioning properly and ready to help you with the questions: "],
    "what is your name": ["My name is Sandeep's ChatBot.It's nice to meet you Sir !"],
    "what is the weather like today": [ "Unfortunately, I don't have direct access to current weather information "
                                        ".As an AI, I don't have the ability to sense the real-time weather"],
    "can you tell me a joke": ["Sure, here's a silly one for you: Why can't a bicycle stand up by itself? It's "
                                " two-tired!"],
    "how old are you": ["I don't have an age in the same way humans do. I was created by Sandeep, but I don't have"
                         " a birth date or aging process."],
    "what is the capital of India": ["The capital of India is delhi."],
    "where are you from": ["I don't have a physical location or place of origin. I'm an artificial intelligence "
                           "assistant."],
    "How's your day going so far": ["As an AI system, I don't experience days or have a sense of how a day is going."
                                     " I'm simply ready to assist you whenever you need help!"],
    "bye": ["Take care!"],
 }


def respond(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check for matching patterns in user input
    for pattern, responses_list in responses.items():
        if re.search(pattern, user_input,re.IGNORECASE):
            return responses_list[0]

    # If no matching pattern is found, return a default response
    return "Could you rephrase that?"


print("Welcome to the ChatBot! Let's chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("ChatBot: Goodbye!")
        break
    print("ChatBot:", respond(user_input))