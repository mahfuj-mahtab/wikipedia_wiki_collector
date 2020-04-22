from bs4 import BeautifulSoup
import requests

text=input("Please Enter any word : ")
url="https://en.wikipedia.org/wiki/"

r=requests.get(url+text)
soup=BeautifulSoup(r.content, "html.parser")

div=soup.find("div",{"class", "mw-body"})
article=div.find_all("p")
for i in article:
    print(i.text)