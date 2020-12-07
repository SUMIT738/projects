import speech_recognition as sr 
  
file = (r'C:\Users\sumit kumar\Desktop\world1.wav')      # use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.AudioFile(file) as source:        #reads the audio file. Here we use record instead of #listen 
    
    audio = r.record(source)   
    print(r.recognize_google(audio))
