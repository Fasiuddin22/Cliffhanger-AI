import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Label
import wikipedia
import pywhatkit as kit
from cohere_demo import generate_response as ai
from cohere_demo import generate_response2 as ai2
# from image_generation import generate_image_local, generate_image_api
import mtranslate
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
from datetime import datetime 


now = datetime.now()
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="tensorflow")


# Optimize TensorFlow settings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # Suppress TensorFlow warnings
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Disable oneDNN optimizations

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Use female voice
engine.setProperty('rate', 200)  # Speech rate


# Speak Function
def speak(text):
    translated_text = mtranslate.translate(text, "hi", "en-in") 
    translated_text = text; # Translate to Hindi
    engine.say(translated_text)
    engine.runAndWait()


# Take Command Function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        try:
            # r.pause_threshold = 0.8  # The pause threshold determines how long the recognizer will wait before considering it as a complete phrase.
            audio = r.listen(source, timeout=10, phrase_time_limit=10)  # Increase the timeout here
            # audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            query = mtranslate.translate(query, "en")  # Translate to English
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
            return None
        except sr.RequestError as e:
            print(f"Error with recognition service: {e}")
            return None


# Screenshot Function
def take_screenshot():
    im = pyautogui.screenshot()
    im.save("screenshot.png")
    speak("Screenshot taken and saved as 'screenshot.png'.")
    show_screenshot(im)


# Display Screenshot
def show_screenshot(image):
    root = tk.Tk()
    root.title("Screenshot")
    img = ImageTk.PhotoImage(image)
    label = Label(root, image=img)
    label.image = img
    label.pack()
    root.mainloop()


# Send Email Function
def send_email(to, subject, body):
    sender_email = "YOUR EMAIL ID"  # Replace with your email
    sender_password = "YOUR APP PASSWORD OF EMAIL"  # Replace with your App Password
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, msg.as_string())
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        speak("Sorry, I couldn't send the email.")


# Main JARVIS Function
def main_program():
    jarvis_chat = []  # Store chat history
    speak("Hello, I am Cliffhanger. How can I assist you today?")

    while True:
        query = takeCommand()
        if not query:
            continue

        # Exit Command
        if "exit" in query or "bye" in query:
            speak("Goodbye! Have a nice day.")
            break

        # Music Command
        elif "play music" in query:
            speak("Playing music.")
            webbrowser.open(random.choice([
                # "https://youtu.be/lo-nkVI52-g?si=qqjTArPf8XIeplQW",
                # "https://youtu.be/lo-nkVI52-g?si=qqjTArPf8XIeplQW"
                "https://open.spotify.com/track/4vHRQnzGcKEtqsLH70tAms?si=a6a8aaeb97b04822",
                "https://open.spotify.com/track/7CkRDNQ11p7p2MCOPYDOM1?si=8808e77fe9b54a43"
                # "<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4vHRQnzGcKEtqsLH70tAms?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>"

            ]))

        # Time Command
        elif "time" in query:
            now = datetime.datetime.now()
            speak(f"The time is {now.strftime('%H:%M:%S')}.")

        # Date Command
        elif "date" in query:
            now = datetime.datetime.now()
            speak(f"Today's date is {now.strftime('%d-%m-%Y')}.")

        # To-Do List Commands
        elif "new task" in query:
            speak("What is the task?")
            task = takeCommand()
            if task:
                with open("todo.txt", "a") as f:
                    f.write(task + "\n")
                speak(f"Task '{task}' added to your to-do list.")
        elif "speak tasks" in query:
            try:
                with open("todo.txt", "r") as f:
                    tasks = f.read()
                speak(f"Your tasks are: {tasks}")
            except FileNotFoundError:
                speak("Your to-do list is empty.")

        # Notification Command
        elif "work" in query:
            try:
                with open("todo.txt", "r") as f:
                    tasks = f.read()
                notification.notify(
                    title="Today's Work",
                    message=tasks,
                    timeout=10
                )
            except FileNotFoundError:
                speak("No tasks found.")

        # Open Applications
        elif "open" in query:
            app_name = query.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(app_name)
            pyautogui.press("enter")

        # Screenshot Command
        elif "screenshot" in query:
            take_screenshot()

        # Wikipedia Search
        elif "wikipedia" in query:
            speak("What do you want to search on Wikipedia?")
            topic = takeCommand()
            if topic:
                result = wikipedia.summary(topic, sentences=1)
                speak(result)

        # Google Search
        elif "search google" in query:
            search_query = query.replace("search google about", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        # WhatsApp Message
        elif "send whatsapp" in query:
            
            now = datetime.now()
            kit.sendwhatmsg("+918125922500", "Hi, How are you? I am using Cliffhanger.", now.hour, now.minute + 2, wait_time=20)

        # Email Command
        elif "send email" in query:
            send_email("mdfasiuddin2210@gmail.com", "Test Email", "Hello! This is a test email sent via JARVIS.")

        # AI Query
        elif "ask ai" in query:
            question = query.replace("ask ai", "").strip()
            jarvis_chat.append({"role": "user", "content": question})
            response = ai(jarvis_chat)
            speak(response)

        # Image Generation
        # elif "generate image" in query:
        #     speak("What should the image contain?")
        #     prompt = takeCommand()
        #     speak("Should I use local generation or API?")
        #     method = takeCommand()
        #     if "local" in method:
        #         output_path = generate_image_local(prompt)
        #         speak(f"Image generated and saved as {output_path}.")
        #     elif "api" in method:
        #         api_token = "your_hugging_face_api_token"  # Replace with your API token
        #         output_path = generate_image_api(prompt, api_token)
        #         speak(f"Image generated and saved as {output_path}.")
        #     else:
        #         speak("Invalid method. Please choose between local or API.")

        # Unrecognized Command
        else:
            jarvis_chat.append({"role": "user", "content": query})
            response = ai2(jarvis_chat)
            speak(response)


# Run the Program
if __name__ == "__main__":
    main_program()
