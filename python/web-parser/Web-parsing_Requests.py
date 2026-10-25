import requests
from bs4 import BeautifulSoup

url ="https://edition.cnn.com/"
response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

news_title = soup.find_all(name='h2')
for i in news_title:
    print(i.getText())





'''films_title = soup.find_all(name='a', class_='movieItem_title')
#print(films_title)

with open('films_titles.txt', 'w', encoding='UTF-8') as file:
    for i in films_title:
        print(i.getText(), file=file)'''



'''x = soup.find(name='h1').get_text()
#print(x)

y = soup.find_all(name='p')
#print(y[0].text)

z = soup.find(name='nav', class_='newFilmInfo_genreMenu swipe outer-mobile inner-mobile')
a = soup.find_all(name='span', class_='newFilmInfo_genreItem button-default')

#for i in a:
    #print(i.getText())'''