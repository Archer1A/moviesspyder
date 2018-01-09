#coding:utf-8
#author:wangyijun
import requests
import time
from bs4 import BeautifulSoup
f = open("ip_pool.txt","w+")
headers = {
'Cookie':'ASPSESSIONIDASSCTBAA=AICDINOABHBCCCIBPEDDIOML; UM_distinctid=160b1e97b5b153-036f40195762bf-5a442916-100200-160b1e97b5d200; CNZZDATA1253438097=2012153161-1514811618-null%7C1514811618',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}

# for i in range(1):
#
#     req = requests.get("http://www.nianshao.me/?page=%s"%(str(i)),headers=headers)
#     soup = BeautifulSoup(req.content.decode("gbk"),"html.parser")
#
#     for i in soup.find_all("table")[0].find_all("tr")[1:]:
#         ip=i.find_all("td")[0].get_text()
#         port=i.find_all("td")[1].get_text()
#         proxies={
#             "http":"http://"+ip+":"+port
#         }
#         print("正在测试地址："+ip+":"+port)
#         try:
#             test=requests.get("http://tool.chinaz.com/",proxies=proxies,timeout=20)
#             if(test.status_code==200):
#               #  f = open("ip_pool.txt", "w")
#                 print("写入中....")
#                 f.write("http://"+ip+":"+port+"\n")
#                # f.close()
#         except:
#             print("无效")
#         time.sleep(1)



for i in range(0,13182,20):
    print(i)
