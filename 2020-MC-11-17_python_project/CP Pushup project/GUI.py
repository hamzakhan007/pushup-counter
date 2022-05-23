from tkinter import *
import tkinter.filedialog as fd
import os
import pushups

# import tkinter as tk
top=Tk()
top.geometry("600x300")  #gui frame
top.maxsize(600,300)
top.minsize(600,300)

Label(top, text='Pushup Counter',font=('Times New Roman',26,'bold')).pack()

def StartCameraBtnCallBack():
    pushups.Run(0)

def StartVideoBtnCallBack():
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[("All files", "*.mp4*")])
    pushups.Run(os.path.abspath(file))

def ExitBtnCallBack():
    quit()


cameraBtn = Button(top, text = "Count using Camera", command = StartCameraBtnCallBack, fg='white', bg='green', font=('Times New Roman',18,'normal'))
cameraBtn.pack(padx= 10, pady=10) # padding means space

videoBtn = Button(top, text = "Count using Video", command = StartVideoBtnCallBack, fg='white', bg='green', font=('Times New Roman',18,'normal'))
videoBtn.pack(padx= 10, pady=10)

exitBtn = Button(top, text = "Exit", command = ExitBtnCallBack, fg='white', bg='green', font=('Times New Roman',18,'normal'))
exitBtn.pack(padx= 10, pady=10)

mainloop() # start the event loop