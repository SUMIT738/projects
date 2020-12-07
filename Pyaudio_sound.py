import pyaudio
import wave
import sys
import cv2
BUFFER_SIZE = 2000

image = cv2.imread(r'C:\Users\sumit kumar\Desktop\ai2.jpg') 
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   
print(cv2.imshow('image', image) )
#cv2.imwrite(r'C:\Users\sumit kumar\Desktop\bird.jpg', image)

    
# Opening audio file as binary data
wf = wave.open(r'C:\Users\sumit kumar\Desktop\world1.wav')

# Instantiate PyAudio
p = pyaudio.PyAudio()
file_sw = wf.getsampwidth()

stream = p.open(format=p.get_format_from_width(file_sw),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
print("VOLUME ON",end="\n")
print("Hi how can i help?")
data = wf.readframes(BUFFER_SIZE)

while data != '':
    stream.write(data)
    data = wf.readframes(BUFFER_SIZE)
print("like a shiri")
stream.stop_stream()
stream.close()

p.terminate

###############################
def act():
    
   image = cv2.imread(r'C:\Users\sumit kumar\Desktop\ai1.png') 
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   
print(cv2.imshow('image', image) )
#cv2.imwrite(r'C:\Users\sumit kumar\Desktop\bird.jpg', image)
act()
