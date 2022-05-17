import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint
file = open('ComedyMovies.csv','w', newline = '\n')
file_obj = csv.writer(file)
file_obj.writerow(['Number', 'Title', 'Year','Genre', 'Rating'])
index = 1
while index < 250:
    url = 'https://www.imdb.com/search/title/?genres=comedy&groups=oscar_nominee&start=1' + str(index)
    headers = {'Accept-Language': 'en-US'}
    res = requests.get(url, headers = headers)
    soupall = BeautifulSoup(res.text,'html.parser')
    soup = soupall.find('div', class_ = 'lister-list')
    all_movie = soup.find_all('div', class_ = 'lister-item')
    for each in all_movie:
        number = each.h3.span.text
        title = each.h3.a.text
        year = each.find('span', class_ = 'lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        rating = each.strong.text
        genre = each.find('span', class_ = 'genre').text
        genre = genre.replace(',', '')
        file.write(number + ',' + title + ',' + year + ',' + genre + ',' + rating + '\n')
        file_obj.writerow = ([number, title, year, genre, rating])
        print(number)
    index+=50
    sleep(randint(15,20))
