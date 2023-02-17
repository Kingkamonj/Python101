from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk() #mainprogram
GUI.title('Shopping_list') #name of program
GUI.geometry('500x400')#size of program


L1 = Label(GUI,text='Shopping list', font=('Time new roman',30), fg='red')
L1.place(x=30,y=20)


########################
def Button1():
    text = 'Date of spending money'
    messagebox.showinfo('Shopping day', text)
    
FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B1 = ttk.Button(FB1, text = 'Date', command=Button1)
B1.pack(ipadx=20,ipady=20)

########################

########################
def Button2():
    text = 'what did you buy'
    messagebox.showinfo('shopping_list', text)
    
FB2 = Frame(GUI)
FB2.place(x=100,y=160)
B2 = ttk.Button(FB2, text = 'Price', command=Button2)
B2.pack(ipadx=20,ipady=20)

########################

########################
def Button3():
    text = 'How many or How much'
    messagebox.showinfo('number of products', text)
    
FB3 = Frame(GUI)
FB3.place(x=100,y=240)
B3 = ttk.Button(FB3, text = 'Number', command=Button3)
B3.pack(ipadx=20,ipady=20)

########################


########################
def Button4():
    text = 'Where to go'
    messagebox.showinfo('Where to find the product', text)
    
FB4 = Frame(GUI)
FB4.place(x=100,y=320)
B4 = ttk.Button(FB4, text = 'Where', command=Button4)
B4.pack(ipadx=20,ipady=20)

########################


GUI.mainloop()



