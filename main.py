import speech_recognition as sr
import os
import sys

# List of offensive words to listen for
offensive_words = ["cheese"]

def shutdown_pc():
    """Function to shut down the computer."""
    os.system("shutdown /s /t 1")  # For Windows
    # os.system("shutdown now")  # Uncomment for Linux

def listen_for_keywords():
    """Function to listen for specific keywords."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for offensive words...")
        while True:
            try:
                audio = recognizer.listen(source)
                recognized_text = recognizer.recognize_google(audio, language='en-US')
                print(f"Recognized: {recognized_text}")

                # Check if any offensive word is in the recognized text
                if any(word in recognized_text for word in offensive_words):
                    print("Offensive word detected! Shutting down...")
                    shutdown_pc()
                    break

            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except KeyboardInterrupt:
                print("Program terminated by user.")
                sys.exit()

if __name__ == "__main__":
    listen_for_keywords()
