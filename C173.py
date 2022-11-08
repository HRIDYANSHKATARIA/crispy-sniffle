from tkinter import *

root = Tk()
root.title("C173")
root.geometry("400x400")



def show1():
    label1["text"]+="GALAXY"
    
def show2():
    label2["text"]+="I CODE"
    
def show3():
    label3["text"]+="DU PONT"
    
BTN1 = Button(root,text="SHOW HOSPITAL ALLOTED",command="show1")
BTN1.place(relx=0.5,rely=0.2,anchor=CENTER)

label1 = Label(root)
label1.place(relx=0.5,rely=0.3,anchor=CENTER)


BTN2 = Button(root,text="SHOW IT COMPANY ALLOTED",command="show2")
BTN2.place(relx=0.5,rely=0.4,anchor=CENTER)

label2 = Label(root)
label2.place(relx=0.5,rely=0.5,anchor=CENTER)

BTN3 = Button(root,text="SHOW CHEMICAL COMPANY ALLOTED",command="show3")
BTN3.place(relx=0.5,rely=0.6,anchor=CENTER)

label3 = Label(root)
label3.place(relx=0.5,rely=0.7,anchor=CENTER)
    
root.mainloop()
