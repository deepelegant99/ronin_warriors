
import requests
from bs4 import BeautifulSoup

# Example URL for cat-related search on eBay
url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=ronin+warriors&_sacat=0&rt=nc&_udhi=30"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract relevant data (modify as needed)
product_items = soup.select(".s-item__info.clearfix")
for item in product_items:
    # Extract product title
    product_title = item.select_one("a.s-item__link").text.strip()
    product_title = product_title.replace("Opens in a new window or tab", "")


    # Extract product price (if available)
    product_price_element = item.select_one(".s-item__price")
    product_price = product_price_element.text.strip() if product_price_element else "N/A"


    # Extract product price (if available)
    product_price_element = item.select_one(".s-item__price")
    product_price = product_price_element.text.strip() if product_price_element else "N/A"

    # Extract product URL
    product_url = item.select_one("a.s-item__link")["href"]


    print(f"Product Title: {product_title}")
    print(f"Product Price: {product_price}")
    print(f"Product URL: {product_url}")
    print("-" * 30)
