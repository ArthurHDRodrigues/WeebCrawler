from bs4 import BeautifulSoup
import sys
import requests

page = requests.get(sys.argv[1], timeout=50)

page_content = BeautifulSoup(page.content, "html.parser")

print(page_content)
#print(page_content.find_all('a href'))


aa
