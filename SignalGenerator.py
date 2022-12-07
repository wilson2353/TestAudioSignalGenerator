from tkinter import *
import pygame.mixer as mixer
import math

# Init mixer
mixer.init()

# Create UI
root = Tk()
root.geometry('300x200')
root.resizable(0,0)
root.attributes('-topmost', 1)
root.title("Signal Generator")

# Define Frame for speration
n_frame = Frame(bg="Black", width=300, height=40).place(x=0,y=0)
f_frame = LabelFrame(text="Source", fg="White", bg="Black", width=300, height=105)
f_frame.place(x=0,y=35)
b_frame = LabelFrame(text="Control", bg="Black", fg="White", width=300, height=60)
b_frame.place(x=0,y=140)

# Create Menu button for Tone Selection
m_btn = Menubutton(root, relief="raised", text='Tone', bg="Grey", fg="White", font=("Georgia", 13), width=7, activebackground="Grey", activeforeground="White")
menu = Menu(m_btn, tearoff=0)
m_btn["menu"] = menu
m_btn.place(x=200,y=100)

# Create Audio Control Buttons
play_btn = Button(b_frame, text='Play', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mixer.music.play(loops=-1))
play_btn.place(x=20,y=2)

stop_btn = Button(b_frame, text='Stop', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mixer.music.stop())
stop_btn.place(x=200,y=2)

def mute():
    volume = mixer.music.get_volume
    if mute_btn["text"] == 'Unmute':
        mixer.music.set_volume(0.0) 
        mute_btn['text'] = 'Muted'
        mute_btn['bg'] = 'Red'
        print(volume)
    elif mute_btn["text"] == 'Muted':
        mixer.music.set_volume(1.0)
        mute_btn['text'] = 'Unmute'
        mute_btn['bg'] = 'Grey'
        print(volume)
    else: return

mute_btn = Button(b_frame, text='Unmute', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mute())
mute_btn.place(x=110,y=2)

# Test Audio
pink_noise = Button(f_frame, text='Pink', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mixer.music.load("mp3/PinkNoise.mp3"))
pink_noise.place(x=20,y=5)

white_noise = Button(f_frame, text='White', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mixer.music.load("mp3/WhiteNoise.mp3"))
white_noise.place(x=110,y=5)

brown_noise = Button(f_frame, text='Brown', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mixer.music.load("mp3/BrownNoise.mp3"))
brown_noise.place(x=200,y=5)

polarity = Button(f_frame, text='Polarity', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mixer.music.load("mp3/PolaritySignal.mp3"))
polarity.place(x=20,y=45)

sweep = Button(f_frame, text='Sweep', font=("Georgia", 13), bg="Grey", fg="White", width=7, command=lambda: mixer.music.load("mp3/sweep.mp3"))
sweep.place(x=110,y=45)

# Options for Tone Selection
menu.add_command(label='100Hz', command=lambda: mixer.music.load("mp3/100Hz.mp3"))
menu.add_command(label='250Hz', command=lambda: mixer.music.load("mp3/250Hz.mp3"))
menu.add_command(label='440Hz', command=lambda: mixer.music.load("mp3/440Hz.mp3"))
menu.add_command(label='1kHz', command=lambda: mixer.music.load("mp3/1kHz.mp3"))
menu.add_command(label='10kHz', command=lambda: mixer.music.load("mp3/10kHz.mp3"))

# Name Display for the Generator
Label(n_frame, text='Test Audio', font=("Georgia", 13), bg="Black", fg="White", width=25).place(x=20,y=10)

root.update()
root.mainloop()