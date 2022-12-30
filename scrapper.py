from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd
import requests

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser=webdriver.Chrome("chromedriver.exe")
browser.get(start_url)

Soup=BeautifulSoup(browser.page_source,"html.parser")
star_table=Soup.find("table")
templist=[]
rows=star_table.find_all("tr")
for tr in rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    templist.append(row)

name=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(templist)):
    name.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
df=pd.DataFrame(list(zip(name,distance,mass,radius)),columns=['Name','Distance','Mass','Radius'])
df.to_csv("scrapper.csv")
