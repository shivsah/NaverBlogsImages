import lxml
from bs4 import BeautifulSoup
from requests import get
from fetch import *

url = 'https://m.post.naver.com/viewer/postView.nhn?volumeNo=20163796&memberNo=29747755'
response = get(url)

#html_soup = BeautifulSoup(response.text, 'lxml')
#print(html_soup)
#type(html_soup)
#html_soup.prettify()

css_soup = BeautifulSoup(response.text,'lxml')
css_count = css_soup.find_all("div", class_="se_component se_image default")
print(len(css_count))
print(css_count)



#print(type(container))
