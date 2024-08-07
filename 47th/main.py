from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import dotenv_values

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8,cs;q=0.7"
}
MIN_PRICE=50000.00


fake_amazon="https://www.amazon.in/GeForce-Trinity-Graphics-Warranty-Extended/dp/B0CRW19Z5D/ref=sr_1_4?crid=3I81I1MKTU67X&dib=eyJ2IjoiMSJ9.-HJn81Zv8WgeI39ZcB07p6T4NNWlwVm59IGbKrps0utCO9WP4W6qfB1og2701_fu5373AuCTznN6w-sdxlrhQAMKGH_OGGfSfzOMGmklP9_9QLfWK8DGzJW-In85YsyhH8KXu3rmaCfteE_T7vVcYHr2cp8H9WpCeE4ID7A-PuQzERduXP-9quzEVqCr7quV7KKo6BXfesrHD_fQYY_R9C_ZtYzVtfrzAy4LMwoAf4c.NO3tZz6LQcrf89Orb3ghumX8ff-VX_Y9I0u6l6PnIEA&dib_tag=se&keywords=graphics+card+4070ti+super&qid=1723004744&sprefix=graphics+card+4070ti%2Caps%2C250&sr=8-4"
config = dotenv_values(".env")
print(config['EMAIL_ADDRESS'])

response=requests.get(url=fake_amazon,headers=headers)
response.raise_for_status()
# print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
print(soup.prettify())
div=soup.find(name="div", class_="a-box-inner")
price=div.find(name="span",class_="a-price-whole").text
price_decimals=div.find(name="span",class_="a-price-fraction").text
full_price=float(price+price_decimals)
print(full_price)

if full_price<MIN_PRICE:
    with smtplib.SMTP(config['SMTP_ADDRESS']) as connection:
        connection.starttls()
        connection.login(user=config['EMAIL_ADDRESS'], password=config['EMAIL_PASSWORD'])
        connection.sendmail(from_addr=config['EMAIL_ADDRESS'], to_addrs=config['RECIEVER_ADDRESS'], msg=f"Price is down for cooker go buy")












