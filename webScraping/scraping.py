import requests #used for gathering HTML data from a page
from bs4 import BeautifulSoup   #for manipulating HTML data easily
import pandas as pd


url = 'https://books.toscrape.com/' #URL of site to start scraping
response = requests.get(url)    #get HTML data
soup = BeautifulSoup(response.content, 'html.parser') #parse with BeautifulSoup

books = soup.find_all('article', class_='product_pod')  #gather all books information


data = []
for book in books:
    title = book.h3.a['title']  #grab title
    price = book.find('p', class_='price_color').text #grab price
    price = float(price[1:len(price)])  #eliminate the price symbol and just keep the price
    rating = book.p['class'][1] #grab the rating
    temp = {    #create a dict with all info
        "title":title,
        "price":price,
        "rating": rating
    }
    data.append(temp)  

df = pd.DataFrame(data) #Convert to pandas DF
print(df.head())