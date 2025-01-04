import speech_recognition as sr
import pyttsx3
import random
import keyboard  # to capture keyboard events

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and transcribe spoken language to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from the recognition service.")
            return ""

# Function to ask an addition question and check the answer
def ask_question():
    # Generate two random single-digit numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    correct_answer = num1 + num2

    # Ask the question
    speak(f"What is {num1} plus {num2}?")
    print(f"Question: What is {num1} + {num2}?")

    # Get the user's answer
    user_input = listen()

    try:
        # Convert the user input to an integer
        user_answer = int(user_input)
    except ValueError:
        speak("Sorry, I didn't catch a number. Let's try another question.")
        return

    # Check if the answer is correct
    if user_answer == correct_answer:
        speak("Correct! Well done.")
    else:
        speak(f"That's incorrect. The correct answer was {correct_answer}.")

# Main function to handle the quiz
def addition_quiz():
    speak("Hello! Let's do some addition practice. Say 'exit' anytime to stop.")
    
    while True:
        ask_question()
        
        # Check if 'q' key is pressed to quit the program
        if keyboard.is_pressed('q'):
            speak("Goodbye! Exiting now.")
            break

# Start the addition quiz
addition_quiz()
