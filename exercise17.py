import requests
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
features="lxml"

import string
from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html, "html.parser")

for h2 in soup.find_all("h2", class_="esl82me2"):
    print(h2.text)

#for h2 in soup.select("9ywo2s esl82me2"):


# class="css-6h3ud0 esl82me2"
