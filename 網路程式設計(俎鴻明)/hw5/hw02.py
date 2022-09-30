import requests
import bs4
url = 'https://www.chinatimes.com/?chdtv'
htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text, 'html.parser')
NewsTitles = objSoup.find_all('h3', class_='title')

for newsTitle in NewsTitles:
    inf=newsTitle.select('a')[0]
    print('-'*50)
    # print("焦點新聞標題:\n", newsTitle.get('img'))
    # print("職務名稱 : ", job.get('data-job-name'))
    print("焦點新聞標題:\n", inf.text,sep='')
print(len(NewsTitles))













