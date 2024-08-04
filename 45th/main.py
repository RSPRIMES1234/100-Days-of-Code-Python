from bs4 import BeautifulSoup
import requests

response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")
web_page=response.text
bs=BeautifulSoup(web_page,"html.parser")
anchors=bs.find_all(name="a",class_="storylink")
text_list=[]
link_list=[]
for anchor in anchors:
    text=anchor.getText()
    article_link=anchor.get("href")
    text_list.append(text)
    link_list.append(article_link)

scores=[int(score.getText().split()[0]) for score in  bs.find_all(name="span",class_="score")]
max=scores.index(max(scores))
print(text_list[max])
print(link_list[max])
print(scores[max])
    # print(text)
    # print(article_link)
    #
    # print(article_upvote)

# print(anchors)







































































































# contents=""
# with open("website.html",encoding="utf-8") as f:
#     red=f.read()
#
#
# bs=BeautifulSoup(red,"html.parser")
# # print(bs.prettify())
# print(bs.findAll(name="p"))