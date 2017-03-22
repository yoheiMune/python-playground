"""
    Selenium x Phantomjs を用いたWebスクレイピング.

    Reference：
        http://zipsan.hatenablog.jp/entry/20150413/1428861548

    Dependencies：
        pip3 install --upgrade beautifulsoup4
        pip3 install --upgrade selenium

    Dependencies:
        PhantomJSをインストールして、$PATH に通った状態にする.
        http://phantomjs.org/
"""
from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 普通に取ると、取得できない...
from urllib.request import urlopen
with urlopen("http://yoheim.net/work/async_page.html") as res:
    html = res.read().decode("utf-8")
    bs = BeautifulSoup(html, "html.parser")
    img_urls = [img.get("src") for img in bs.select("#imageRoot img")]
    pprint(img_urls)  # 空っぽ    


driver = webdriver.PhantomJS()
driver.get("http://yoheim.net/work/async_page.html")

# ちょっと待つ（必要あれば）
# time.sleep(5) # 5s

html = driver.page_source

# 画像のURLを取得する.
bs = BeautifulSoup(html, "html.parser")
img_urls = [img.get("src") for img in bs.select("#imageRoot img")]
pprint(img_urls)

# ついでにスクリーンショット.
driver.save_screenshot("ss.png")

driver.quit()


















