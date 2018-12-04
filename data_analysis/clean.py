# -*- coding: utf-8 -*-
# @Time    : 2018/11/4 15:49
# @Author  : Arjun

import pandas as pd

inputfile = "./data/meidi_jd.txt"
outputfile = "./data/meidi_jd_process_1.txt"
data = pd.read_csv(inputfile, encoding='utf-8', header=None)
l1 = len(data)
"""原始数据去重"""
data = pd.DataFrame(data[0].unique())
"""原始数据去重"""
# data = data.drop_duplicates()
l2 = len(data)
data.to_csv(outputfile, index=False, header=False, encoding='utf-8')
print(u'删除了%s条评论' %(l1-l2))