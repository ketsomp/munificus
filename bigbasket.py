from bs4 import BeautifulSoup
import requests

def bigbasket(item):
    results=[]

    #  the following part is user specific
    #  go to this site https://httpbin.org/get
    #  and copy the part in "user-Agent" and put the full line in the headers variable given below 
    headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", }

    # the next line is to make the url work for any product the user inputs
    # this formatting was done by simply observing url of multiple different searches 

    url="https://www.bigbasket.com/ps/?q={prod}&nc=as".format(prod=item)

    page = requests.get(url, headers=headers) #pulls apge request
    soup1 = BeautifulSoup(page.content, "html.parser") # pulls data from page 


    data=soup1.find_all('li',{'class':"PaginateItems___StyledLi-sc-1yrbjdr-0 dDBqny"})

    if page.status_code==200:
        print("Big Basket connected")
    else:
        print("Failed to connect to Big Basket:",page.status_code)


    # extractor function for all the values we will need 
    def bigbasket(item):
        res=[]
        title=''
        price=''
        ratings=''
        delivery='' 
        link=''
        try:
            title = item.find('h3',{'class':"block m-0 line-clamp-2 font-regular text-base leading-sm text-darkOnyx-800 pt-0.5 h-full"}).get_text()
            price = item.find('span',{'class':"Label-sc-15v1nk5-0 Pricing___StyledLabel-sc-pldi2d-1 gJxZPQ AypOi"}).get_text()
            ratings=item.find('span',{'class':"Label-sc-15v1nk5-0 gJxZPQ"}).get_text()
            link= "https://www.bigbasket.com"+ item.a.get("href")

        except:
            if title==None:
                title='' 
            if price==None:
                price='' 

            if ratings==None:
                ratings='' 
            if link==None:
                link='' 
        res.append(2)
        res.append(title.strip())
        res.append(price.strip()[1:])
        res.append(ratings.strip())
        res.append(link.strip())
        res.append(None)
        return res


    # this part basically runs the extractor 5 times to give top 5 search results, is dynamic 
    for i in range(5):
        try:
            results.append(bigbasket(data[i]))
        except:
            print('Big Basket Fetch Error!')
    return results

print(bigbasket('iphone 14'))
