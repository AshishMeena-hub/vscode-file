import requests
import pandas as pd
import html5lib
from bs4 import BeautifulSoup
url =  "https://www.dunzo.com/chennai"
r = requests.get(url)
htmlcontent = r.content
#print(htmlcontent)
soup = BeautifulSoup(htmlcontent,'html.parser')
title = soup.title
#print(title)
paras = soup.find_all('p')
#print(paras)
anchors = soup.find_all('a')
#print(anchors)
#print(soup.find('p')['class'])
#needs = (soup.find_all("p",class_="sc-1gu8y64-0 hlIaQc sc-9dk4hu-1 SxUhl"))
#for need in needs:
#    print(need.get_text())
needs = soup.find_all(class_='sc-bdVaJa bn5c3a-2 jlCyXG')
#print(needs[0])
#print(needs[0].find(class_='sc-1gu8y64-0 hlIaQc sc-9dk4hu-1 SxUhl').get_text())
daily_needs = [need.find(class_='sc-1gu8y64-0 hlIaQc sc-9dk4hu-1 SxUhl').get_text() for need in needs]
#print(daily_needs)
#stores = soup.find_all(class_='sc-bdVaJa ia5a90-1 blNhbU')
#store_name = [store.find(class_='sc-1gu8y64-0 hlIaQc sc-1vmrdfr-0 jdbBdT store-name').string for store in stores]
#print(store_name)
#store_address = [store.find(class_='sc-bdVaJa iHZvIS store-area').get_text() for store in stores]

#all_links = set()
#for link in anchors:
    #if(link.get('href')!='#'):
        #linktext = "https://www.dunzo.com/chennai" +link.get('href')
        #all_links.add(link)
        #print(linktext)
        #print(all_links)
#needables = soup.find_all('p', class_='sc-bdVaJa sc-bwzfXH bn5c3a-1 bENzZA')
#print(needables)
#container = soup.find_all("div",class_="sc-bdVaJa sc-bwzfXH pjOvZ")

        #data1 = set()
       # data2 = set()
        
#stores = [container.find(class_='sc-1gu8y64-0 hlIaQc sc-1vmrdfr-0 jdbBdT store-name').string for store in container]
#address = [container.find(class_='sc-1gu8y64-0 hlIaQc sc-1vmrdfr-1 mPTWh').string for address in container]
#print(address)
#print(soup.get_text())
#print(stores)
#    stores = soup.find("div", class_="sc-bdVaJa ia5a90-1 blNhbU")
#store_name = [store.find(class_='sc-1gu8y64-0 hlIaQc sc-1vmrdfr-0 jdbBdT store-name').get_text() for store in stores]
#store_address = [store.find(class_='sc-1gu8y64-0 hlIaQc sc-1vmrdfr-1 mPTWh').get_text() for store in stores]
#print(store_name)
all_stores_name = []
stores = (soup.find_all("p",class_="sc-1gu8y64-0 hlIaQc sc-1vmrdfr-0 jdbBdT store-name"))

    all_store_name.add(stores.string)

print(all_stores_name)    
