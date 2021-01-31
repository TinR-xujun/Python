# import pyaudio
# import wave
# import sys
# chunk = 1024
# wf = wave.open('D:/CloudMusic/shot.mp3', 'rb')
# p = pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#         channels=wf.getnchannels(),
#         rate=wf.getframerate(),
#         output=True)
# data = wf.readframes(chunk)
# while len(data) > 0:
#   stream.write(data)
#   data = wf.readframes(CHUNK)
# stream.stop_stream()
# stream.close()
# p.terminate()


# from playsound import playsound

# playsound('D:/CloudMusic/shot.mp3')

from pygame import mixer 


mixer.init()
mixer.music.load('D:/CloudMusic/shot.mp3')
mixer.music.play()
