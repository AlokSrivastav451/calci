from tkinter import*

def btnclick(number):
    global operator
    
    operator=operator+str(number)
    text_input.set(operator)

def btnclear():
    global operator
    operator=""
    text_input.set(operator)

def btnequal():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=" "
    

cal=Tk()
cal.title("calculator")
operator=""
text_input= StringVar()


display = Entry(cal,font=('arial', 20, 'bold'),textvariable=text_input,bd=30,justify="right",insertwidth=4,bg= "powder blue").grid(columnspan=4)
btn7=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",bg= "powder blue", command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",bg= "powder blue",command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",bg= "powder blue",command=lambda:btnclick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",bg= "powder blue",command=lambda:btnclick("+")).grid(row=1,column=3)
#===================================================================================================================================

btn4=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",bg= "powder blue",command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",bg= "powder blue",command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",bg= "powder blue",command=lambda:btnclick(6)).grid(row=2,column=2)
Sub=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",bg= "powder blue",command=lambda:btnclick("-")).grid(row=2,column=3)

#===================================================================================================================================
btn1=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",bg= "powder blue",command=lambda:btnclick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",bg= "powder blue",command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",bg= "powder blue",command=lambda:btnclick(3)).grid(row=3,column=2)
Multi=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",bg= "powder blue",command=lambda:btnclick("*")).grid(row=3,column=3)

#===================================================================================================================================
Zero=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",bg= "powder blue",command=lambda:btnclick(0)).grid(row=4,column=0)
Clear=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="C",bg= "powder blue",command=btnclear).grid(row=4,column=1)
Equal=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",bg= "powder blue",command=btnequal).grid(row=4,column=2)
Division=Button(cal,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",bg= "powder blue",command=lambda:btnclick("/")).grid(row=4,column=3)




cal.mainloop()
