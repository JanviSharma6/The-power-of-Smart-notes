from tkinter import *
from PIL import ImageTk
#import pymysql
from tkinter import messagebox
import database
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirm_passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are Required')
    elif passwordEntry.get() != confirm_passwordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:
        res = database.register((emailEntry.get(), usernameEntry.get().strip(), passwordEntry.get()))
        if res:
            messagebox.showinfo('Success', 'Register is successful.')
        else:
            messagebox.showerror('Alert', 'Something went wrong')
    
def login_page():
    signup_window.destroy()
    import signin
    import Frame1
signup_window = Tk()
signup_window.title('signup page')
signup_window.resizable(0, 0)
background=ImageTk.PhotoImage(file='images/bg.jpg')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame= Frame(signup_window, bg='white')
frame.place(x=554,y=100)
heading = Label(frame, text='CREATE AN ACCOUNT', font=('time new roman', 18, 'bold'), bg='white',
                fg='firebrick1')
heading.grid(row=0, column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('time new roman', 10, 'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=30,font=('time new roman',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('time new roman', 10, 'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('time new roman',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)


passwordLabel=Label(frame,text='Password',font=('time new roman', 10, 'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('time new roman',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirm_passwordLabel=Label(frame,text='Confirm Password',font=('time new roman', 10, 'bold'),bg='white',fg='firebrick1')
confirm_passwordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirm_passwordEntry=Entry(frame,width=30,font=('time new roman',10,'bold'),fg='white',bg='firebrick1')
confirm_passwordEntry.grid(row=8,column=0,sticky='w',padx=25)
check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),
                              bg='white',fg='firebrick1',activebackground='white',activeforeground='firebrick1'
                               ,cursor='hand2', variable= check)
termsandconditions.grid(row=9,column=0,padx=15,pady=10)

signupButton=Button(frame,text='Signup',font=('open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',
                    activebackground='firebrick1',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text="Don't have an account?",font=('open Sans',9,'bold'),fg='firebrick1',bg='white')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)
loginButton=Button(frame,text='Log in',font=('open Sans',9,'bold underline'),bd=0, cursor ='hand2',fg='blue',bg='white',
                   activebackground='white',activeforeground='blue',command= login_page)
loginButton.place(x=170,y=377)
signup_window.mainloop()





















