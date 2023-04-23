import os
from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.nike.com/t/giannis-immortality-basketball-shoes-p9QlJF/CZ4099-400"

html_code = requests.get(url=url).text
soup = BeautifulSoup(html_code, "html.parser")

TARGET_PRICE = float(40)

email = os.environ["EMAIL"]
password = os.environ["EMAIL_APP_PASSWORD"]

product_price = round(float(soup.select_one("div.product-price").getText().strip("$")))
product_title = soup.select_one("h1#pdp_product_title").getText() + " " + soup.select_one("h2.headline-5").getText()

msg = f"Subject:Sale for {product_title}! Buy Now!\n\n{product_title} now only ${product_price}!\nBuy now at {url}"

if product_price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=msg)
        print("Successfully Sent Message")
