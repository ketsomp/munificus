from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
import math
from test import test,ttest
from flipkart import flipkart
from amazon import amazon

root = ctk.CTk()
root.geometry('1200x800')
root.title('Munificus')
root.resizable(0,0)

def rating_stars(n,c):
    star = ImageTk.PhotoImage(Image.open("assets/star.png").resize((20, 20)))
    half_star = ImageTk.PhotoImage(Image.open("assets/half-star.png").resize((20, 20)))
    stars=[]
    count=math.trunc(n)
    for i in range(count):
        stars.append(ctk.CTkLabel(root,image=star,text=''))
    if not (float(n)).is_integer():
        stars.append(ctk.CTkLabel(root,image=half_star,text=''))
        count+=1
    print(count)
    print(len(stars))
    for i in range(len(stars)):
        stars[-1].place(x=50+(100*c)+(c*200)+20*i,y=670)
        print('plac')

def get_input():
    # web scraping file call goes here
    input='laptop' if item_entry.get() is '' else item_entry.get()
    print('get',item_entry.get())
    print('input',input)
    amzn=amazon(input)
    flip=flipkart(input)
    # flip=test('lal')
    # amzn=ttest('lal')
    if amzn is None:
        results=flip
    elif flip is None:
        results=amzn
    else:
        results=flip+amzn
    print(results)
    results=sorted(results,key=lambda x:x[2])

    for i in range(4):
        photos.append(ctk.CTkLabel(root,image=
                                   ImageTk.PhotoImage(Image.open(f"assets/{companies[results[i][0]]}.png")
                                                    .resize((200, 200))),text=''))
        names.append(ctk.CTkLabel(root,text=f"{results[i][1]}",width=30))
        rating.append(ctk.CTkLabel(root,text=f"Rating: {results[i][3]}",width=30))
        prices.append(ctk.CTkLabel(root,text=f"Price: {results[i][2]}",width=30))
        delivery_date.append(ctk.CTkLabel(root,text=f"Delivery Date: {results[i][4]}"))
        photos[-1].place(x=50+(100*i)+(i*200),y=350)
        names[-1].place(x=50+(100*i)+(i*200),y=550)
        rating[-1].place(x=50+(100*i)+(i*200),y=600)
        prices[-1].place(x=50+(100*i)+(i*200),y=650)
        delivery_date[-1].place(x=50+(100*i)+(i*200),y=700)
photos=[]
names=[]
prices=[]
delivery_date=[]
rating=[]

companies={0:'Amazon',1:'Flipkart'}

logo_img = ImageTk.PhotoImage(Image.open("assets/properdark munificus.png").resize((200, 200)))
logo_label = Label(root, image=logo_img)
logo_label.pack(padx=100,pady=20)

ham_img=ctk.CTkImage(light_image=Image.open('assets/hamburger.png'))
ham_button=ctk.CTkButton(root,image=ham_img,text='',width=32,bg_color='#242424')
ham_button.place(x=10,y=10)

search_img=ctk.CTkImage(light_image=Image.open('assets/seacher.png'),
                        size=(32,32))
# search_button=ctk.CTkButton(root,image=search_img,text='',width=32,command=get_input)
# search_button.place(x=777,y=256)
search_button=Button(root,text='search',width=32,command=get_input)
search_button.place(x=777,y=256)

item_entry=ctk.CTkEntry(root,width=335,height=40)
item_entry.place(x=433,y=255)

root.mainloop()