
from tkinter import *
root = Tk()
def click(event):
    global scvalue
    text = event.widget.cget("text")  # to extract the text from butten
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

#root = Tk()
root.title("calculator")
root.geometry("644x900")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(padx=50, pady=10)   #pad is for margan of box from boundry

f = Frame(root,bg="grey")


b = Button(f,text="9",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="7",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="6",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)


b = Button(f,text="5",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)


b = Button(f,text="4",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="3",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)



b = Button(f,text="2",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="1",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="0",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="+",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="=",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="-",padx=16,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="c",padx=10,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="/",padx=13,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="%",padx=9,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="*",padx=8,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="@",padx=6,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>", click)
f.pack()
f.pack()
root.mainloop()
