#coding:utf-8
#author:wangyijun
import xlrd
from collections import Counter
workbook = xlrd.open_workbook("贾樟柯_导演.xls")
sheet = workbook.sheet_by_index(0)
list=[]
for i in range(sheet.nrows):
    rows= sheet.row_values(i)
    list.append(rows[2][2:-2])
count_list = Counter(list)
x=[]
y=[]
list={}
for key,values in count_list.items():
    list[key]=values
x=sorted(list)
ll={}
for i in x:
    y.append(list[i])
#print(list_new)
import matplotlib.pyplot as plt
from   matplotlib import font_manager
zh_font = font_manager.FontProperties(fname="./simkai.ttf")
plt.figure()


plt.plot(x,y,marker='o',markerfacecolor='b',markersize=5)
plt.xlabel("year")
plt.ylabel("movie count")
plt.title("贾樟柯导演电影数目",fontproperties=zh_font)
plt.show()