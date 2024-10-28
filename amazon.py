import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Amazon URL to scrape (replace with the actual product page or search URL)
url = "https://www.amazon.com/s?k=smartphone"

# Add headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Send a request to the Amazon page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Parse product data (modify selectors based on Amazon page structure)
products = soup.find_all("div", {"data-component-type": "s-search-result"})

# Create the root element of the XML document
root = ET.Element("products")

for product in products:
    try:
        # Extract product details
        title = product.h2.text.strip()
        price = product.find("span", class_="a-price-whole").text.strip() if product.find("span", class_="a-price-whole") else "N/A"
        rating = product.find("span", class_="a-icon-alt").text.strip() if product.find("span", class_="a-icon-alt") else "N/A"
        
        # Create a product element
        product_elem = ET.SubElement(root, "product")
        
        # Add title, price, and rating to the product element
        ET.SubElement(product_elem, "title").text = title
        ET.SubElement(product_elem, "price").text = price
        ET.SubElement(product_elem, "rating").text = rating
    except Exception as e:
        print(f"Error processing product: {e}")

# Create the tree structure and write it to an XML file
tree = ET.ElementTree(root)
tree.write("amazon_products.xml", encoding="utf-8", xml_declaration=True)

print("Data scraped and saved to amazon_products.xml")
