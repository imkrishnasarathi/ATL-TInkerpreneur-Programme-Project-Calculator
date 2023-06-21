from customtkinter import *
import tkinter

set_appearance_mode("dark")
set_default_color_theme("blue")

root = CTk()
root.minsize(480, 620)
root.maxsize(480, 620)

display = CTkLabel(master=root,justify=LEFT, anchor=W, text='0', font=("monospace", 40), height=2, width=420)
displayHeight = 2
display.grid(columnspan=4, row=0, pady=35, padx=23)

buttons = CTkFrame(root, width=90, height=100)
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
        display.configure(height=displayHeight)

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
        display.configure(text=displayText)

    elif btn[0] == "clear":
        num1 = None
        periodEntered = False
        shouldResetDisplay = False
        operator = None
        displayText = '0'
        display.configure(text=displayText)
        display.configure(height=2)
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

        display.configure(text=displayText)

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
                display.configure(text=displayText)
        case '*':
            res = num1 * num2
        case '':
            res = ''
    if int(res) == res:
        res = int(res)
    displayText = str(res)
    display.configure(text=displayText)
# First row

btnClear = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='C',width=360, font=('Helvetica', 20), height=100, command=lambda:onclick(['clear', 'C']))
btnClear.grid(row=0, columnspan=3)

btnDivide = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='/', font=('Helvetica', 20), height=100, width=120, command=lambda:onclick(['operator', '/']))
btnDivide.grid(row=0, column=3)

# Second Row

btnSeven = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='7', font=('Helvetica', 20), height=100, width=120,command=lambda: onclick(['number', '7']))
btnEight = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='8', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['number', '8']))
btnNine = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='9', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['number', '9']))
btnMultiply = CTkButton(buttons, border_color="", corner_radius=12, border_width=4,text='*', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['operator', '*']))

btnSeven.grid(row=1, column=0)
btnEight.grid(row=1, column=1)
btnNine.grid(row=1, column=2)
btnMultiply.grid(row=1, column=3)

# Third Row

btnFour = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='4', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['number', '4']))
btnFive = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='5', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['number', '5']))
btnSix = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='6', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['number', '6']))
btnMinus = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='-', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['operator', '-']))

btnFour.grid(row=2, column=0)
btnFive.grid(row=2, column=1)
btnSix.grid(row=2, column=2)
btnMinus.grid(row=2, column=3)

# Fourth Row

btnOne = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='1', font=('Helvetica', 20), height=100, width=120, command=lambda:  onclick(['number', '1']))
btnTwo = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='2', font=('Helvetica', 20), height=100, width=120, command=lambda:  onclick(['number', '2']))
btnThree = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='3', font=('Helvetica', 20), height=100, width=120, command=lambda:  onclick(['number', '3']))
btnAdd = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='+', font=('Helvetica', 20), height=100, width=120, command=lambda:  onclick(['operator', '+']))

btnOne.grid(row=3, column=0)
btnTwo.grid(row=3, column=1)
btnThree.grid(row=3, column=2)
btnAdd.grid(row=3, column=3)

# Fifth Row

btnZero = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='0', font=('Helvetica', 20),height=100, width=240, command=lambda: onclick(['number', '0']))
btnDecimal = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='.', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['decimal', '.']))
btnEqual = CTkButton(buttons, border_color="", corner_radius=12, border_width=4, text='=', font=('Helvetica', 20), height=100, width=120, command=lambda: onclick(['equal', '=']))

btnZero.grid(row=4, columnspan=2)
btnDecimal.grid(row=4, column=2)
btnEqual.grid(row=4, column=3)

root.mainloop()
