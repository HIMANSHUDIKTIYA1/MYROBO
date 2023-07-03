import speech_recognition as sr
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")


def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("listening.../")
    r.pause_threshold=1
    audio = r.listen(source)

    query = r.recognize_google(audio, language="en-in")
    print(f"User said:{query}\n")
        
       
    return query
  

speak.Speak("hy , I AM HD Box dout AI  ")
while True:
  speak.Speak("If ANY QUESTION")

  query=takeCommand()
  speak.Speak(query)
  

