from tkinter import *
window=Tk()#creates window
window.geometry("500x500")#the measureemnts of the window
window.title("order your pizza :)")
window.config(background="pink")

def calculateprice():
    pizza=spinboxone.get()
    sizep=size.get()
    if pizza=="margherita":
        if sizep=="small":
            pprice=6
        elif sizep=="medium":
            pprice=7
        elif sizep=="large":
            pprice==8
    
        

heading=Label(window,text="TYPE OF PIZZA",font=("Arial",20),background="pink",foreground="dark green")
heading.place(x=50,y=150)
spinboxone=Spinbox(window,values=("margherita","veg extravaganza","marinara","peperoni","hawaiian"),command=None)
spinboxone.place(x=260,y=150)
pamount=Label(window,text="QUANTITY",font=("Arial",20),background="pink",foreground="dark green")
pamount.place(x=50,y=200)
spinboxtwo=Spinbox(window,from_=0,to=10)
spinboxtwo.place(x=260,y=200)
sizep=Label(window,text="SIZE",font=("Arial",20),background="pink",foreground="dark green")
sizep.place(x=50,y=250)

size=StringVar()
size.set("small")
radioone=Radiobutton(window,text="small",value="S",variable=size)
radiotwo=Radiobutton(window,text="medium",value="M",variable=size)
radiothree=Radiobutton(window,text="large",value="L",variable=size)



radioone.place(x=150,y=250)
radiotwo.place(x=150,y=275)
radiothree.place(x=150,y=300)

submit_button=Button(window,text="calculate total price",command=None)
submit_button.place(x=170,y=350)

window.mainloop()
