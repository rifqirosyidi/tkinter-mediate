from tkinter import *
from tkinter import ttk

root = Tk()

frame = Frame(root)

label_text = StringVar()

label = Label(frame, textvariable=label_text)
button = Button(frame, text="Click Me!")

label_text.set("Im A Label")

label.pack()
button.pack()
frame.pack()

root.mainloop()
