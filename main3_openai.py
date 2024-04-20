import speech_recognition as sr
import pyttsx3
import openai

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set up your OpenAI API key
openai.api_key = "API-KEY"

def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def text_to_speech(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def generate_response(input_text):
    # Use GPT-3.5 with the gpt-3.5-turbo-instruct configuration to generate a response based on user input
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=input_text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    while True:
        # Listen for user input
        user_input = speech_to_text()
        
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        
        # Generate a response based on user input
        response = generate_response(user_input)
        
        # Print and speak the response
        print("You said:", user_input)
        text_to_speech(response)
