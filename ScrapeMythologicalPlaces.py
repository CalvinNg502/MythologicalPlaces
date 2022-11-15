from selenium import webdriver
from bs4 import BeautifulSoup
import re

# fetch webpage
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://en.wikipedia.org/wiki/List_of_mythological_places")



# parse webpage with soup
soup = BeautifulSoup(driver.page_source, "html.parser")

# grab places and descriptions and put them in lists
places = []
descriptions = []
i = 0
for table in soup.find_all('table', {'class':'wikitable'}):
    for text in table.find_all('td'):
        if i % 2 == 0:
            places.append(text.get_text())
        else:
            descriptions.append(text.get_text())
        i += 1

# write to file
file = open("places.txt", "w", encoding="utf-8")
for place in places:
    file.write(str(place) + '\n')
file.write("end_of_places\n")
for description in descriptions:
    file.write(re.sub("\[.*\]", "", str(description)))
file.write("end_of_file")