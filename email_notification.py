import smtplib, ssl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import warnings
from email_list import EMAIL_LIST, FROM_MAIL
from selenium.webdriver.chrome.options import Options
warnings.filterwarnings("ignore", category=DeprecationWarning) 

PASSWORD = input("Input password: ")
TARGET_SALE_PRICE = "1500"


def get_price():
	fireFoxOptions = webdriver.FirefoxOptions()
	fireFoxOptions.set_headless()
	driver = webdriver.Firefox(firefox_options=fireFoxOptions)

	q = "gme+stock"
	driver.get("https://www.google.com/search?q=" + q)
	OutputElement = "/html/body/div[7]/div[2]/div[9]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/g-card-section/div/g-card-section/span[1]/span/span[1]"
	try:
		ResultElement = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(OutputElement))
		price = ResultElement.text
	except:
		price = 5
	price = float(price)
	driver.quit()
	print(time.strftime('%H:%M%p, %b %d, %Y'), "   - - -   GME - $ {}".format("N/A" if price==5 else price))
	return price

def send_email():
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	for to_mail in EMAIL_LIST:

		text = "FELLOW APE: BANANAS ARE NOW READY TO SELL AT {}".format(TARGET_SALE_PRICE)
		message = MIMEMultipart("alternative")
		message["Subject"] = "I LIKE THE STOCK"
		message["From"] = FROM_MAIL
		message["To"] = to_mail
		part1 = MIMEText(text, "plain")
		message.attach(part1)

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(FROM_MAIL, PASSWORD)
			server.sendmail(FROM_MAIL, to_mail, message.as_string())

def check_price_and_email():
	print("Starting email server...")
	while True:
		time.sleep(1)
		price = get_price()
		if price >= int(TARGET_SALE_PRICE):
			send_email()


check_price_and_email()