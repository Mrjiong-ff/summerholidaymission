import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.roboxx.ltd/'
targethtml = requests.get(url)
soupdata = BeautifulSoup(targethtml.text,'html.parser')
data=soupdata.select('#post-1727 > div > div.entry-after-image > header > h2 > a')
for target in data:
    result={
        'title':target.get_text('href'),
        'link':target.get('href'),
        'ID':re.findall('\d+',target.get('href'))
    }
# print(data)
# print(result)