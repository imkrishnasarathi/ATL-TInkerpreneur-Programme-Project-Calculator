from tkinter import *

root = Tk()
root.minsize(500, 700)
root.maxsize(500, 700)

display = Label(root, text='0', font="monospace 25 bold", background='#709e7c', height=2, anchor='nw', width=22)
displayHeight = 2
display.grid(columnspan=4, row=0, pady=35, padx=23)

buttons = Frame(root, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=200, height=100)
buttons.grid(columnspan=4, row=1)

# functions
shouldResetDisplay = False
num1 = 0
num2 = 0
displayText = '0'
operator = ''

def onclick(btn):
    global num1, num2, shouldResetDisplay,displayHeight, displayText, operator

    if btn[0] == "equal":
        if num1!=0 and num2!=0:
            calculate(num1, num2)

    if btn[0] == "operator":
        operator = btn[1]
        if num1!=0:
            num2 = int(displayText)
        else:
            num1 = int(displayText)
        if shouldResetDisplay:
            display.config(text=str(calculate(num1, num2)))
            displayText = str(calculate(num1, num2))
        else:
            display.config(text='0')
            displayText = '0'
        shouldResetDisplay = False
    elif btn[0] == "number":
        shouldResetDisplay = True
        if len(displayText) % 22 == 0:
            display.config(height=displayHeight+1)
            displayHeight = displayHeight + 1
            displayText = displayText + '\n'
        if btn[1] == '0':
            display.config(text=displayText + btn[1])
            displayText = displayText + btn[1]
        else:
            if displayText == '0':
                display.config(text=btn[1])
                displayText = btn[1]
            else:
                display.config(text=displayText+btn[1])
                displayText = displayText+btn[1]

    elif btn[0] == "clear":
        num1 = 0
        num2 = 0
        shouldResetDisplay = False
        display.config(text="0")
        displayText = '0'
        display.config(height=2)
        displayHeight = 2

def calculate(n1, n2):
    global operator
    match operator:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '/':
            return n1 / n2
        case '*':
            return n1 * n2
        case '':
            return ''

# First row

btnClear = Button(buttons, text='C',width=37, height=5, command=lambda:onclick(['clear', 'C']))
btnClear.grid(row=0, columnspan=3)

btnDivide = Button(buttons, text='/', height=5, width=10, command=lambda:onclick(['operator', '/']))
btnDivide.grid(row=0, column=3)

# Second Row

btnSeven = Button(buttons, text='7', height=5, width=10, command=lambda: onclick(['number', '7']))
btnEight = Button(buttons, text='8', height=5, width=10, command=lambda: onclick(['number', '8']))
btnNine = Button(buttons, text='9', height=5, width=10, command=lambda: onclick(['number', '9']))
btnMultiply = Button(buttons, text='*', height=5, width=10, command=lambda: onclick(['operator', '*']))

btnSeven.grid(row=1, column=0)
btnEight.grid(row=1, column=1)
btnNine.grid(row=1, column=2)
btnMultiply.grid(row=1, column=3)

# Third Row

btnFour = Button(buttons, text='4', height=5, width=10, command=lambda: onclick(['number', '4']))
btnFive = Button(buttons, text='5', height=5, width=10, command=lambda: onclick(['number', '5']))
btnSix = Button(buttons, text='6', height=5, width=10, command=lambda: onclick(['number', '6']))
btnMinus = Button(buttons, text='-', height=5, width=10, command=lambda: onclick(['operator', '-']))

btnFour.grid(row=2, column=0)
btnFive.grid(row=2, column=1)
btnSix.grid(row=2, column=2)
btnMinus.grid(row=2, column=3)

# Fourth Row

btnOne = Button(buttons, text='1', height=5, width=10, command=lambda:  onclick(['number', '1']))
btnTwo = Button(buttons, text='2', height=5, width=10, command=lambda:  onclick(['number', '2']))
btnThree = Button(buttons, text='3', height=5, width=10, command=lambda:  onclick(['number', '3']))
btnAdd = Button(buttons, text='+', height=5, width=10, command=lambda:  onclick(['operator', '+']))

btnOne.grid(row=3, column=0)
btnTwo.grid(row=3, column=1)
btnThree.grid(row=3, column=2)
btnAdd.grid(row=3, column=3)

# Fifth Row

btnZero = Button(buttons, text='0', height=5, width=24, command=lambda: onclick(['number', '0']))
btnDecimal = Button(buttons, text='.', height=5, width=10, command=lambda: onclick(['decimal', '.']))
btnEqual = Button(buttons, text='=', height=5, width=10, command=lambda: onclick(['equal', '=']))

btnZero.grid(row=4, columnspan=2)
btnDecimal.grid(row=4, column=2)
btnEqual.grid(row=4, column=3)

root.mainloop()

