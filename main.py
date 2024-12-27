'''
Author: Kyle Yang
Creation Date: September 6th, 2021
Last Modified: September 9th, 2021
Project Description: A robotic dog that responds to your questions and messages.
The dog version of an Amazon Echo or Google Home.
Instructions: Press space to talk to the dog and ask questions.
Press tab to make a custom message for the dog.
You can also ask questions like "How are you?", "What is your favorite food?",
"What is your favorite color?", and "What is your favorite sport?".
Credits: None
Updates: None
Rubric Item:
    Functions: Line 24, Line 60, Line 64, Line 68, Line 104
        Built-in function used: Line 68, Line 104
        main() used: Line 24
        Custom function returns a value: Line 60, Line 64
    Dictionary: Line 56
        Contains a list: Line 136, Line 138
        Lists are looped: Line 108, Line 126
        Methods Used: Line 134
'''

from cmu_graphics import *

def main():
    while len(app.dogName) == 0:
        app.dogName = app.getTextInput("What is your name?")
        if len(app.dogName) != 0:
            app.message = getRandomGreeting() + ", Press 'space' to ask questions. Press 'tab' to add messages."
            text.value = ""

# globals
app.guesses = 0
app.dogName = ''
app.message = ""

# objects
text = Label("",200,350)

# groups
dog = Group(Circle(200,200,100,fill='blue',border='black'),
            Line(150,100,50,250,lineWidth=25),
            Line(250,100,350,250,lineWidth=25),
            Circle(200,230,50),
            Oval(200,220,150,100,fill='blue'),
            Circle(175,175,25,fill='white',border='black'),
            Circle(225,175,25,fill='white',border='black'),
            Circle(175,175,10),
            Circle(225,175,10),
            Circle(200,225,25))

# lists
greetings = ["Hi", "Hello", "What's up", "Hey there", "G'day"]
exclamations = ["Cool!", "Nice!", "Ok!", "That's awesome!", "Wow!"]
incorrections = ["Nice Try!", "Nope!", "Incorrect!", "Wrong!", "Haha! I guess you'll never know!"]

# dictionaries
customMessages = {}

# functions
def getRandomGreeting():
    # Gets a random greeting from the list that's called greetings.
    greeting = choice(greetings)
    return greeting

def getRandomExclamation():
    # Gets a random exclamation from the list that's called exclamations.
    exclamation = choice(exclamations)
    return exclamation

# onStep
def onStep():
    if len(text.value) < len(app.message):
        text.value += app.message[len(text.value)]
    else:
        if app.message == "I'm feeling great! How about you?":
            feeling = app.getTextInput("How are you?")
            app.message = feeling + "? " + getRandomExclamation()
            text.value = ""
        if app.message == "Guess! Or you'll never know the answer!" or app.message in incorrections:
            if app.guesses < 5:
                guess = app.getTextInput("What is the dog's favorite food?")
                if guess == "Pork":
                    app.message = "Correct! You got it right! My favorite food is pork."
                else:
                    app.message = incorrections[app.guesses]
                    app.guesses += 1
            else:
                app.message = "Okay, fine! I'll tell you! My favorite food is pork."
                app.guesses = 0
            text.value = ""
        if app.message == "My favorite color is blue. What is your favorite color?":
            color = app.getTextInput("What it your favorite color?")
            if color == "Blue":
                app.message = getRandomExclamation() + " My favorite color is blue too!"
            else:
                app.message = color + "? " + getRandomExclamation()
            text.value = ""
        if app.message == "My favorite sport is soccer. What is your favorite sport?":
            sport = app.getTextInput("What it your favorite sport?")
            if sport == "Soccer":
                app.message = getRandomExclamation() + " My favorite sport is soccer too!"
            else:
                app.message = sport + "? " + getRandomExclamation()
            text.value = ""

# onKeyPress
def onKeyPress(key):
    if key == 'space':
        question = app.getTextInput("Say Something:")
        if question in customMessages:
            app.message = choice(customMessages[question])
        elif question in greetings:
            app.message = getRandomGreeting() + ", " + app.dogName
        elif question == "How are you?":
            app.message = "I'm feeling great! How about you?"
        elif question == "What is your favorite food?":
            app.message = "Guess! Or you'll never know the answer!"
        elif question == "What is your favorite color?":
            app.message = "My favorite color is blue. What is your favorite color?"
        elif question == "What is your favorite sport?":
            app.message = "My favorite sport is soccer. What is your favorite sport?"
        else:        
            app.message = getRandomExclamation()
        text.value = ""
    if key == 'tab':
        message = app.getTextInput("What should the message be?")
        response = app.getTextInput("What should the response be?")
        if message in customMessages:
            answer = app.getTextInput('Looks like you already have a response for this message.\
            Would you like to add a new response or would you like to start a new response for this message?\
            If you add a new response, one of your responses will be selected at random.\
            (Type in "Add new response").\
            If you start a new response, only the response you just entered will be selected.\
            (Type in "Start new response").')
            if answer == "Add new response":
                customMessages[message].append(response)
            if answer == "Start new response":
                customMessages[message] = [response]
        else:
            customMessages[message] = [response]




main()


cmu_graphics.run()
