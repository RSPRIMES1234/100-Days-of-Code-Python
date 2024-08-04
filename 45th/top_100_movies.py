import requests
from bs4 import BeautifulSoup

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

website=response.text
soup=BeautifulSoup(website,"html.parser")

titles=soup.find_all(name="h3",class_="title")
title_list=[title.getText()  for title in titles]
title_list=title_list[::-1]

with open("top100movies.txt",'w',encoding="utf-8") as f:
    for _ in title_list:
        f.writelines(f"{_}\n")
    print("done")