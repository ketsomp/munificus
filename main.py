from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
import search
import random
import math

root = ctk.CTk()
root.geometry('1200x800')
root.title('Munificus')
root.resizable(0,0)

def rating_stars(n):
    star = ImageTk.PhotoImage(Image.open("assets/star.png").resize((20, 20)))
    half_star = ImageTk.PhotoImage(Image.open("assets/half-star.png").resize((20, 20)))
    stars=[]
    count=math.trunc(n)
    for i in range(count):
        stars.append(ctk.CTkLabel(root,image=star,text=''))
    if not (float(n)).is_integer():
        stars.append(ctk.CTkLabel(root,image=half_star,text=''))
        count+=1
    for i in range(count):
        stars[-1].place(x=50+(100*i)+(i*200)+(20*i),y=670)

def get_input():
    # web scraping file call goes here
    
    for i in range(len(companies)):
        photos.append(ctk.CTkLabel(root,image=
                                   ImageTk.PhotoImage(Image.open(f"assets/{companies[i]}.png")
                                                    .resize((200, 200))),text=''))
        prices.append(ctk.CTkButton(root,text=f"Price: {random.randint(1,500)}"))
        delivery_date.append(ctk.CTkButton(root,text=f"Delivery Date: {random.randint(1,30)}"))

        photos[-1].place(x=50+(100*i)+(i*200),y=350)
        prices[-1].place(x=50+(100*i)+(i*200),y=600)
        delivery_date[-1].place(x=50+(100*i)+(i*200),y=640)
        rating_stars(1)

photos=[]
prices=[]
delivery_date=[]
rating=[]

companies={0:'Amazon',1:'Flipkart',2:'Ebay',3:'Myntra'}

logo_img = ImageTk.PhotoImage(Image.open("assets/properdark munificus.png").resize((200, 200)))
logo_label = Label(root, image=logo_img)
logo_label.pack(padx=100,pady=20)

ham_img=ctk.CTkImage(light_image=Image.open('assets/hamburger.png'))
ham_button=ctk.CTkButton(root,image=ham_img,text='',width=32,bg_color='#242424')
ham_button.place(x=10,y=10)

search_img=ctk.CTkImage(light_image=Image.open('assets/seacher.png'),
                        size=(32,32))
search_button=ctk.CTkButton(root,image=search_img,text='',width=32,command=get_input)
search_button.place(x=777,y=256)

item_entry=ctk.CTkEntry(root,width=335,height=40)
item_entry.place(x=433,y=255)

item_button=Button(root,width=100,text='Enter',command=get_input) # use ctk.CtkButton at the end, 
# ctk glitches out on mac so using ttk button for testing
#item_button.pack(pady=10)

root.mainloop()