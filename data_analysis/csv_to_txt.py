# -*- coding: utf-8 -*-
# @Time    : 2018/11/4 14:59
# @Author  : Arjun

import pandas as pd

inputfile = "./data/huizong.csv"
outputfile = "./data/meidi_jd.txt"

"""读取csv文件"""
data = pd.read_csv(inputfile,encoding="utf-8")
"""读取美的的所有评论"""
data = data[["评论"]][data["品牌"]=="美的"]
data.to_csv(outputfile,index=False,header=False)