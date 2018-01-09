#coding:utf-8
#author:wangyijun
import json

import requests
import time
from bs4 import BeautifulSoup

headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
   'cookie':'bid=t29pYeCgr_0; gr_user_id=04a9dc29-b756-468c-b362-b52789595f6c; ll="118172"; viewed="25775696_26801374_3112503_3348010_27074564_6809987"; _vwo_uuid_v2=E5BFF96096B2B3C1CCAC3ACD76A4E14B|c6f37a08ac5cd1afff1aec3af7e3af83; __utmz=30149280.1511666291.10.10.utmcsr=link.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.914550256.1504840431.1511666291.1514727218.11; __utmc=30149280; __utmt=1; __utmb=30149280.4.10.1514727218'
   # 'host':'erebor.douban.com',
   ,'Referer':'https://movie.douban.com/subject_search?search_text=%E8%B4%BE%E6%A8%9F%E6%9F%AF&cat=1002&start=0'

}
import xlwt
workbook = xlwt.Workbook(encoding="utf-8")
worksheet=workbook.add_sheet("贾樟柯")

fff = open("贾樟柯.txt","w+",encoding="utf-8")

def get_detail(i,id):
    print(i)
    proxie = {
        'http': 'http://122.72.18.35:80'
    }
    message = requests.get("https://api.douban.com/v2/movie/%s"%(str(id)),proxies = proxie,timeout = 20)
    #print(message.text)
    js=json.loads(message.content.decode('raw_unicode_escape'))
    movie_name =str(js["attrs"]["title"])
    print(movie_name)
    if("director" in js["attrs"].keys()):
        director = str(js["attrs"]["director"])
        worksheet.write(i, 1, director)


    year = str(js["attrs"]["year"])
    summary = str(js["summary"])
    tag=str(js["tags"])
    average_rate=str(js["rating"]["average"])
    alt = str(js["alt"])
    #fff.write(movie_name+"\t"+director+"\t"+year+"\t"+summary+"\t"+tag+"\t"+average_rate++"\t"+alt+"\n")
    worksheet.write(i,0,movie_name)

    worksheet.write(i,2,year)
    worksheet.write(i,3,summary)
    worksheet.write(i,4,tag)
    worksheet.write(i,5,average_rate)
    worksheet.write(i,6,alt)





def get_all_movie_messages():
    fo = open("zhangkejia.txt","w+",encoding="utf-8")
    for d in range(8):
        usl = "https://movie.douban.com/celebrity/1274261/movies?start=%d&format=pic&sortby=vote&"%(d*10)
        proxie={
            'http':'http://114.235.254.166:80'
        }
        req =requests.get(url=usl)

        #print(req.content.decode("utf-8"))
        soup = BeautifulSoup(req.text,"html.parser")
        ul=soup.find_all("ul",_class="")

        for li in ul[3].find_all("li"):
            print("*"*20)
            url=li.find("h6").a.get("href")
            list=li.find("h6").get_text().split("\n")
            movie_name = list[1].strip()
            print(movie_name)
            year = list[2].strip()
            print(year)
            role = list[3].strip()
            print(role)
            fo.write(movie_name+"\t"+url+"\t"+year+"\t"+role+"\t"+"\n")
        time.sleep(3)

file = open("zhangkejia.txt","rb")
# for line in file.readlines():
#     ll = line.decode("utf-8").split("\t")[1].split("/")[4]
#     get_detail(ll)
if __name__ == '__main__':
    i=0
    file = open("zhangkejia.txt", "rb")

    for line in file.readlines():
        if "导演" in line.decode("utf-8"):
            print(line.decode("utf-8"))
            ll = line.decode("utf-8").split("\t")[1].split("/")[4]
            get_detail(i,ll)
            i+=1
            time.sleep(3)
    workbook.save("贾樟柯_导演.xls")




# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
# browser.get("https://movie.douban.com/subject_search?search_text=%E8%B4%BE%E6%A8%9F%E6%9F%AF&cat=1002&start=0")
# element = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.ID,"wrapper")))
# for i in range(15):
# print(element[0].find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]'))