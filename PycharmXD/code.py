import urllib.parse
import urllib.request

# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

from bs4 import BeautifulSoup

soup = BeautifulSoup(open(r'C:\Users\marcuscheng\Downloads\Trace Option.html',encoding='UTF-8'), 'html.parser')