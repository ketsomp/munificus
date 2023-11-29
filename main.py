from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk

root = ctk.CTk()
root.geometry('600x400')
root.title('Munificus')

img = ImageTk.PhotoImage(Image.open("assets/classy munificus.png").resize((200, 200)))
label = Label(root, image=img)
label.pack(padx=100, pady=50)

root.mainloop()