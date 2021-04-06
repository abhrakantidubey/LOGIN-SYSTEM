import tkinter as tk
from tkinter import *
import PIL as ImageTK
from tkinter import messagebox

root=tk.Tk()
root.title("Login System")
root.geometry("600x450")


def enter():
	if username.get()=="" or password1.get()=="":
		messagebox.showerror("ERROR","All fields are required ! ")
	elif username.get()=="xyz@gmail.com" or password1.get()=="123456":
		messagebox.showinfo("CONGRATS","LOGIN SUCCESSFUL")
	else:
		messagebox.showerror("ERROR","INVALID USERNAME OR PASSWORD")



#=My Image

photo=PhotoImage(file=r"logo.png")

logo=Label(
	root,
	image=photo).pack()

lbl1= Label(
	root,
	text="LOGIN SYSTEM BY ABHRA",
	font=("Verdana",25,"bold"),
	width=50,
	bg="yellow",
	fg="red",
	relief=SOLID
	)
lbl1.pack(padx=10,pady=15)

username=StringVar()
password1=StringVar()

username1=Entry(
	root,
	text='enter your username',
	font=("Verdana",20,"italic"),
	width=30,
	# bg="#fbc531",
	textvariable=username,
	relief=GROOVE,
	bd=10).pack()

user_txt=Label(
	root,
	text="ENTER YOUR USER NAME",
	font=("Verdana",18,"bold"),
	fg="red"
	)
user_txt.pack()

password=Entry(
	root,
	text='enter your username',
	font=("Verdana",20,"italic"),
	width=30,
	textvariable=password1,
	relief=GROOVE,
	bd=10)
password.pack()

pass_txt=Label(
	root,
	text="ENTER YOUR PASSWORD",
	font=("Verdana",18,"bold"),
	fg="red"
	)
pass_txt.pack()

space=Label(
	root,
	text="").pack()


loginbtn=Button(
	root,
	text="LOGIN",
	font=("Callibri",18,"bold"),
	width=300,
	relief=GROOVE,
	bg="#4cd137",
	bd=3,
	command=enter).pack()






root.mainloop()


