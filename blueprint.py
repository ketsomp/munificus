#the following file is a blueprint i have used to make other files, this has the code for amazon in it but after changing values u can use it for any other site


from bs4 import BeautifulSoup
import requests


results=[]
item=input("Enter item:") # entering the product name 

#  the following part is user specific
#  go to this site https://httpbin.org/get
#  and copy the part in "user-Agent" and put the full line in the headers variable given below 
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", }

# the next line is to make the url work for any product the user inputs
# this formatting was done by simply observing url of multiple different searches 

url="https://www.amazon.in/s?k={prod}&crid=6XILPNWGTG75&sprefix=logitech+b170%2Caps%2C409&ref=nb_sb_noss_1".format(prod=item.replace(' ','+'))

page = requests.get(url, headers=headers) #pulls apge request
soup1 = BeautifulSoup(page.content, "html.parser") # pulls data from page 

# the below commented line makes soup legible for us 
# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#extractign data from soup as an object 
data=soup1.find_all('div',{'data-component-type':"s-search-result"})

# extractor function for all the values we will need 
def extractor(item):
    res=[]
    title=''
    price=''
    ratings=''
    delivery='' 
    try:
        title = item.find('span',{'class':"a-size-medium a-color-base a-text-normal"}).get_text()
        price = item.find('span',{'class':"a-price-whole"}).get_text()
        ratings =item.find('span',{'class':"a-icon-alt"}).get_text()

        # below part has some issues----------------------
        delivery= item.find('span',{'class':"a-color-base a-text-bold"}).get_text()
        #-------------------------------------------------------

    except:
        if title==None:
            title='' 
        if price==None:
            price='' 

        if ratings==None:
            ratings='' 
        if delivery==None:
            delivery='' 
            
    res.append(title.strip())
    res.append(price.strip())
    res.append(ratings.strip())
    res.append(delivery.strip())
    return res
# this part basically runs the extractor 5 times to give top 5 search results, is dynamic 
for i in range(5):
    results.append(extractor(data[i]))
