from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry('344x233')
def update():
    messagebox.showinfo('help','updating the GUI')
    root.geometry(f"{width.get()}x{width.get()}")
width = StringVar()
height = StringVar()
Label(root,text = "window Resizer",font = ('Helvetica',18,'bold')).grid(row=0,column = 1)
l1 = Label(root,text = 'width:')
l1.grid(row=2,column = 0)
l2 = Label(root,text = 'height:')
l2.grid(row=3,column =0)
Entry(root,textvar = width).grid(row=2,column = 1)
Entry(root,textvar = height).grid(row=3,column = 1)
Button(root,text = 'Apply',command = update).grid(row=5,column = 1)
root.mainloop()
