# Note: The practicepythonorg_probles.py file became too large, causing the code to execute slowly. 
# Therefore, I created a second part of it. 😇

# URL OF THE WEBSITE https://www.practicepython.org/

# ALL IMPORTS
import requests
from bs4 import BeautifulSoup

# 18. Decode A Web Page Two

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
responce = requests.get(url)

soup = BeautifulSoup(responce.text, "html.parser")
title = soup.title.string

article = soup.find_all("p")
x: int = 0
for i in article:
  x += 1
  print(f"{x}:\n {i.get_text()}\n")