from tkinter import *


def get_the_sum(event):
    num1 = int(num_1.get())
    num2 = int(num_2.get())

    sum = num1 + num2

    total_sum.delete(0, "end")
    total_sum.insert(0, sum)


root = Tk()

num_1 = Entry(root)
num_1.pack(side=LEFT)
Label(root, text="+").pack(side=LEFT)

print(num_1)

num_2 = Entry(root)
num_2.pack(side=LEFT)

button_submit = Button(root, text="Equal")
button_submit.bind("<Button-1>", get_the_sum)
button_submit.pack(side=LEFT)

total_sum = Entry(root)
total_sum.pack(side=LEFT)

root.mainloop()
