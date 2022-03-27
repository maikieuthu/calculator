from tkinter import*
window= Tk()
window.title("Calculator")
window.geometry("500x500")
window.resizable(0,0)
#---------------
def btn_click(num):
    global press
    press= press+ str(num)
    input_text.set(press)

def btn_clr():
    global press
    press=" "
    input_text.set(" ")

def btn_equal():
    global press
    result=str(eval(press))
    input_text.set(result)
    press = " "

#---------------
input_text=StringVar()
press=""
#---------------
inputframe= Frame(window, width=312, height=50)
inputframe.pack(side= TOP)
#---------------
inputfield= Entry(inputframe,font=("Arial", 18,"bold"), textvariable=input_text, justify= RIGHT)
inputfield.grid(row=0,column=0,ipady=10)
#---------------
btnframe=Frame(window)
btnframe.pack()
#firstrow---
btn7=Button(btnframe,text="7",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2"
,command = lambda: btn_click(7))
btn7.grid(row=1,column=0,padx = 5, pady = 5)

btn8=Button(btnframe,text="8",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
            command = lambda: btn_click(8))
btn8.grid(row=1,column=1,padx = 5, pady = 5)

btn9=Button(btnframe,text="9",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
command = lambda: btn_click(9))
btn9.grid(row=1,column=2,padx = 5, pady = 5)

multiply=Button(btnframe,text="*",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
command = lambda: btn_click("*"))
multiply.grid(row=1,column=3,padx = 5, pady = 5)

#secondrow---
btn4=Button(btnframe,text="4",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
            command = lambda: btn_click(4))
btn4.grid(row=2,column=0,padx = 5, pady = 5)

btn5=Button(btnframe,text="5",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
            command = lambda: btn_click(5))
btn5.grid(row=2,column=1,padx = 5, pady = 5)

btn6=Button(btnframe,text="6",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
            command = lambda: btn_click(6))
btn6.grid(row=2,column=2,padx = 5, pady = 5)

btn_subtraction=Button(btnframe,text="-",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
                       command=lambda: btn_click("-"))
btn_subtraction.grid(row=2,column=3,padx = 5, pady = 5)

#thirdrow---

btn1=Button(btnframe,text="1",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",command = lambda: btn_click(1))
btn1.grid(row=3,column=0,padx = 5, pady = 5)

btn2=Button(btnframe,text="2",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",command = lambda: btn_click(2))
btn2.grid(row=3,column=1,padx = 5, pady = 5)

btn3=Button(btnframe,text="3",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
            command = lambda: btn_click(3))
btn3.grid(row=3,column=2,padx = 5, pady = 5)

Divide=Button(btnframe,text="/",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
              command=lambda: btn_click("/"))
Divide.grid(row=3,column=3,padx = 5, pady = 5)

#fourthrow---

btn0=Button(btnframe,text="0",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
            command = lambda: btn_click(0))
btn0.grid(row=4,column=0,padx = 5, pady = 5)

Clear=Button(btnframe,text="C",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
                 command = lambda: btn_clr())
Clear.grid(row=4,column=1,padx = 5, pady = 5)

Equal=Button(btnframe,text="=",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
                 command = lambda: btn_equal())
Equal.grid(row=4,column=2,padx = 5, pady = 5)

btn_plus=Button(btnframe,text="+",font=("Arial",13),bg="#dde2eb",fg = "black", width = 5, height = 2,cursor="hand2",
                command=lambda: btn_click("+"))
btn_plus.grid(row=4,column=3,padx = 5, pady = 5)

window.mainloop()