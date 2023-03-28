from tkinter import *

def configureWindow(window):

    previousInputFrame = Frame(window, width=400, height=50, bg='grey85')
    previousInputFrame.pack(side=TOP)

    inputFrame = Frame(window, width=400, height=70, bg='grey60')
    inputFrame.pack(side=TOP)

    input = StringVar()
 
    previousResultField = Label(previousInputFrame)
    inputField = Label(inputFrame, font=('arial', 18, 'bold'), textvariable=input, justify=RIGHT)
    
    #inputField.grid(row=0, column=0)
    #inputField.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
    
    buttonFrame = Frame(window, width=400, height=500, bg='grey90')
    buttonFrame.pack(side=BOTTOM)
    
    clear = Button(buttonFrame, text = 'C', width = 32, height = 3, bd = 0, bg = '#eee', font='arial 12', command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
    divide = Button(buttonFrame, text = '/', width = 9, height = 3, bd = 0, bg = '#eee', font='arial 12', command = lambda: btn_click('/')).grid(row = 0, column = 3, padx = 1, pady = 1)
    
    num7 = Button(buttonFrame, text = '7', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
    num8 = Button(buttonFrame, text = '8', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
    num9 = Button(buttonFrame, text = '9', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
    multiply = Button(buttonFrame, text = '*', width = 9, height = 3, bd = 0, bg = '#eee', font='arial 12', command = lambda: btn_click('*')).grid(row = 1, column = 3, padx = 1, pady = 1)
    
    num4 = Button(buttonFrame, text = '4', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
    num5 = Button(buttonFrame, text = '5', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
    num6 = Button(buttonFrame, text = '6', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
    minus = Button(buttonFrame, text = '-', width = 9, height = 3, bd = 0, bg = '#eee', font='arial 12', command = lambda: btn_click('-')).grid(row = 2, column = 3, padx = 1, pady = 1)
    
    num1 = Button(buttonFrame, text = '1', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
    num2 = Button(buttonFrame, text = '2', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
    num3 = Button(buttonFrame, text = '3', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
    plus = Button(buttonFrame, text = '+', width = 9, height = 3, bd = 0, bg = '#eee', font='arial 12', command = lambda: btn_click('+')).grid(row = 3, column = 3, padx = 1, pady = 1)
    
    negate = Button(buttonFrame, text = '+/-', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(0)).grid(row = 4, column = 0, padx = 1, pady = 1)
    num0 = Button(buttonFrame, text = '0', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click(0)).grid(row = 4, column = 1, padx = 1, pady = 1)
    dot = Button(buttonFrame, text = '.', width = 9, height = 3, bd = 0, bg = 'grey100', font='arial 12 bold', command = lambda: btn_click('.')).grid(row = 4, column = 2, padx = 1, pady = 1)
    equal = Button(buttonFrame, text = '=', width = 9, height = 3, bd = 0, bg = 'lightblue', font='arial 12', command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
