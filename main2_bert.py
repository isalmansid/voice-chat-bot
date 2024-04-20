import speech_recognition as sr
import pyttsx3
from transformers import BertTokenizer, BertForQuestionAnswering

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = BertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

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
    # Here you would use BERT to generate a response based on the input_text
    # For simplicity, let's just echo the input_text
    return input_text

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
