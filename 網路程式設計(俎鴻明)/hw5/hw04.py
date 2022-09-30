import time

from bs4 import BeautifulSoup
from selenium import webdriver
'''
進入https://rent.housefun.com.tw網頁後，區域找 選台北市 全區，按找租屋 按鈕
得到下面url網址，此網頁內容是由javascript產生
'''
url = "https://rent.housefun.com.tw/region/%C2%A5x%C2%A5_%C2%A5%C2%AB/?cid=0000"
npage=eval(input("要爬取多少頁? 請輸入: "))
driver = webdriver.Chrome()
driver.get(url)
page=1
while page<=npage:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    div = soup.find("div", id="SearchContent")
    items = div.find_all("article")
    print("爬取第{}頁，共有{}筆資料".format(page,len(items)))


    page+=1
    scpt=f"PM({page})"
    driver.execute_script(scpt)
    driver.implicitly_wait(50)
    time.sleep(1)


    for item in items:
        title = item.find("h3", class_="title").find("a")
        #title = item.select("h3[class=title]")[0].select("a")[0]
        if title: print(title.text)
        address = item.find("address", class_="addr")
        #address = item.select("address[class=addr]")[0]
        if address: print(address.text.strip())
        price = item.find("span",class_='infos num')
        #price = item.select("span[class='infos num']")[0]
        if price: print(price.text)
        print("-------------------")
#driver.quit()
