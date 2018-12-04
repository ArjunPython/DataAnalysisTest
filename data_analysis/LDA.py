# -*- coding: utf-8 -*-
# @Time    : 2018/11/4 17:48
# @Author  : Arjun

import pandas as pd
from gensim import corpora, models


negfile = './data/meidi_jd_neg_cut.txt'
posfile = './data/meidi_jd_pos_cut.txt'
stoplist = './data/stoplist.txt'

neg = pd.read_csv(negfile, encoding='utf-8', header=None,engine="python")
pos = pd.read_csv(posfile, encoding='utf-8', header=None,engine="python")
stop = pd.read_csv(stoplist, encoding='utf-8', header=None, sep='tipdm',engine="python")

"""sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错"""
"""所以解决办法是手动设置一个不存在的分割词，如tipdm。"""
"""Pandas自动过滤了空格符，这里手动添加"""
stop = [' ', ''] + list(stop[0])

"""定义一个分割函数，然后用apply广播"""
neg[1] = neg[0].apply(lambda s: s.split(' '))

"""逐词判断是否停用词，思路同上"""
neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop])
pos[1] = pos[0].apply(lambda s: s.split(' '))
pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stop])



"""负面主题分析"""
"""建立词典"""
neg_dict = corpora.Dictionary(neg[2])
"""建立语料库"""
neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]]
"""LDA模型训练"""
neg_lda = models.LdaModel(neg_corpus, num_topics=3, id2word=neg_dict)
for i in range(3):
    """输出每个主题"""
    print(neg_lda.print_topic(i))

"""正面主题分析"""
pos_dict = corpora.Dictionary(pos[2])
pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
pos_lda = models.LdaModel(pos_corpus, num_topics=3, id2word=pos_dict)
for i in range(3):
  print(neg_lda.print_topic(i))

