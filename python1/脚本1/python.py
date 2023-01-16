#!/usr/bin/python3
# _*_ coding=utf-8 _*_

#File name  : python.py
#Author     : liyg
#Description: 将文件按按照内容根据指定的信息提取并分到不同的文件中，再将重复的内容去掉。
#Modified on: 2023-01-16
#Revised content: 1.0
#Shortcoming: 输入文件名称过于死板，文件路径过于绝对，不能在外部修改

import re
import shutil

#指定各个文件的路径
file_dir    ="/ldata/failed.log"
file_liyg   ="/ldata/sim/liyg1.log"
file_ouy    ="/ldata/sim/ouy1.log"
file_gub    ="/ldata/sim/gub1.log"
file_yinqh  ="/ldata/sim/yinqh1.log"
file_kuangzy="/ldata/sim/kuangzy1.log"

file_log    =open(file_dir,"r").read()            #读取载入的文件
f_liyg      =open(file_liyg,"a")                  #打开文件以便写入
f_ouy       =open(file_ouy,"a")                   #打开文件以便写入
f_gub       =open(file_gub,"a")                   #打开文件以便写入
f_yinqh     =open(file_yinqh,"a")                 #打开文件以便写入
f_kuangzy   =open(file_kuangzy,"a")               #打开文件以便写入

result=""

#指定某行的特定信息提取出来（正则表达式，可替换）
test_liyg   =re.compile('test_liyg.+time')        #生成一个正则表达式：从test_liyg开始到time 结束的内容
test_ouy    =re.compile('test_ouy.+time')         #生成一个正则表达式：从test_liyg开始到time 结束的内容
test_gub    =re.compile('test_gub.+time')         #生成一个正则表达式：从test_liyg开始到time 结束的内容
test_yinqh  =re.compile('test_yinqh.+time')       #生成一个正则表达式：从test_liyg开始到time 结束的内容
test_kuangzy=re.compile('test_kzy.+time')         #生成一个正则表达式：从test_liyg开始到time 结束的内容

test_liyg   =test_liyg.findall(file_log)          #用于指定的字符串中进行匹配
test_ouy    =test_ouy.findall(file_log)           #用于指定的字符串中进行匹配
test_gub    =test_gub.findall(file_log)           #用于指定的字符串中进行匹配
test_yinqh  =test_yinqh.findall(file_log)         #用于指定的字符串中进行匹配
test_kuangzy=test_kuangzy.findall(file_log)       #用于指定的字符串中进行匹配

result_liyg   =result + '\n'.join(test_liyg)      #换行输出
result_ouy    =result + '\n'.join(test_ouy)       #换行输出
result_gub    =result + '\n'.join(test_gub)       #换行输出
result_yinqh  =result + '\n'.join(test_yinqh)     #换行输出
result_kuangzy=result + '\n'.join(test_kuangzy)   #换行输出

#输出到文件中
print(result_liyg,file=f_liyg)
print(result_ouy,file=f_ouy)
print(result_gub,file=f_gub)
print(result_yinqh,file=f_yinqh)
print(result_kuangzy,file=f_kuangzy)

#文件关闭
f_liyg.close
f_gub.close
f_ouy.close
f_yinqh.close
f_kuangzy.close

liyg = 0
gub = 0
ouy = 0
yinqh = 0
kuangzy = 0

#不知道
lines_ouy = set()
lines_gub = set()
lines_yinqh = set()
lines_kuangzy = set()
lines_liyg = set()

#将重复内容去除，并记录有多少个不同   (每行比对)
dir_liyg=open(file_liyg,"r")
out_liyg=open("liyg.log","w")
for line in dir_liyg:
    if line not in lines_liyg:
        liyg+=1
        out_liyg.write(line)
        lines_liyg.add(line)
out_liyg.close
print("liyg:" + str(liyg)+ "!!!")

dir_gub=open(file_gub,"r")
out_gub=open("gub.log","w")
for line_gub in dir_gub:
    if line_gub not in lines_gub:
        gub+=1
        out_gub.write(line_gub)
        lines_gub.add(line_gub)
out_gub.close
print("gub:" + str(gub)+ "!!!")

dir_ouy=open(file_ouy,"r")
out_ouy=open("ouy.log","w")
for line_ouy in dir_ouy:
    if line_ouy not in lines_ouy:
        ouy+=1
        out_ouy.write(line_ouy)
        lines_ouy.add(line_ouy)
out_ouy.close
print("ouy:" + str(ouy)+ "!!!")

dir_kuangzy=open(file_kuangzy,"r")
out_kuangzy=open("kuangzy.log","w")
for line_kuangzy in dir_kuangzy:
    if line_kuangzy not in lines_kuangzy:
        kuangzy+=1
        out_kuangzy.write(line_kuangzy)
        lines_kuangzy.add(line_kuangzy)
out_kuangzy.close
print("kuangzy:" + str(kuangzy)+ "!!!")

dir_yinqh=open(file_yinqh,"r")
out_yinqh=open("yinqh.log","w")
for line_yinqh in dir_yinqh:
    if line_yinqh not in lines_yinqh:
        yinqh+=1
        out_yinqh.write(line_yinqh)
        lines_yinqh.add(line_yinqh)
out_yinqh.close
print("yinqh:" + str(yinqh)+ "!!!")
