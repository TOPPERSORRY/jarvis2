import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)     
engine.setProperty("rate",140)  

def wishMe():
     hour = int(datetime.datetime.now().hour) 
     if hour>=0 and hour<12:
          speak("Good Morning!") 

     elif hour>=0 and hour<18:
          speak("Good Afternoon!")

     else:
          speak('Good Evening!')

     speak("I am JARVIS Please tell how may i help you")

def takeCommand():
  

     try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
     except Exception as e:

          print(e)
         

def speak(audio):
     engine.say(audio)
     engine.runAndWait()
     engine.setProperty("rate",140)

if __name__ == "__main__":  
    wishMe()
   
    while True :
   
         query =  takeCommand().lower()
         if 'wikipedia' in query:
              speak("Searching Wikipedia....")
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query,sentences=10)
              speak("according to wikipedia")
              print(results)
              speak(results)

   

         elif 'open youtube' in query:
             speak("opening Youtube")
             webbrowser.open("https://youtube.com/")

         elif 'How are you' in query:
             speak("I am fine sir, how are you ")      
            
         elif 'open google' in query:
              speak("Opening Google")
              webbrowser.open("https://www.google.com/")
             
         elif 'open whatsapp' in query:              
             speak("opening whatsapp")
             os.startfile("C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
             
         elif 'open code' in query:
              codePath=("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
              speak("Opening VS code")
              os.startfile(codePath)
              
         elif 'open file' in query:
              speak("Opening Files")
              os.startfile("explorer.exe")
              
         elif 'who are you' in query:
             speak("hi there my name is jarvis an automated text to speech bot. i can search anything on wikipedia just speak like this sharukh khan wikipedia i can open google,whatsapp,chrom etc ")    

         
         elif 'who is amit' in query:
             speak(" Amit is ritvik jain's father")
             
         elif 'who is arpit' in query:
             speak(" arpit is chaman lakho ka bacha")
             
         elif 'open calculator' in query:
              speak("Opening calculator")
              os.startfile("calc.exe")

         elif 'open excel' in query:
              speak("Opening excel")
              os.startfile("excel.exe")     
              
         elif ('the time') in query:
               strTime = datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"Sir, The time is{strTime}") 
         
    
         elif('exit') in query:
              speak("Bye there have a great day")
              break;      

         
       
