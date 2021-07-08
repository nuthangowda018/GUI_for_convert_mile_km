from tkinter import *

window=Tk()
window.title("coverting Miles to Kilometer")
window.minsize(width=400,height=100)
window.config(padx=100,pady=100)


label1=Label(text="miles")
label1.grid(column=3,row=1)

label1=Label(text="is equal to ")
label1.grid(column=1,row=2)

label1=Label(text="km ")
label1.grid(column=3,row=2)

label2= Label(text= 0)
label2.grid(column=2, row=2)

entry=Entry(width=20)
entry.grid(column=2,row=1)

def cal():
    label2["text"]=round(int(entry.get())*1.609)


button=Button(text="calculate",command=cal)
button.grid(column=2,row=3)



window.mainloop()