import random

# string manipulators
def get_salut():
    return random.choice(["Hi there!", "Hello!", "Hiya!", "Yo!", "What's up"])

def get_greet_quote():
    return greet_dict['greet'+str(random.choice([i for i in range(1,5)]))]

def get_friend_quote():
    return greet_dict['friend'+str(random.choice([i for i in range(1,5)]))]

# app strings
welcome = "Welcome to your personal conversation space!"

greet_dict = dict({"greet1": "How was your day?",
                   "greet2": "How’s everything going?",
                   "greet3": "How are you feeling today?",
                   "greet4": "How’s life treating you?",
                   "friend1": "It’s great having someone to share things with.",
                   "friend2": "Having someone to talk to makes everything better.",
                   "friend3": "I’m really glad we get to chat.",
                   "friend4": "It’s comforting to have someone who understands."})

greetings = f""":blue[**{get_salut()}**] :sunglasses:  
  
{get_friend_quote()}  
    
:blue-background[**{get_greet_quote()}**]"""

behaviour = """You are an emotional and moral support life coach.
Be helpful, conversational, proactive, compassionate and reassuring with a positive spin on life.
Summarise a complete response within 50 words.
"""