import speech_recognition as  sr
import webbrowser
# import pyttsx3
import edge_tts 
import asyncio
import os
import pygame
import pyautogui
from datetime import datetime



recognizer= sr.Recognizer()
voice= "en-US-AriaNeural"

async def speak(text):
    file= "voice.mp3"
    communicate= edge_tts.Communicate(text, voice) 
    await communicate.save(file)
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    pygame.mixer.quit()

    os.remove(file)

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif c.lower()== "open youtube":
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "time" in c.lower():
        current_time =datetime.now().time()
        asyncio.run(speak(str(current_time)))
    elif "date" in c.lower():
        current_date= datetime.now().date()
        asyncio.run(speak(str(current_date)))
    
if __name__=="__main__":
    asyncio.run(speak("your virtual assistant is truned on"))
    while True:
        try:
            with sr.Microphone() as source:
                print("speaking something...")
                recognizer.adjust_for_ambient_noise(source) 
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
            text= recognizer.recognize_google(audio)
            print("recognizing")
            print(text)
            if text.lower()== "jarvis":
                print("jarvis activated")
                asyncio.run(speak("yes, how can i help you"))
                with sr.Microphone() as source:
                    print("speaking something...")
                    recognizer.adjust_for_ambient_noise(source) 
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                    # text= recognizer.recognize_google(audio)

            processcommand(text)
                
                
                


        except sr.WaitTimeoutError:
            print("no command detected")
        except Exception as e:
            print(e)
