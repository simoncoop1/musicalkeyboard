import pyaudio
import wave
import sys
import time
import curses
import os
import threading


def dostuffthread(fname):

    #wf = wave.open("sound1.wav", 'rb')
    wf = wave.open(fname, 'rb')

    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()

#def dostuff():
  

def main(win):
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    while 1:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("@")
           win.addstr(str(key)) 
           ##call a sound
           if key == 'q':
               thread = threading.Thread(target=dostuffthread, args=("1.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start() 
           if key == 'w':
               thread = threading.Thread(target=dostuffthread, args=("2.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()                 
           if key == 'e':
               thread = threading.Thread(target=dostuffthread, args=("3.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'r':
               thread = threading.Thread(target=dostuffthread, args=("4.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start() 
           if key == 't':
               thread = threading.Thread(target=dostuffthread, args=("5.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'y':
               thread = threading.Thread(target=dostuffthread, args=("6.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'u':
               thread = threading.Thread(target=dostuffthread, args=("7.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'i':
               thread = threading.Thread(target=dostuffthread, args=("8.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'o':
               thread = threading.Thread(target=dostuffthread, args=("9.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'p':
               thread = threading.Thread(target=dostuffthread, args=("10.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'a':
               thread = threading.Thread(target=dostuffthread, args=("sound1.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 's':
               thread = threading.Thread(target=dostuffthread, args=("sound2.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == 'd':
               thread = threading.Thread(target=dostuffthread, args=("sound3.wav",))
               thread.daemon = True                            # Daemonize thread
               thread.start()
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass

curses.wrapper(main)



print("ok")
