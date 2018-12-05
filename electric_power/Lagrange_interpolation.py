# -*- coding: utf-8 -*-
# @Time    : 18-12-5 下午5:21
# @Author  : Arjun

"""拉格朗日插值法"""

import pandas as pd
from scipy.interpolate import lagrange

inputfile = "./data/missing_data.xls"
outputfile = "./data/missing_data_processed.xls"

data = pd.read_excel(inputfile,header=None)

print(data.columns)

"""s 为列向量，n为被插值的位置，k为取前后的数据个数，默认为5"""
def ployinterp_column(s,n,k=5):
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]
    """删除空置"""
    y = y[y.notnull()]
    """进行插值，并返回插值结果"""
    return lagrange(y.index,list(y))(n)

for i in data.columns:
    print(i)
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)


data.to_excel(outputfile,header=None,index=False)