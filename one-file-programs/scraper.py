import requests as r
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

result = r.get(url).content
soup = BeautifulSoup(result, 'html.parser')
story = soup.findAll("p", text=True)
# story = soup.findAll("p").get_text()

for i in range(len(story)):
    print(story[i].text)