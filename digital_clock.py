from tkinter import*
import time
root = Tk()
root.title('Digital clock')
l = Label(root,text = 'this is my digital clock!',font=('Boulder',25,'bold'))
l.grid(row=2,column = 0)
root.geometry('420x150')
root.resizable(1,1)
root.config(bg = 'blue')
label = Label(root,font = ('Boulder',68,'bold'),bg = 'blue',fg = 'white')
label.grid(row=0,column = 0)
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200,digital_clock)
digital_clock()
root.mainloop()
