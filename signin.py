from tkinter import *
from PIL import ImageTk
import os
from tkinter import messagebox
from Frame1 import Frame1


# Functionality Part
def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='images/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def onclick():
    print('button is being clicked')
    if usernameEntry.get().strip() and passwordEntry.get():
        print(f'username is {usernameEntry.get()}, password is {passwordEntry.get()}')
        # messagebox.showinfo('Alert', 'Details Valid')
        login_window.destroy()
        
        obj = Frame1()
        obj.create1()
        obj.root.mainloop()
        # signup_window()
    else:
        print('enter details first')
        messagebox.showwarning('Alert', 'Please enter your details first')
    # messagebox.showerror('Alert', 'Please enter your details first. error')

# GUI Part
login_window = Tk()
login_window.geometry('990x660')
login_window.resizable(0, 0)
login_window.title('Login Page')
#img = Image.open(os.path.abspath('bg.jpg')).resize((200, 300))
bgImage = ImageTk.PhotoImage(file='images/bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='SIGN IN', font=('time new roman', 23, 'bold'), bg='white',
                fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('time new roman', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2)
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('time new roman', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)

passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2)
frame2.place(x=580, y=282)

openeye = PhotoImage(file='images/closeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('time new roman', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1')
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19,
                     command= onclick)
loginButton.place(x=578, y=350)

signupLabel = Label(login_window, text="Don't have an account?", font=('time new roman', 9), fg='firebrick1', bg='white')
signupLabel.place(x=590, y=500)
newaccountButton = Button(login_window, text='create new one', font=('time new roman', 9, 'bold underline'), fg='blue',
                          bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                          command=signup_page)
newaccountButton.place(x=727, y=500)
login_window.mainloop()