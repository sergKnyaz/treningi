from os import times
from tkinter import *
import random,time

def bros():
    rang=random.choice(['image//b.png','image//b2.png','image//b3.png','image//b4.png','image//b5.png','image//b6.png'])
    return rang

def push(event):
    global b1,b2
    for i in range(random.randint(10,20)):
        b1=PhotoImage(file=bros())
        b2=PhotoImage(file=bros())
        lab1['image']=b1
        lab2['image']=b2
        root.update()
        time.sleep(0.1)

root=Tk()
root.geometry('400x200')
root.title('БРОСАЙ КОСТИ')
root.resizable(width=False,height=False)
root.iconphoto(True,PhotoImage(file='image//iconka.png'))
font=PhotoImage(file='image//holst.png')
Label(root,image=font).pack()
lab1=Label(root)
lab1.place(relx=0.3,rely=0.5,anchor=CENTER)
lab2=Label(root)
lab2.place(relx=0.7,rely=0.5,anchor=CENTER)
root.bind('<1>',push)
push('')
root.mainloop()