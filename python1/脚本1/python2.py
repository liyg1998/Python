#!/usr/bin/python3
#encoding:utf-8
# _*_ coding=utf-8 _*_

#File name  : python.py
#Author     : liyg
#Description: 对比两个文件内容，输出html格式
#Modified on: 2023-01-17
#Revised content: 1.0

import difflib
import sys

#读取配置文件函数
def read_file(file_name):
    try:
        file_handle=open(file_name,"r")         #打开文件
        text=file_handle.read().splitlines()    #按行进行分割读取
        file_handle.close()                     #关闭文件
        return text
    except IOError as error:
        print("Read file Error:{0}").format(error)
        sys.exit()

#比较两个文件并输出html格式的结果
def compare_file(file1_name,file2_name):
    if file1_name == " " or file2_name == " ":
        print("文件路径不能为空：file1_name的路径为:{0},file2_name的路径为：{1} .").format(file1_name,file2_name)
        sys.exit()
    text1_lines=read_file(file1_name)
    text2_lines=read_file(file2_name)
    diff=difflib.HtmlDiff()                         #创建htmldiff对象
    result=diff.make_file(text1_lines,text2_lines)  #通过make_file方法输出html格式的对比结果
    
    #将结果保存到result.html文件中并打开
    try:
        with open("result.html","w") as result_file:
            result_file.write(result)
    except IOError as error:
            print("写入html文件错误:{0}").format(error)

if __name__ == "__main__":
    compare_file("test_reg_case.cfg","test.log")  #传入两文件的路径
