from Tkinter import Tk, Label, Button, Text
import sys, os

class RPIGUI:
    def __init__(self, master):
        self.master = master
        master.title("RPI-Youtube player")

        self.label = Label(master, text="Type in a valid youtube link")
        self.label.pack()

        self.url = Text(master, height=2, width=30)
        self.url.pack()

        self.greet_button = Button(master, text="Play", command=self.play)
        self.greet_button.pack()


    def play(self):
        url = self.url.get("1.0",'end-1c')
        os.system('omxplayer $(youtube-dl -g -f mp4 {0})'.format(url))

root = Tk()
gui = RPIGUI(root)
root.mainloop()
