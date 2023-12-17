from bs4 import BeautifulSoup as bs
import requests


def flipkart(input):
    link='https://www.flipkart.com/search?q={prod}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'.format(prod=input.replace(' ','+'))
    page=requests.get(link)
    soup=bs(page.content,'html.parser')
    data=soup.find_all('div',class_='_1AtVbE col-12-12')
    results=[]
    if page.status_code==200:
        print("Flipkart connected!")
    else:
        print("Failed to connect to Flipkart:",page.status_code)
    for i in data:
        try:
            name=i.find('div',class_='_4rR01T').get_text()
            rating=i.find('div',class_="_3LWZlK").get_text()
            price=i.find('div',class_="_30jeq3").get_text()
            # if i.find('div',class_='_2kHMtA'):
            #     b=i.find('div',class_='_2kHMtA')
            #     c=b.find('a')['href']
            #     if c:
            #         link=c.get_text()
            n=name.split(' ')[:8]
            l=[1,''.join(x+' ' for x in n),price,rating,None]
            results.append(l)
        except:
            print('Flipkart Fetch Failed!')


    return results

#    product_name = soup.find("span",{"class":"B_NuCI"}).get_text()
# <span class="B_NuCI">
# print(flipkart('laptop'))