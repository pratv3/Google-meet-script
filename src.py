from tkinter import *
from tkinter import messagebox as tmsg
import os
import time
import pyautogui as key
import webbrowser as web
v=time.strftime("%I:%M")
print(v)       
       
       
r=Tk()
r.title("script for gmeet")
def mk():
    quit()
def run():
    h=tmsg.askokcancel("gmeet","are you sure to run")
    if h==True:
        c=time.sleep(sd.get()*60)
        print(c)
        web.open_new_tab(f"https://meet.google.com/{su.get()}")
        time.sleep(50)
        key.hotkey("ctrl","d")
        key.hotkey("ctrl","e")
        key.click(x=708,y=463)
        time.sleep(op.get()*60)
        key.click(x=612,y=690)
        
       

    else:
        print("operation cancelled by user")
        quit()

    z=sd.get()




   
sd=IntVar()
su=StringVar()
op=IntVar()
tmsg.showinfo("gmeet","plz enter time and code and left time")
b=Label(r,text="code to join").grid(row=0,column=0)
a=Entry(bg="cyan",textvariable=su).grid(row=0,column=1)
add=Label(r,text="Start Time in minutes").grid(row=2,column=0)
nm=Label(r,text="End time in minutes").grid(row=3,column=0)
q=Entry(textvariable=op,bg="yellow").grid(row=3,column=1)
k=Button(r,text="RUN",bg="green",fg="light blue",command=run).grid(row=4,column=0)
mk=Button(r,text="Quit",bg="red",fg="white",command=mk).grid(row=5,column=0)
ent=Entry(textvariable=sd,bg="light blue",).grid(row=2,column=1)
r.mainloop()

