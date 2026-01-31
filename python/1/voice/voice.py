# this are the a some required the libraries i had imports then 
"""
Docstring for Projects.voice
such as the property are the a 
sounddevices = this the functions that play and records numpy arrays container audio this is used fro a record audio as well as play a adio 


wavio and scipy = are used for a the  save the files in audio formats 
"""

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# give here the frequency 
freq = 44100

# what times wants 
durations = 10

 # Start recorder with the given values 
# of duration and sample frequency
# there rec functions that is the a pre defined as well as a samplerate , channels
"""
rec =records sound from your microphone and stores it in a variable
samplerate=Number of audio samples taken per second Measured in Hz
Number of audio tracks

Channels	          Meaning
1	Mono              (single mic) 🎤 
2	Stereo (         left + right) 🎧
"""
recording = sd.rec(int(durations * freq) , samplerate=freq , channels= 2)



# Record audio for the given number of seconds

sd.wait()


# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav" , freq , recording)



# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)
