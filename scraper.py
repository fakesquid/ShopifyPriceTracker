import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Price Tracker for Haven
# URL of the product
URL = 'PRODUCT_URL'

headers = {INSERT_HEADERS}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# Product Price and Information
product = soup.find("h1", {"itemprop": "name"}).get_text()
original_price = soup.find("div", {"class": "price-main"}).get_text()
converted_original_price = float(original_price[1:7])
sale_price = soup.find("span", {"class": "highlight"}).get_text()
converted_sale_price = float(sale_price[1:7])

def check_price():
	print(product)
	print(converted_sale_price)

	if(converted_sale_price < 255.00):
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('YOUR_EMAIL', 'APP_PASSWORD')

	subject = f'Haven {product} Price Decreased from {converted_original_price} to {converted_sale_price}!'
	body = 'Check Haven link at PRODUCT_URL'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'FROM_EMAIL',
		'TO_EMAIL',
		msg
	)
	print('email has been sent!')

	server.quit()

while(True):
	check_price()
	time.sleep(14400)