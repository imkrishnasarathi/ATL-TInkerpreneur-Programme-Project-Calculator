from tkinter import *

root = Tk()
root.minsize(500, 700)
root.maxsize(500, 700)

display = Label(root, text='0', font="monospace 25 bold", background='#517059', height=2, anchor='w', width=22)
display.grid(columnspan=4, row=0, pady=35, padx=23)

buttons = Frame(root, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=200, height=100)
buttons.grid(columnspan=4, row=1)

btnClear = Button(buttons, text='C', width=30, height=3)
btnClear.grid(row=0, columnspan=3)

btnDivide = Button(buttons, text='/', height=3, width=10)
btnDivide.grid(row=0, column=3)



root.mainloop()