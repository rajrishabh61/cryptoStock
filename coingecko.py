from bs4 import BeautifulSoup
import requests
import csv
class cryptoStock():
    
    def __init__(self):
        # Open CSV file once in constructor
        self.file = open('some.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        # Write header row correctly
        self.writer.writerow(['Coin', 'Price', '24h Change', 'Market Cap'])
            
    def crypsto(self):
        url = "https://www.coingecko.com/"
        response = requests.get(url)   
        soup = BeautifulSoup(response.text, 'html.parser')
        # Loop through each row in the table
        rows = soup.select("table tbody tr")
        seen = set()
        for row in rows:
            # Coin name
            name_tag = row.find("div", class_="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5")
            coin = name_tag.text.strip() if name_tag else None

            # Coin price (stored inside span with data-price-target)
            price_tag = row.find("span", {"data-price-target": True})
            price = price_tag['data-price-target'] if price_tag else None
            change_tag = row.find('span',class_="gecko-up") or row.find('span',class_="gecko-down")
            changein24h = change_tag.text if change_tag else 'N/A'
            marketgap = row.find("span", {"data-price-target":True})
            mrktgap = marketgap.text if marketgap else 'N/A'
            if coin not in seen:
                seen.add(coin)
                print(coin , "||", price , "||", changein24h , "||",  mrktgap)
                self.writer.writerow([coin , price , changein24h, mrktgap])
# Usage
crypto = cryptoStock()
crypto.crypsto()