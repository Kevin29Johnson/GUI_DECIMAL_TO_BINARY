from tkinter import*
root=Tk()
root.geometry('400x250') 
def disp():
    dec=int(e.get())
    b=bin(dec)[2:]
    l=Label(root,text='Binary equivalnet is:'+b)
    l.grid(row=6,column=3)
def clear():
    e.delete(0,END)
l=Label(root,text='Enter Decimal no:')
l.grid(row=0,column=0)
e=Entry(root)
e.grid(row=1,column=1)
btn=Button(root,text='Convert',padx=10,pady=10,bd=2,fg='red',command=disp)
btn.grid(row=5,column=1)
bclear=Button(root,text='Clear',padx=10,pady=10,bd=2,fg='green',command=clear)
bclear.grid(row=10,column=1)

root.mainloop()
