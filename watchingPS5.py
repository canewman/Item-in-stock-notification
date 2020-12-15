import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New"
#url = "https://www.bestbuy.com/site/playstation-5/playstation-5-packages/pcmcat1588107358954.c?id=pcmcat1588107358954"
ua = UserAgent()
ua = ua.random
headers = {'User-Agent': ua}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

addToCartButton = soup.find('button', class_='add-to-cart btn btn-primary')
availability = str(addToCartButton)
button = str(addToCartButton).split(',')#a list of the buttons components
print(button[10][16:-1])#prints the result of availability

'''
psDiscButton = soup.find(id="fulfillment-add-to-cart-button-09bde328-a15c-424d-83a5-bc874c981666")
#psDigitalButton = soup.find(id="fulfillment-add-to-cart-button-1be10061-d746-44dc-ac87-133ec505a7f5")
psDigitalButton = soup.find('button', class_='btn btn-disabled v-medium btn-block add-to-cart-button')
print(psDigitalButton)
'''
