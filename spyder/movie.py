#coding:utf-8
#author:wangyijun
import re

import requests
import time

import xlwt
import pymongo
from bs4 import BeautifulSoup
# workbook=xlwt.Workbook(encoding="utf-8")
# worksheet=workbook.add_sheet("1")



connection = pymongo.MongoClient("127.0.0.1",27017)
collection=connection["jiazhengke"]["xiaowu"]
headers={
'Cookie':'bid=t29pYeCgr_0; gr_user_id=04a9dc29-b756-468c-b362-b52789595f6c; __yadk_uid=7OYuwaLPCSHZ3H0KkItXnYzQdK9xEGK0; ll="118172"; viewed="25775696_26801374_3112503_3348010_27074564_6809987"; _vwo_uuid_v2=E5BFF96096B2B3C1CCAC3ACD76A4E14B|c6f37a08ac5cd1afff1aec3af7e3af83; ap=1; __utmc=30149280; __utmz=30149280.1515418673.14.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1515418794.9.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1515426030%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DTcJJj_t7UyFRFG8W8_gK6xLdRYXEcRtLwG3zkLWNZDX51f-ZjqRIOOM_LCxJY-aL%26wd%3D%26eqid%3Dfc30e9780000a1bf000000065a5374a4%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.914550256.1504840431.1515418673.1515426030.15; __utmt_douban=1; __utma=223695111.2096366670.1504840431.1515418794.1515426031.10; __utmb=223695111.0.10.1515426031; __utmt=1; ps=y; dbcl2="172319033:GdhtblBh95E"; ck=eKcU; push_noty_num=0; push_doumail_num=0; __utmb=30149280.10.10.1515426030; _pk_id.100001.4cf6=ab4235686d9ae603.1504840431.10.1515426218.1515419867.',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Host':'movie.douban.com',

}
for i in range(0,500,20):
    url = "https://movie.douban.com/subject/1291851/comments?start=%d&limit=20&sort=new_score&status=P&percent_type="%(i)
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    if(html.status_code==200):
        comments_detail = soup.find_all("div",id="comments")

        for item in comments_detail[0].find_all("div",attrs={"data-cid":re.compile(".*")}):

            vote=item.find_all("span",attrs={"class":"votes"})[0].get_text()
            times=item.find_all("span",attrs={"class":"comment-time"})[0].get_text()
            comment=item.find_all("p")[0].get_text()
            comments={"time":times,"comment":comment,"vote":vote}
            collection.insert(comments)
            collection.save(comments)
        print("完成%d条"%(i))
        time.sleep(2)

    else:
        print(i)
        exit(0)
