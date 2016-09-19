import urllib.request
from bs4 import BeautifulSoup


# 試し
html = urllib.request.urlopen("http://www.yoheim.net").read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

h2 = soup.find("h2")
print(h2)
if "content" in h2:
    print("aaa")
else:
    print("bbb")