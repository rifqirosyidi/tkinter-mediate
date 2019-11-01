from tkinter import *


# ***** Pack Geometry Manager *****
#

root = Tk()

frame_pack = Frame(root)

Label(frame_pack, text="PACK GEO MANAGER", pady=10).pack()
Button(frame_pack, text="Button One").pack(side=LEFT, fill=Y)
Button(frame_pack, text="Button Two").pack(side=TOP, fill=X)
Button(frame_pack, text="Button Three").pack(side=RIGHT, fill=X)
Button(frame_pack, text="Button Four").pack(side=RIGHT, fill=X)

frame_pack.pack()


# ***** GRID *****

Label(root, text="GRID GEO MANAGER", pady=10).pack()

frame_grid = Frame(root)

Label(frame_grid, text="First Name").grid(row=0, column=0, sticky=W, padx=4)
Entry(frame_grid).grid(row=0, column=1, sticky=E, pady=4)

Label(frame_grid, text="Last Name").grid(row=1, column=0, sticky=W, padx=4)
Entry(frame_grid).grid(row=1, column=1, sticky=E, pady=4)

Button(frame_grid, text="Submit", anchor=CENTER).grid(row=3, columnspan=2)
frame_grid.pack()


# SOME EXAMPLE
Label(root, text="FRAME EXP", pady=10).pack()

frame_exp = Frame(root)

Label(frame_exp, text="Description").grid(row=0, column=0, sticky=W)
Entry(frame_exp).grid(row=0, column=1, sticky=E)
Button(frame_exp, text="Submit").grid(row=0, column=8)

Label(frame_exp, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(frame_exp, text="Best", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(frame_exp, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(frame_exp, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(frame_exp, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

Label(frame_exp, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(frame_exp, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(frame_exp, text="Use Voucher").grid(row=3, column=1, sticky=W)

frame_exp.pack()

root.mainloop()
