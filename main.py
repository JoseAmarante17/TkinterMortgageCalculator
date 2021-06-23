'''
Author: Jose Amarante
Date : 6/17/2021
'''
import tkinter as tk
from tkinter.constants import DISABLED, X, Y
from tkinter import messagebox


# initalizes window
window = tk.Tk()
window.title("Mortgage Calculator")
window.iconphoto(False,tk.PhotoImage(file='folder_home.png'))
#window.configure(background="yellow")
# Sets size of window and locks it to that size
window.resizable(width=False, height=False)
window.geometry('575x700')

# defualt font
fontSet = ('Arial',17,'bold')
inputFont = ('Arial',14,'bold')
headingFontSet = ('Arial',25,'bold','underline')


def labels():
    frameInput = tk.Frame()
    # Heading
    heading = tk.Label(text="Mortgage Calculator",font=(headingFontSet),fg='#2e86c1')
    heading.pack()

    # Lables with corresponding input
    priceLabel = tk.Label(text="Price",font=fontSet, fg='#2e86c1')
    priceLabel.place(x=100,y=100)

    priceInput = tk.Entry(font=inputFont,fg='#2e86c1',border='4')
    priceInput.insert(0,"0")
    priceInput.place(x=300,y=100,height=30)

    # term
    termLabel = tk.Label(text="Term(in years)",font=fontSet, fg='#2e86c1')
    termLabel.place(x=100,y=150)

    termInput = tk.Entry(font=inputFont,fg='#2e86c1',border='4')
    termInput.insert(0,"0")
    termInput.place(x=300,y=150,height=30)


    # interest
    interestLabel = tk.Label(text="Annual Interest %",font=fontSet, fg='#2e86c1')
    interestLabel.place(x=100,y=200)

    interestInput = tk.Entry(font=inputFont,fg='#2e86c1',border='4')
    interestInput.insert(0,"0")
    interestInput.place(x=300,y=200,height=30)

    # down payment
    dwnPymtLabel = tk.Label(text="Down Payment $",font=fontSet, fg='#2e86c1',border='4')
    dwnPymtLabel.place(x=100,y=250)

    dwnPymtInput = tk.Entry(font=inputFont,fg='#2e86c1',border='4')
    dwnPymtInput.insert(0,"0")
    dwnPymtInput.place(x=300,y=250,height=30)

    frameInput.pack()
    
    # output heading
    outPutHeading = tk.Label(text="OUTPUT", font=headingFontSet,fg='#2e86c1')
    outPutHeading.place(x=215,y=290)

    # OUTPUT and is non-interactable
    monthlyLabel = tk.Label(text="Monthly Payment",font=fontSet, fg='#2e86c1')
    monthlyLabel.place(x=100,y=350)

    monthlyOutput = tk.Entry(state='readonly',font=inputFont,border='4')
    monthlyOutput.insert(0,"0")
    monthlyOutput.place(x=300,y=350,height=30)

    
    # total
    totalLabel = tk.Label(text="Total Payments",font=fontSet, fg='#2e86c1')
    totalLabel.place(x=100,y=400)

    totalOutput = tk.Entry(state='readonly',font=inputFont,border='4')
    totalOutput.insert(0,"0")
    totalOutput.place(x=300,y=400,height=30)

    # buttons
    Clear = tk.Button(
        text="Clear",
        width=8,
        height=2,
        font=fontSet,
        bg="red",
        fg="white",
        activebackground="#CD5C5C",
        activeforeground="White",
        border="5",
        command=lambda: clear(priceInput,termInput,interestInput,dwnPymtInput,monthlyOutput,totalOutput)
    )
    # use .place instead of pack to place where ever you want to
    Clear.place(x=140,y=500)

    Calculate = tk.Button(
        text="Calculate",
        width=8,
        height=2,
        font=fontSet,
        fg="white",
        bg="green",
        activebackground="#7CFC00",
        activeforeground="White",
        border="5",
        command = lambda: calc(priceInput,termInput,interestInput,dwnPymtInput,monthlyOutput,totalOutput)
    )
    Calculate.place(x=335,y=500)

def clear(priceInput,termInput,interestInput,downInput,paymentOutput,totalPayment):
    
    # defualt value variable
    entryTest = tk.StringVar()
    entryTest2 = tk.StringVar()
    entryTest3 = tk.StringVar()
    entryTest4 = tk.StringVar()
    entryTest5 = tk.StringVar()
    entryTest6 = tk.StringVar()

    # sets default value
    priceInput.configure(textvariable = entryTest)
    termInput.configure(textvariable = entryTest2)
    interestInput.configure(textvariable = entryTest3)
    downInput.configure(textvariable = entryTest4)
    paymentOutput.configure(textvariable = entryTest5)
    totalPayment.configure(textvariable = entryTest6)

    entryTest.set("0")
    entryTest2.set('0')
    entryTest3.set("0")
    entryTest4.set("0")
    entryTest5.set("0")
    entryTest6.set("0")
    # FORMAT IT

def calc(priceInput,termInput,interestInput,downInput,paymentOutput,totalPayment):
    
     # INPUT VARIABLES
    price = float(priceInput.get())
    term = int(termInput.get())
    interest = eval(interestInput.get())
    downPyt = eval(downInput.get())

    # CALCULATIONS
    priceAfterDown = price - downPyt
    interest = ((interest/12)/100)
    termLoan = term*12
    total = 0
    time = 0
    # FINALY CALC
    try:
        total = priceAfterDown * interest * \
            (((1+interest)**termLoan)/(((1+interest)**termLoan)-1))
        time = priceAfterDown/ total
    except:
        if price == 0:
            # INITS MESSAGE BOX
            messageBox()

        elif term == 0:
            messageBox()

        elif interest == 0:
            messageBox()

        elif downPyt == 0:
            messageBox()
        else:
            print("")

    entryText = tk.StringVar()
    entryText.set(f"${format(total, ',.2f')}")
    paymentOutput.configure(textvariable = entryText)
    # NUMBER OF PAYMENTS LEFT
    totalText = tk.StringVar()
    totalText.set(f"{priceAfterDown/total:.0f}")
    totalPayment.configure(textvariable = totalText)

def messageBox():
    tk.messagebox.showerror(title="Error", message="Fill OUT ALL FIELDS", )


def main():
    labels()
    
    # displays the window
    window.mainloop()

main()
