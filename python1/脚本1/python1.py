#!/usr/bin/python3
# _*_ coding=utf-8 _*_

#File name  : python1.py
#Author     : liyg
#Description: 将文件内容进行批量处理，比如每行都增加某个内容
#Modified on: 2023-01-16
#Revised content: 1.0

import os

file_log    =open("test_reg_case.cfg","r")      #读取载入的文件
f_liyg      =open("run_test","a")               #打开文件以便写入

# line 是文件中每行的内容
for line in file_log.readlines():
    if("#" in line or "//" in line):            #如果出现‘#’或“//”，不做任何操作继续循环
        continue
    elif (line == "\n"):                        #如果i接收到的内容为空，不做任何操作继续循环
        continue
    else:
        line = line.strip('\n')                 #删除每行内容的换行符
        #line = line.replace("\n"," ")          #将每行的换行符替换为空格
        f_liyg.write("run tst -case " + line + "  -wav -psl all\n")#将添加的内容表示出来
            
f_liyg.close()                                  #关闭文件，避免浪费系统资源
