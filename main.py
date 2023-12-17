from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
import search
import random
import math
from test import test,ttest
from flipkart import flipkart
from amazon import amazon
from excel_export import write_product_data_to_excel
from tkinter import messagebox

root = ctk.CTk()
root.geometry('1200x800')
root.title('Munificus')
root.resizable(0,0)

def ham():
    printer_img=ctk.CTkImage(light_image=Image.open('assets/printer.png'),
                        size=(32,32))
    printer_button=ctk.CTkButton(root,image=printer_img,text='',width=32,command=csv)
    printer_button.place(x=10,y=60)

def csv():
    write_product_data_to_excel([element[1:] for element in amzn], [element[1:] for element in flip], "output_file.xlsx")
    messagebox.showinfo('Success!','Written successfully!\nRefer to output_file.csv')


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
    global amzn,flip
    # web scraping file call goes here
    input='laptop' if item_entry.get() is None else item_entry.get()
    amzn=amazon(input)[0:6]
    flip=flipkart(input)[0:6]
    # flip=test('lal')
    # amzn=ttest('lal')
    results=flip+amzn
    results=sorted(results,key=lambda x:x[2])

    for i in range(len(companies)):
        photos.append(ctk.CTkLabel(root,image=
                                   ImageTk.PhotoImage(Image.open(f"assets/{companies[results[i][0]]}.png")
                                                    .resize((200, 200))),text=''))
        names.append(ctk.CTkLabel(root,text=f"{' '.join([str(result) for result in results[i][1].split()[:5]])}",width=30))
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

companies={0:'Amazon',1:'Flipkart',2:'Ebay',3:'Myntra'}

logo_img = ImageTk.PhotoImage(Image.open("assets/properdark munificus.png").resize((200, 200)))
logo_label = Label(root, image=logo_img)
logo_label.pack(padx=100,pady=20)

ham_img=ctk.CTkImage(light_image=Image.open('assets/hamburger.png'),size=(32,32))
ham_button=ctk.CTkButton(root,image=ham_img,text='',width=32,bg_color='#242424',command=ham)
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