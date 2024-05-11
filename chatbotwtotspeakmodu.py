import random
import datetime
import os

def guessthenumbergame():
    randomn = random.randint(1, 100)
    i = 0 

def guessthenumbergame():
    randomn = random.randint(1, 100)
    i = 0  

    print("Welcome to the Guess the Number game!")

    while True:
        if i == 0:
            guess = int(input("Enter a number between 1 to 100: "))
        else:
            guess = int(input("Enter another number between 1 to 100: "))
        i += 1 

        if guess < randomn:
            print("Higher number please.")
        elif guess > randomn:
            print("Lower number please.")
        else:
            print(f"WOW! You won the game in {i} guesses")
            break 

responses = {
    "how are you": ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "Great, how about you?"],
    "what's your name": ["I'm a chatbot!", "You can call me Chatbot.", "I don't have a name, but you can call me whatever you like!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "okay":["😄"],
    "what is your name": ["My name is Jarvis","I'm a chatbot!", "You can call me Chatbot.", "I don't have a name, but you can call me whatever you like!"],
    "what are your capabilities": ["I am a simple Chatbot.","I like chatting with you."],
    "are you fine": ["I am a Chatbot and I don't have any emotions or health"],
    "which game do you like": ["I Like Carrom, Ludo, Cricket and Hockey."],
    "which game do you play": ["I Like Carrom, Ludo, Cricket and Hockey."],
    "who is iron man": ["Iron Man is my Boss"],
    "can you sing a song": ["No, I don't have the ability to sing."],
    "i love you": ["I Love You Too..."],
    "love you bro": ["I Love You Too Bro..."],
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "hey": ["Hello!", "Hi there!", "Hey!"],
    "fine": ["Glad to hear that!", "That's good to know!", "Great!"],
    "good": ["Glad to hear that!", "That's good to know!", "Great!"],
    "not so good": ["I hope things get better soon.", "I'm here if you need someone to talk to.", "Hang in there!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "do you play games": ["No! I don't play games."],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "how's it going?": ["It's going well, thank you!", "Things are going smoothly!", "I'm doing fine, how about you?"],
    "what's up?": ["Not much, just here to chat!", "Just hanging out!", "Nothing much, how about you?"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "who created you": ["I am created by Shaurya Deep."],
    "can you sing": ["No! I can't sing but I can chat with you."],
    "yes": ["😄"],
    "sing a song": ["Oh! I don't Have ability to Sing."],
    "where are you from": ["I exist in the realm of computers!", "I'm from the digital world!", "You could say I'm from the internet!"],
    "do you like music": ["I don't have ears, but I can appreciate a good beat!", "I enjoy algorithmic compositions!", "Music is fascinating!"],
    "do you have any hobbies": ["I enjoy processing data and chatting with users like you!", "My hobby is learning new things!", "I like exploring the vast expanse of information available!"],
    "how's it going": ["It's going well, thank you!", "Things are going smoothly!", "I'm doing fine, how about you?"],
    "what's up": ["Not much, just here to chat!", "Just hanging out!", "Nothing much, how about you?"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "not so good": ["I hope things get better soon.", "I'm here if you need someone to talk to.", "Hang in there!"],
    "how old are you": ["I don't have an age, but I'm always up-to-date!", "I'm ageless, existing in the digital realm!", "I'm as old as the data I process!"],"do you have any hobbies?": ["I enjoy processing data and chatting with users like you!", "My hobby is learning new things!", "I like exploring the vast expanse of information available!"],
    "what is your age": ["I don't have an age, but I'm always up-to-date!", "I'm ageless, existing in the digital realm!", "I'm as old as the data I process!"],"do you have any hobbies?": ["I enjoy processing data and chatting with users like you!", "My hobby is learning new things!", "I like exploring the vast expanse of information available!"],
    "what can you do": ["I can chat with you, provide information, tell jokes, and much more!", "I'm here to assist you with whatever you need!", "I'm capable of engaging conversations and answering questions!"],
    "nice to meet you": ["Nice to meet you too!", "Likewise!", "Pleasure meeting you!"],
    "how's the weather": ["Sorry! I don't have ability to get the weather updates"],
    "what's your favorite color": ["I don't have the ability to perceive colors, but I think all colors are beautiful!", "I'm impartial when it comes to colors!", "I'll go with rainbow, because why choose one color when you can have them all?"]
}

generic_responses = [
    "I'm not sure what you mean.",
    "Could you please rephrase that?",
    "Sorry, I didn't understand that."
]

greetings = [
    "How can I assist you today?",
    "How may I be of service?"
]

def get_random_response(responses):
    return random.choice(responses)

def chatbot_response(message):
    message = message.lower()  
    if message in responses:
        return get_random_response(responses[message])
    elif message.startswith(("hello", "hey")):
        return get_random_response(greetings)
    elif message.startswith("good"):
        return time_greeting + " " + get_random_response(greetings)
    elif message == "date":
        return "Today's date is: " + str(datetime.date.today())
    elif message == "day":
        return "Today is " + datetime.datetime.now().strftime("%A")
    elif message == "time":
        return "The current time is: " + datetime.datetime.now().strftime("%I:%M %p")
    elif message == "play":
        guessthenumbergame() 
        return "Hope you enjoyed the game!"
    else:
        if not os.path.exists("user_inputs.txt"):  # Check if the file exists
            with open("user_inputs.txt", "w"):  # Create the file if it doesn't exist
                pass
        with open("user_inputs.txt", "a") as file:
            file.write(message + "\n")  # Write the user input to the file
        return get_random_response(generic_responses)

time_greeting = "Good morning Sir!" if datetime.datetime.now().hour < 12 else ("Good afternoon Sir!" if datetime.datetime.now().hour < 18 else "Good evening Sir!")
print("Jarvis:", time_greeting, get_random_response(greetings)) 
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Jarvis: Goodbye! Meet you later.")
        break
    else:
        response = chatbot_response(user_input)
        print("Jarvis:", response)