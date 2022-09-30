import requests
import bs4
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url1 = 'https://salary.tw/c/OTVU?currentPage='                   #改這裡就好
url2 = '&sort=null'
"""  前置步驟， 找總頁數"""
htmlFile = requests.get(url1+str(1)+url2, headers=headers) #先爬取第一頁，找到下方頁數
objSoup = bs4.BeautifulSoup(htmlFile.text, 'html.parser')
Findfinalpages = objSoup.find_all('a', class_='gl_page-link')#找到下面顯示頁數的地方
for Findfinalpage in Findfinalpages:
    inf = Findfinalpage.select('span')
    aa = Findfinalpage.text.replace("\n","").strip()
FinalPage = int(aa)
print("共有 :　%s 頁" %FinalPage)

"""  前置步驟結束"""
for i in range(FinalPage):
    htmlFile = requests.get(url1 + str(i + 1) + url2, headers=headers)
    objSoup = bs4.BeautifulSoup(htmlFile.text, 'html.parser')
    title = objSoup.select('.sa_title-wrap')
    for j in range(len(title)):
        print('*'*20)
        print('第{}頁 ， 第 {} 項'.format(i+1,j+1))
        print('*' * 20)
        # print(aa[j])
        inf = title[j].select('a')[0]
        print("職務名稱:", inf.text, sep='')
























