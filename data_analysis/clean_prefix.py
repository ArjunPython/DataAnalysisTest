# -*- coding: utf-8 -*-
# @Time    : 2018/11/4 16:46
# @Author  : Arjun

import pandas as pd

inputfile1 = "./data/meidi_jd_process_1_负面情感结果.txt"
inputfile2 = './data/meidi_jd_process_1_正面情感结果.txt'
outputfile1 = './data/meidi_jd_neg.txt'
outputfile2 = './data/meidi_jd_pos.txt'

# f1 = open("./data/meidi_jd_process_1_负面情感结果.txt")
data1 = pd.read_csv(inputfile1, encoding='utf-8', header=None,engine="python")
data2 = pd.read_csv(inputfile2, encoding='utf-8', header=None,engine="python")
"""去除分数 空格"""
data1 = pd.DataFrame(data1[0].str.replace('.*?\d+?\\t ', ''))
data2 = pd.DataFrame(data2[0].str.replace('.*?\d+?\\t ', ''))

data1.to_csv(outputfile1, index=False, header=False, encoding='utf-8')
data2.to_csv(outputfile2, index=False, header=False, encoding='utf-8')
