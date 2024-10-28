Amazon Product Scraper
This Python script scrapes product information (title, price, and rating) from Amazon search results and saves the data into an XML file.

Features
Scrapes product titles, prices, and ratings from Amazon.
Saves the scraped data into an XML file.
Easy to configure for other product categories or pages on Amazon.
Prerequisites
Before running the script, ensure you have the following dependencies installed:

Python 3.x
Required Python libraries:
requests
BeautifulSoup4
You can install the required libraries using pip:

bash

pip install requests beautifulsoup4
Usage
Clone the repository or download the script.

Modify the URL in the script to the specific Amazon search page or product category you wish to scrape:

python

url = "https://www.amazon.com/s?k=smartphone"
Run the script:
bash

python amazon_scraper.py
After the script has run, it will generate an amazon_products.xml file containing the scraped product data.
Example Output
Here is an example of what the output XML file might look like:

xml

<?xml version="1.0" encoding="utf-8"?>
<products>
  <product>
    <title>Apple iPhone 12 (64GB, Blue) [Locked] + Carrier Subscription</title>
    <price>799.00</price>
    <rating>4.5 out of 5 stars</rating>
  </product>
  <product>
    <title>Samsung Galaxy S21 5G (128GB, Phantom Gray) - Unlocked</title>
    <price>699.00</price>
    <rating>4.7 out of 5 stars</rating>
  </product>
</products>
Important Notes
Legal Disclaimer: This script is for educational purposes only. Scraping Amazon's website may violate their Terms of Service, and excessive scraping may result in your IP address being blocked. Please scrape responsibly.

Anti-Scraping Protection: Amazon has implemented anti-scraping mechanisms such as CAPTCHAs and IP blocking. Consider using proxies and rotating user agents for more advanced use cases.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributions
Feel free to submit pull requests or raise issues if you have suggestions for improvements or encounter any bugs.

