import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
a=0
operator = ""

def clickbtnplus():
    global a
    global val
    global operator
    a= int(val)
    operator = "+"
    val = val + "+"
    out.set(val)
def clickbtnmin():
    global a
    global val
    global operator
    a= int(val)
    operator = "-"
    val = val + "-"
    out.set(val)
def clickbtnmul():
    global a
    global val
    global operator
    a= int(val)
    operator = "*"
    val = val + "*"
    out.set(val)
def clickbtndiv():
    global a
    global val
    global operator
    a= int(val)
    operator = "/"
    val = val + "/"
    out.set(val)
def clickbtnC():
    global a
    global val
    global operator
    val = ""
    a= 0
    operator = ""
    out.set(val)

def result():
    global a
    global val
    global operator
    val2 = val
    if operator == "+":
        x=int(val2.split("+")[1])
        y = a+x
        out.set(y)
        val = str(y)
    elif operator == "-":
        x=int(val2.split("-")[1])
        y = a-x
        out.set(y)
        val = str(y)
    elif operator == "*":
        x=int(val2.split("*")[1])
        y = a*x
        out.set(y)
        val = str(y)
    elif operator == "/":
        x=int(val2.split("/")[1])
        if x==0:
            messagebox.showerror("Error","Div by 0 not possible")
            a=0
            val = ""
            operator = ""
        else:
            y = a/x
            out.set(y)
            y = int(a/x)
            val = str(y)

def clickbtn1():
    global val
    val = val + "1"
    out.set(val)
def clickbtn2():
    global val
    val = val + "2"
    out.set(val)
def clickbtn3():
    global val
    val = val + "3"
    out.set(val)
def clickbtn4():
    global val
    val = val + "4"
    out.set(val)
def clickbtn5():
    global val
    val = val + "5"
    out.set(val)
def clickbtn6():
    global val
    val = val + "6"
    out.set(val)
def clickbtn7():
    global val
    val = val + "7"
    out.set(val)
def clickbtn8():
    global val
    val = val + "8"
    out.set(val)
def clickbtn9():
    global val
    val = val + "9"
    out.set(val)
def clickbtn0():
    global val
    val = val + "0"
    out.set(val)

calc = tkinter.Tk()
calc.geometry("250x400+300+300")
calc.resizable(0, 0)
calc.title("Shivanshu Verma")

out= StringVar()
lbl = Label(calc,text= "Calculator", anchor = SE, font= ("Ariel",20), textvariable = out, bg="#ffffff", fg="#000000")
lbl.pack(expand= True, fill = "both")

btnr1 = Frame(calc, bg="#000000")
btnr1.pack(expand=True, fill ="both",)
btnr2 = Frame(calc)
btnr2.pack(expand=True, fill ="both",)
btnr3 = Frame(calc)
btnr3.pack(expand=True, fill ="both",)
btnr4 = Frame(calc)
btnr4.pack(expand=True, fill ="both",)


btn1 = Button(btnr1,text="1", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn1)
btn1.pack(side = LEFT, expand = True, fill= "both")
btn2 = Button(btnr1,text="2", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn2)
btn2.pack(side = LEFT, expand = True, fill= "both")
btn3 = Button(btnr1,text="3", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn3)
btn3.pack(side = LEFT, expand = True, fill= "both")
btnplus = Button(btnr1,text="+", font = ("Ariel",20), relief = GROOVE, border = 0,command = clickbtnplus)
btnplus.pack(side = LEFT, expand = True, fill= "both")

btn4 = Button(btnr2,text="4", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn4)
btn4.pack(side = LEFT, expand = True, fill= "both")
btn5 = Button(btnr2,text="5", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn5)
btn5.pack(side = LEFT, expand = True, fill= "both")
btn6 = Button(btnr2,text="6", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn6)
btn6.pack(side = LEFT, expand = True, fill= "both")
btnmin = Button(btnr2,text="-", font = ("Ariel",20), relief = GROOVE, border = 0,command = clickbtnmin)
btnmin.pack(side = LEFT, expand = True, fill= "both")

btn7 = Button(btnr3,text="7", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn7)
btn7.pack(side = LEFT, expand = True, fill= "both")
btn8 = Button(btnr3,text="8", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn8)
btn8.pack(side = LEFT, expand = True, fill= "both")
btn9 = Button(btnr3,text="9", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn9)
btn9.pack(side = LEFT, expand = True, fill= "both")
btnmul = Button(btnr3,text="*", font = ("Ariel",20), relief = GROOVE, border = 0,command = clickbtnmul)
btnmul.pack(side = LEFT, expand = True, fill= "both")

btnC = Button(btnr4,text="C", font = ("Ariel",20), relief = GROOVE, border = 0,command = clickbtnC)
btnC.pack(side = LEFT, expand = True, fill= "both")
btn0 = Button(btnr4,text="0", font = ("Ariel",20), relief = GROOVE, border = 0, command = clickbtn0)
btn0.pack(side = LEFT, expand = True, fill= "both")
btneq = Button(btnr4,text="=", font = ("Ariel",20), relief = GROOVE, border = 0,command = result)
btneq.pack(side = LEFT, expand = True, fill= "both")
btndiv = Button(btnr4,text="/", font = ("Ariel",20), relief = GROOVE, border = 0,command = clickbtndiv)
btndiv.pack(side = LEFT, expand = True, fill= "both")




calc.mainloop()
