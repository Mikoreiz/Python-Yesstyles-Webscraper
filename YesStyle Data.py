from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

##THIS PROGRAM WILL COLLECT DATA FROM THE WEBSITE YESSTYLE. IT WILL COLLECT THE NAME, 
##PRICE AND DISCOUNT OF THE FIRST 35 MEN'S TOPS ON SALE.

	

##SCRAPES THE URL FOR THE PRODUCTION INFORMATION	
mentop_url = 'http://www.yesstyle.com/en/men-tops/list.html/bcc.14160_bpt.46'
uClient = uReq(mentop_url)
page_html = uClient.read()
uClient.close()
mentopsoup_page = soup(page_html, 'html.parser')
mens_tops = mentopsoup_page.find_all('div', {'class':'itemContainer'})
	
##THIS IS WHERE THE PRODUCT INFORMATION WILL GO IN TO
name = []
price = []
discount = []
merch = {}


##COLLECTS THE NAME, PRICE AND DISCOUNT OF ALL THE PRODUCTS AND ADDS THEM INTO THE LISTS
for tops in mens_tops:
	top_title = tops.find_all('div', {'class':'itemTitle'})
	product_name = top_title[0].text
	top_price = tops.find_all('div', {'class':'itemPrice'})
	product_price = top_price[0].text
	#top_discount = tops.find_all('div', {'class':'itemStatus'})
	#product_discount = top_discount[0].text
	
	name.append(product_name)
	price.append(product_price)
	#discount.append(product_discount)

##ADDS THE LISTS INTO THE 'MERCH' DICTIONARY	
merch['Name'] = name
merch['Price'] = price
#merch['Discount'] = discount


##PUTS THE DATE INTO A DATAFRAME AND PRINTS IT OUT FOR US TO SEE
df = pd.DataFrame(merch)


#df.to_csv("New.csv")

g = df.groupby('Name')
		


	
	