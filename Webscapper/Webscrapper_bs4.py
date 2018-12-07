# https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
# webbrowser. Comes with Python and opens a browser to a specific page.
# Requests. Downloads files and web pages from the Internet.
# Beautiful Soup. Parses HTML, the format that web pages are written in.
# Selenium. Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser.

import requests
import csv
from bs4 import BeautifulSoup


# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
# soup = BeautifulSoup(page.text, 'html.parser')

# # Finds AlphaNav and Remove bottom links
# last_links = soup.find(class_='AlphaNav')
# last_links.decompose()

# # Create a file to write to, add headers row
# f = csv.writer(open('z-artist-names.csv', 'w'))
# f.writerow(['Name', 'Link'])

# # Pull all text from the BodyText div
# artist_name_list = soup.find(class_='BodyText')
# # Pull text from all instances of <a> tag within BodyText div
# artist_name_list_items = artist_name_list.find_all('a')

# # Create for loop to print out all artists' names
# # prettify - nicely formatted Unicode string
# # for artist_name in artist_name_list_items:
# #     print(artist_name.prettify())

# # Pulling the Contents from a Tag
# # target contents of <a> tags rather than print entire link tag.
# # .contents - return the tag’s children as a Python list data type.
# for artist_name in artist_name_list_items:
#     names = artist_name.contents[0]
#     # Extract URL associated
#     links = 'https://web..org' + artist_name.get('href')
#     print(names)
#     print(links)

# # Writing the Data to a CSV File
#     # Add each artist’s name and associated link to a row
#     f.writerow([names, links])
    
# # Retrieving Related Pages

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)


for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        f.writerow([names, links])