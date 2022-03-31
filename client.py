import socket
from tkinter import *
import tkinter as ttk
from tkinter import filedialog
from  threading import Thread
import random
from PIL import ImageTk, Image
from tkmacosx import Button
import platform

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry("400x400")
    window.configure(bg='LightSkyBlue')
    selectlabel = Label(window, text="Select Music", bg="LightSkyBlue", font=("Calibri",50))
    selectlabel.place(x=2, y=1)
    listbox = Listbox(window, height=10, width=39, activestyle='dotbox', bg='LightSkyBlue', borderwidth=2, font=("Calibri", 10))
    listbox.place(x=10, y=100)
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=0.99)
    scrollbar1.config(command = listbox.yview)
    play_button = Button(window, text = "Play", width=70, bd=1, bg='SkyBlue', font=("Calibri", 10))
    play_button.place(x=30, y=300)
    stop = Button(window, text = "Stop", width=70, bd=1, bg='SkyBlue', font=("Calibri", 10))
    stop.place(x=200, y=300)
    upload = Button(window, text ="Upload", width=70, bd=1, bg='SkyBlue', font=("Calibri", 10))
    upload.place(x=30, y=350)
    download = Button(window, text ="Download", width=70, bd=1, bg='SkyBlue', font=("Calibri", 10))
    download.place(x=200, y=350)
    infoLabel = Label(window, text="", fg="blue", font=("Calibri", 8))
    infoLabel.place(x=4, y=200)
    window.mainloop()
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    
    musicWindow()
    
setup()