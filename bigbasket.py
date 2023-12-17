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

url="https://www.bigbasket.com/ps/?q={prod}&nc=as".format(prod=item)

page = requests.get(url, headers=headers) #pulls apge request
soup1 = BeautifulSoup(page.content, "html.parser") # pulls data from page 


data=soup1.find_all('li',{'class':"PaginateItems___StyledLi-sc-1yrbjdr-0 dDBqny"})


# extractor function for all the values we will need 
def bigbasket(item):
    res=[]
    title=''
    price=''
    ratings=''
    delivery='' 
    try:
        title = item.find('h3',{'class':"block m-0 line-clamp-2 font-regular text-base leading-sm text-darkOnyx-800 pt-0.5 h-full"}).get_text()
        price = item.find('span',{'class':"Label-sc-15v1nk5-0 Pricing___StyledLabel-sc-pldi2d-1 gJxZPQ AypOi"}).get_text()
        ratings=item.find('span',{'class':"Label-sc-15v1nk5-0 gJxZPQ"}).get_text()

    except:
        if title==None:
            title='' 
        if price==None:
            price='' 

        if ratings==None:
            ratings='' 
    res.append(title.strip())
    res.append(price.strip())
    res.append(ratings.strip())
    return res


# this part basically runs the extractor 5 times to give top 5 search results, is dynamic 
for i in range(5):
    results.append(extractor(data[i]))

print(results)
