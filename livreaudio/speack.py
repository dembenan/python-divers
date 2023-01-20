from tkinter import *
import pyttsx3
import threading

root = Tk()







class Speaking(threading.Thread):
    def __init__(self, sentence, **kw):
        super().__init__(**kw)
        self.words = sentence.split()
        self.paused = False

    def run(self):
        self.running = True
        while self.words and self.running:
            if not self.paused:
                word = self.words.pop(0)
                print(word)
                engine.say(word)
                engine.runAndWait()
        print("finished")
        self.running = False

    def stop(self):
        self.running = False

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

speak = None

def read():
    global speak
    if speak is None or not speak.running:
        speak = Speaking(text.get(1.0, END), daemon=True)
        speak.start()

def stop():
    global speak
    if speak:
        speak.stop()
        speak = None

def pause():
    if speak:
        speak.pause()

def unpause():
    if speak:
        speak.resume()

engine = pyttsx3.init()

text = Text(width=65, height=20, font="consolas 14")
text.pack()

text.insert(END, "This is a text widget\n"*10)

read_button = Button(root, text="Read aloud", command=read)
read_button.pack(pady=20)

pause_button = Button(root, text="Pause", command=pause)
pause_button.pack()

unpause_button = Button(root, text="Unpause", command=unpause)
unpause_button.pack(pady=20)

stop_button = Button(root, text="Stop", command=stop)
stop_button.pack()

mainloop()