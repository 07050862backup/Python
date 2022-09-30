import requests
import bs4
url = 'http://news.baidu.com/tech'
htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text, 'html.parser')
aa = objSoup.select('.middle-focus-news')

for i in range(len(aa)):
    bb = aa[i].select('.fb-list')
    for j in range(len(bb)):
        cc = bb[j].select('li')
        print('-' * 50)
        for k in range(len(cc)):
            print("* ", cc[k].text, sep='')














