import string
import tkinter
from random import randint,choice
import openpyxl
import xlrd
import xlwt
from xlwt import Workbook
from openpyxl import Workbook


def buttonclick(args):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Account"
    sheet["B1"] = "Password"
    workbook.save("mypasswords.xlsx")
    i=2
    cellx='B'+ str(i)
    while(args!=5):
     if args == 1:
            if(cellx != ''):
                i += 1
                sheet[cellx]= password4

     if args == 2:
            if (cellx != ''):
                i += 1
                sheet[cellx] = password7
     if args == 3:
            if (cellx != ''):
                i += 1
                sheet[cellx] = password10
     if args == 4:
            if (cellx != ''):
                i += 1
                sheet[cellx] = password32

     workbook.save("mypasswords.xlsx")

#window
a = tkinter.Tk()
a.title('Password Genrator')
a.geometry("400x240")
Font1=("Comic Sans MS",20,'bold')
Font2=("Comic Sans MS",10,'bold')
l=tkinter.Label(a,text='Password Genrator',font=Font1).place(x=550,y=100)

#genrator
characters=string.ascii_letters + string.punctuation + string.digits
password4="".join(choice(characters) for x in range(0,4))
password7="".join(choice(characters) for x in range(0,7))
password10="".join(choice(characters) for x in range(0,10))
password32="".join(choice(characters) for x in range(0,32))


#buttons
b7 = tkinter.Button(a,text="Generate  7 digit password",width=30,activebackground='#98d6af',font=Font2,command=lambda:buttonclick(2))
b10 = tkinter.Button(a,text="Generate  10 digit password",width=30,activebackground='#98d6af',font=Font2,command=lambda:buttonclick(3))
b32 = tkinter.Button(a,text="Generate  32 digit password",width=30,activebackground='#98d6af',font=Font2,command=lambda:buttonclick(4))
b4 = tkinter.Button(a,text="Generate  4 digit password",width=30,activebackground='#98d6af',font=Font2,command=lambda:buttonclick(1))
exitbutton = tkinter.Button(a,text="Exit",width=30,activebackground='#98d6af',font=Font2,command=lambda:buttonclick(5))
b4.place(x=300,y=200)
b7.place(x=300,y=250)
b10.place(x=300,y=300)
b32.place(x=300,y=350)
exitbutton.place(x=300,y=500)



# print(password4)
# print(password7)
# print(password10)
# print(password32)
a.mainloop()
