# -*- coding: utf-8 -*-
# @Time    : 2018/11/4 17:16
# @Author  : Arjun

import pandas as pd
import jieba


inputfile1 = './data/meidi_jd_neg.txt'
inputfile2 = './data/meidi_jd_pos.txt'
outputfile1 = './data/meidi_jd_neg_cut.txt'
outputfile2 = './data/meidi_jd_pos_cut.txt'

data1 = pd.read_csv(inputfile1, encoding='utf-8', header=None)
data2 = pd.read_csv(inputfile2, encoding='utf-8', header=None)

"""自定义简单分词函数"""
mycut = lambda s: ' '.join(jieba.cut(s))
""" 通过“广播”形式分词，加快速度。"""
data1 = data1[0].apply(mycut)
data2 = data2[0].apply(mycut)

data1.to_csv(outputfile1, index=False, header=False, encoding='utf-8')
data2.to_csv(outputfile2, index=False, header=False, encoding='utf-8')