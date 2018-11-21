#encoding=utf8
# 获取豆瓣小说标签页面中的所有书籍名称
import urllib2
from bs4 import BeautifulSoup

url = "http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book"
req = urllib2.Request(url)
res = urllib2.urlopen(req).read()
#print res

soup = BeautifulSoup(res, "html.parser")
book_div = soup.find(attrs={"id":"book"})
#print book_div
book_a = book_div.find_all(attrs={"class":"title"})
#print book_a
for book_name in book_a:
    #print book_name.contents[0]
    print book_name.string
