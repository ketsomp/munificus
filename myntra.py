import requests
from bs4 import BeautifulSoup

def scrape_myntra_search(search_query):
    base_url = f"https://www.myntra.com/{search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
    }
    
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        products = soup.find_all("li", class_="product-base")
        print(products)
        
        for product in products:
            product_name = product.find("h3", class_="product-brand").text.strip() if product.find("h3", class_="product-brand") else "N/A"
            product_price = product.find("div", class_="product-productMetaInfo").text.strip() if product.find("div", class_="product-productMetaInfo") else "N/A"
            
            print(f"Product Name: {product_name}")
            print(f"Price: {product_price}")
            print("=" * 30)
    else:
        print("Failed to fetch the page!")

search_query = "men-tshirts"  # Change this to your desired search query
scrape_myntra_search(search_query)
