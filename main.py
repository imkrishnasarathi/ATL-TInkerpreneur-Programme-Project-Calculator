from tkinter import *

root = Tk()
root.minsize(500, 720)
root.maxsize(500, 720)
root.config(background="darkgrey")

display = Label(root, text='0', font="monospace 25 bold", background='#709e7c', height=2, anchor='nw', width=22)
displayHeight = 2
display.grid(columnspan=4, row=0, pady=35, padx=23)

buttons = Frame(root, bd=0, width=190, height=100, background="darkgrey")
buttons.grid(columnspan=4, row=1)

# functions (logic)
shouldResetDisplay = False
num1 = None
displayText = '0'
operator = None
periodEntered = False

def onclick(btn):
    global num1, periodEntered, shouldResetDisplay,displayHeight, displayText, operator

    if len(displayText) > 21 and len(displayText) % 22 == 0:
        displayHeight+=1
        displayText+='\n'
        display.config(height=displayHeight)

    if btn[0] == "operator":
        periodEntered = False
        if operator != None and (not shouldResetDisplay):
            calculate()
        operator = btn[1]
        num1 = float(displayText)
        shouldResetDisplay = True

    elif btn[0] == "equal":
        if operator != None and (not shouldResetDisplay):
            calculate()
        operator = None


    elif btn[0] == "number":
        if shouldResetDisplay:
            displayText = btn[1]
            shouldResetDisplay = False
        else:
            if displayText == "0":
                displayText = btn[1]
            else:
                displayText += btn[1]
        display.config(text=displayText)

    elif btn[0] == "clear":
        num1 = None
        periodEntered = False
        shouldResetDisplay = False
        operator = None
        displayText = '0'
        display.config(text=displayText)
        display.config(height=2)
        displayHeight = 2

    elif btn[0] == "decimal":
        if periodEntered != True:
            if shouldResetDisplay or (displayText == "0"):
                displayText = f"0{btn[1]}"
                periodEntered = True
                shouldResetDisplay = False
            else:
                if displayText == "0":
                    periodEntered = True
                    displayText = btn[1]
                else:
                    periodEntered = True
                    displayText += btn[1]
        else:
            return

        display.config(text=displayText)

def calculate():
    global operator, num1, displayText
    if operator == None or num1 == None:
        return
    num2 = float(displayText)
    res = None

    match operator:
        case '+':
            res = num1 + num2
        case '-':
            res = num1 - num2
        case '/':
            try:
                res = num1 / num2
            except ZeroDivisionError as e:
                displayText = "Cannot divide by Zero"
                display.config(text=displayText)
        case '*':
            res = num1 * num2
        case '':
            res = ''
    if int(res) == res:
        res = int(res)
    displayText = str(res)
    display.config(text=displayText)

#Images of buttons

addImg, divideImg, subtractImg, multiplyImg = PhotoImage('images/add.png'), PhotoImage('images/divide.png'), PhotoImage('images/subtract.png'), PhotoImage('images/multiply.png')

oneImg, twoImg, threeImg = PhotoImage('images/one.png'), PhotoImage('images/two.png'), PhotoImage('images/three.png')
fourImg, fiveImg, sixImg = PhotoImage('images/four.png'), PhotoImage('images/five.png'), PhotoImage('images/six.png')
sevenImg, eightImg, nineImg = PhotoImage('images/seven.png'), PhotoImage('images/eight.png'), PhotoImage('images/nine.png')
clearImg = PhotoImage('images/clear.png')
equal = PhotoImage('images/equal.png')
period = PhotoImage('images/period.png')
zero = PhotoImage('images/zero.png')

# First row

btnClear = Button(buttons, text='C',width=30, font=(20), height=5, background="#333332", foreground="white", command=lambda:onclick(['clear', 'C']))
btnClear.grid(row=0, columnspan=3)

btnDivide = Button(buttons, text='/', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda:onclick(['operator', '/']))
btnDivide.grid(row=0, column=3)

# Second Row

btnSeven = Button(buttons, text='7', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['number', '7']))
btnEight = Button(buttons, text='8', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['number', '8']))
btnNine = Button(buttons, text='9', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['number', '9']))
btnMultiply = Button(buttons, text='*', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['operator', '*']))

btnSeven.grid(row=1, column=0)
btnEight.grid(row=1, column=1)
btnNine.grid(row=1, column=2)
btnMultiply.grid(row=1, column=3)

# Third Row

btnFour = Button(buttons, text='4', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['number', '4']))
btnFive = Button(buttons, text='5', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['number', '5']))
btnSix = Button(buttons, text='6', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['number', '6']))
btnMinus = Button(buttons, text='-', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['operator', '-']))

btnFour.grid(row=2, column=0)
btnFive.grid(row=2, column=1)
btnSix.grid(row=2, column=2)
btnMinus.grid(row=2, column=3)

# Fourth Row

btnOne = Button(buttons, text='1', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda:  onclick(['number', '1']))
btnTwo = Button(buttons, text='2', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda:  onclick(['number', '2']))
btnThree = Button(buttons, text='3', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda:  onclick(['number', '3']))
btnAdd = Button(buttons, text='+', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda:  onclick(['operator', '+']))

btnOne.grid(row=3, column=0)
btnTwo.grid(row=3, column=1)
btnThree.grid(row=3, column=2)
btnAdd.grid(row=3, column=3)

# Fifth Row

btnZero = Button(buttons, text='0', font=(20),height=5, width=19, background="#333332", foreground="white", command=lambda: onclick(['number', '0']))
btnDecimal = Button(buttons, text='.', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['decimal', '.']))
btnEqual = Button(buttons, text='=', font=(20), height=5, width=8, background="#333332", foreground="white", command=lambda: onclick(['equal', '=']))

btnZero.grid(row=4, columnspan=2)
btnDecimal.grid(row=4, column=2)
btnEqual.grid(row=4, column=3)

root.mainloop()
