from bs4 import BeautifulSoup
import requests
import re

def main():
    # fetch webpage
    url = "https://en.wikipedia.org/wiki/List_of_mythological_places"
    page = requests.get(url)

    # parse webpage with soup
    soup = BeautifulSoup(page.text, "html.parser")

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

if __name__ = '__main__':
    main()