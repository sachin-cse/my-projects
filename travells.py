from tkinter import*
root = Tk()
root.geometry('644x9444')
root.title('travells form')
def click():
    print(e1.get())
    print(e2.get())
    print(e3.get())
    print(e4.get())
    print(e5.get())
    print('You have submitted your form successfully!')
    print('thank you!')
Label(root,text = 'welcome to sachin travell form!',font=25,fg = 'blue',pady = 15).grid(row=0,column = 3)
name = Label(root,text = 'Name:',font = 25)
phone = Label(root,text = 'Phone:',font = 25)
gender = Label(root,text = 'Gender:',font = 25)
emergency = Label(root,text = 'Emergency contact:',font = 25)
mode = Label(root,text = 'Payment mode:',font = 25)
name.grid(row=1,column = 0)
phone.grid(row=2,column = 0)
gender.grid(row=3,column = 0)
emergency.grid(row=4,column = 0)
mode.grid(row=5,column = 0)
namevar = StringVar()
phonevar = StringVar()
gendervar = StringVar()
emergencyvar = StringVar()
modevar = StringVar()
foodservices = IntVar()
e1 = Entry(root,textvar = namevar,font=20)
e1.grid(row=1,column = 3)
e2 = Entry(root,textvar = phonevar,font=20)
e2.grid(row=2,column = 3)
e3 = Entry(root,textvar = gendervar,font=20)
e3.grid(row=3,column = 3)
e4 = Entry(root,textvar = emergencyvar,font=20)
e4.grid(row=4,column = 3)
e5 = Entry(root,textvar = modevar,font=20)
e5.grid(row=5,column = 3)
foodservice = Checkbutton(text = 'want to prebook your meals!',variable = foodservices,onvalue = 1,offvalue = 0,font = 25,fg='blue')
foodservice.grid(row=6,column = 3)
Button(root,text = 'Submit',command = click,fg = 'red').grid(row=12,column = 0)
root.mainloop()
