import requests
import bs4
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
#class="pure-u items_container"
url = 'https://feebee.com.tw/s/?q=raspberry+pi+4'
htmlFile = requests.get(url, headers=headers)
objSoup = bs4.BeautifulSoup(htmlFile.text, 'html.parser')
NewsTitles = objSoup.find_all('span', class_='pure-u items_container')
for newsTitle in NewsTitles:
    inf=newsTitle.select('a')[0]
    print('-'*50)
    print("Title :   ", inf.text)
    print("Link  :   ", inf.get('href'))
    print("Price :   ", inf.get('data-price'))
print(len(NewsTitles))