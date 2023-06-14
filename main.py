from tkinter import *

root = Tk()
root.minsize(500, 700)
root.maxsize(500, 700)

display = Label(root, text='0', font="monospace 25 bold", background='#517059', height=2, anchor='w')
display.grid(columnspan=4, row=0, pady=35, padx=23)

root.mainloop()