# -*- coding: utf-8 -*-
import random

import requests
from bs4 import BeautifulSoup
from random import choice

random_number = random.randint(0,100)
list_name=[]
list_tarih=[]
list_imdb=[]
filmbilgileri={}
url ="https://www.imdb.com/chart/moviemeter/"
R = requests.get(url)
Soup = BeautifulSoup(R.text,"html5lib")
List = Soup.find("tbody",{"class":"lister-list"}).find_all("tr")

for Film in List:
    Name = Film.find("td",{"class": "titleColumn"}).a.text
    Tarih = Film.find("td",{"class":"titleColumn"}).span.text
    imdb = Film.find("td",{"class":"ratingColumn imdbRating"}).text.strip()
   # filmbilgileri[Name] = (Tarih, imdb)
    list_name.append(Name)
    list_tarih.append(Tarih)
    list_imdb.append(imdb)

print(list_name[random_number] +"“\n”"+ list_tarih[random_number] +"“\n”"+ list_imdb[random_number])




