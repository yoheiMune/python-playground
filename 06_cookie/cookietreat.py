# -*- coding: utf-8 -*-
# Cookieの扱い
# はてなブックマークにログインする
import urllib.request
import http.cookiejar
import gzip
import sys, os, os.path

class Main():
    def __init__(self):
        self.cookiefile = "cookies.txt"
        self.cj = http.cookiejar.LWPCookieJar()
        if os.path.exists(self.cookiefile):
            self.cj.load(self.cookiefile)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        urllib.request.install_opener(opener)

    def __del__(self):
        self.cj.save(self.cookiefile)
        print("Cookie save to " + self.cookiefile)

    def getURL(self, url):
        headers = { 'User-Agent' :  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
        req = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(req)
        charset = response.headers.get_content_charset()
        if charset == None:
            charset = "utf-8"
        dechtml = ""
        if response.info().get("Content-Encoding" ) == "gzip":
            dechtml = gzip.decompress(response.read())
        else:
            dechtml = response.read()
        html = dechtml.decode(charset, "ignore")
        open("response.html", "w", encoding=charset, errors="ignore").write(html)

Main().getURL("http://www.google.com")
