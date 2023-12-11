from bs4 import BeautifulSoup
import requests

def amazon(item):
    headers={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
    }
    url="https://www.amazon.in/s?k={prod}&ref=nb_sb_noss".format(prod=item.replace(' ','+'))

    page = requests.get(url, headers=headers) #pulls page request
    soup1 = BeautifulSoup(page.content, "html.parser") # pulls data from page 

    data=soup1.find_all('div',{'data-component-type':"s-search-result"})
    if page.status_code==200:
        print("Amazon connected")
    else:
        print("Failed to connect to Amazon:",page.status_code)

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
        res.append(0) # amazon id
        res.append(title.strip())
        res.append(price.strip())
        res.append(ratings.strip().split()[0])
        res.append(delivery.strip())
        return res
    for i in range(5):
        try:
            print(extractor(data[i]))
        except:
            print("Amazon Fetch Error!")
            break