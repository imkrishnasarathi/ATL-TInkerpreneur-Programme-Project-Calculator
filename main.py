from tkinter import *

root = Tk()
root.minsize(500, 700)
root.maxsize(500, 700)

display = Label(root, text='0', font="monospace 25 bold", background='#709e7c', height=2, anchor='w', width=22)
display.grid(columnspan=4, row=0, pady=35, padx=23)

buttons = Frame(root, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=200, height=100)
buttons.grid(columnspan=4, row=1)

# functions

def onClick(btn):
    pass


# First row

btnClear = Button(buttons, text='C', width=37, height=5)
btnClear.grid(row=0, columnspan=3)

btnDivide = Button(buttons, text='/', height=5, width=10)
btnDivide.grid(row=0, column=3)

# Second Row

btnSeven = Button(buttons, text='7', height=5, width=10)
btnEight = Button(buttons, text='8', height=5, width=10)
btnNine = Button(buttons, text='9', height=5, width=10)
btnMultiply = Button(buttons, text='*', height=5, width=10)

btnSeven.grid(row=1, column=0)
btnEight.grid(row=1, column=1)
btnNine.grid(row=1, column=2)
btnMultiply.grid(row=1, column=3)

# Third Row

btnFour = Button(buttons, text='4', height=5, width=10)
btnFive = Button(buttons, text='5', height=5, width=10)
btnSix = Button(buttons, text='6', height=5, width=10)
btnMinus = Button(buttons, text='-', height=5, width=10)

btnFour.grid(row=2, column=0)
btnFive.grid(row=2, column=1)
btnSix.grid(row=2, column=2)
btnMinus.grid(row=2, column=3)

# Fourth Row

btnOne = Button(buttons, text='1', height=5, width=10)
btnTwo = Button(buttons, text='2', height=5, width=10)
btnThree = Button(buttons, text='3', height=5, width=10)
btnAdd = Button(buttons, text='+', height=5, width=10)

btnOne.grid(row=3, column=0)
btnTwo.grid(row=3, column=1)
btnThree.grid(row=3, column=2)
btnAdd.grid(row=3, column=3)

# Fifth Row

btnZero = Button(buttons, text='0', height=5, width=24)
btnDecimal = Button(buttons, text='.', height=5, width=10)
btnEqual = Button(buttons, text='.', height=5, width=10)

btnZero.grid(row=4, columnspan=2)
btnDecimal.grid(row=4, column=2)
btnEqual.grid(row=4, column=3)

root.mainloop()