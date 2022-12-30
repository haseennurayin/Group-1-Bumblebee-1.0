import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
import cv2
import numpy as np
import threading
import win32api
from tkinter.filedialog import asksaveasfilename

VIDEO_SIZE = (960, 540)

cap = cv2.VideoCapture(0)

date = datetime.datetime.now()
#filename='E:/project/videos/rec_%s%s%s%s%s%s.avi' % (date.year, date.month, date.day,
                                                     #date.hour, date.minute, date.second)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_rate = 12

out = cv2.VideoWriter()
def change_r():
        if rec_btn['text'] == 'Start Recording':
            start_recording()

            rec_btn.config(text="Stop Recoding")
        else:
            stop_recording()

            rec_btn.config(text="Start Recording")
def change_w():
        if cap_btn['text'] == 'Open webcam':
            start_webcam()

            cap_btn.config(text="Close Webcam")
        else:
            stop_webcam(event)

            cap_btn.config(text="Open webcam")
# --- screen capture
def Cursor_pos(img,center,radius,color,thickness):
    center = tuple(map(int,center))
    rgb = [255*c for c in color[:3]] # convert to 0-255 scale for OpenCV
    alpha = color[-1]
    radius = int(radius)
    if thickness > 0:
        pad = radius + 2 + thickness
    else:
        pad = radius + 3
    roi = slice(center[1]-pad,center[1]+pad),slice(center[0]-pad,center[0]+pad)

    try:
        overlay = img[roi].copy()
        cv2.circle(img,center,radius,rgb, thickness=thickness, lineType=cv2.LINE_AA)
        opacity = alpha
        cv2.addWeighted(src1=img[roi], alpha=opacity, src2=overlay, beta=1. - opacity, gamma=0, dst=img[roi])
    except:
        logger.debug("transparent_circle would have been partially outside of img. Did not draw it.")

def recording_screen():
    global recording
    recording = True
    while recording:
        img = ImageGrab.grab()
        frame = np.array(img)
        _xs,_ys = win32api.GetCursorPos()
        #curpos = root.winfo_pointerx(), root.winfo_pointery()
        Cursor_pos(frame,(_xs,_ys),20,(255,255,0,0.5), -1)
        #cv2.circle(frame, curpos, 10, (0,255,255), 2)
        frame = cv2.resize(frame, VIDEO_SIZE)
        tkimage.paste(Image.fromarray(frame))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

def start_recording():

    if not out.isOpened():
        filename = asksaveasfilename(initialdir = "/",title = "Save as",mode='wb',filetypes = (("Video file","*.avi"),("all files","*.*")),defaultextension=".avi")


        out.open(filename, fourcc, frame_rate, VIDEO_SIZE)
    threading.Thread(target=recording_screen, daemon=True).start()

def stop_recording():
    global recording
    recording = False
    #filename = asksaveasfilename(initialdir = "/",title = "Save as",mode='wb',filetypes = (("Video file","*.avi"),("all files","*.*")),defaultextension=".avi")



# --- webcam

webcam = None
WEBCAM_SIZE = (280, 200)

def read_frame(imgbox):
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, WEBCAM_SIZE)
            image = Image.fromarray(frame)
            imgbox.image.paste(image)
        webcam.after(20, read_frame, imgbox)

def stop_webcam(event):
    global webcam
    if webcam:
        webcam.destroy()
        webcam = None

def start_webcam():
    global webcam
    if webcam is None:
        webcam = tk.Toplevel()
        webcam.geometry('{}x{}+5+520'.format(WEBCAM_SIZE[0], WEBCAM_SIZE[1]))
        webcam.overrideredirect(1)
        imgbox = tk.Label(webcam)
        imgbox.pack()
        imgbox.image = ImageTk.PhotoImage(image=Image.new('RGB',WEBCAM_SIZE,(0,0,0)))
        imgbox.config(image=imgbox.image)
        webcam.bind('<F8>', stop_webcam)
        read_frame(imgbox)

# --- main

root = tk.Tk()

tkimage = ImageTk.PhotoImage(Image.new('RGB', VIDEO_SIZE, (0,0,0)))

w, h = VIDEO_SIZE
vbox = tk.Label(root, image=tkimage, width=w, height=h, bg='black')
vbox.pack()

frame = tk.Frame(root)
frame.pack()

rec_btn = ttk.Button(frame, text='Start Recording', width=20, command=change_r)
rec_btn.grid(row=0, column=0, padx=10, pady=10)

#stop_btn = ttk.Button(frame, text='stop recording', width=20, command=stop_recording, state='disabled')
#stop_btn.grid(row=0, column=1, padx=10, pady=10)

cap_btn = ttk.Button(frame, text='Open webcam', width=20, command=change_w)
cap_btn.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()

out.release()
cap.release()