# -*- coding: utf-8 -*-
"""
@author: zhang
"""

import os
import sys
def insert_somthing_between(path):
    file_list = os.listdir(path)
    file_list.sort()

    for file_name in file_list:
        if file_name=='.DS_Store':
            continue
        fisrt_name,last_name = os.path.splitext(file_name)
        list_fisrt_name = list(fisrt_name)
        while ' ' in list_fisrt_name:
            list_fisrt_name.remove(' ')
        #在每个字符间插入-, abc --> a-b-c
        #可以选择插入符号，只要修改 '插入内容'.join()，插入内容可以随意修改
        new_first_name = '_'.join(list_fisrt_name)
        new_name = new_first_name + last_name
        os.chdir(path)
        os.rename(file_name,new_name)

if __name__ == '__main__':
    target_dir = sys.argv[1]
    insert_somthing_between(target_dir)
