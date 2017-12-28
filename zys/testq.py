# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#定义常量
rnn_unit=10       #hidden layer units
input_size=3
output_size=1
lr=0.0006         #学习率
#——————————————————导入数据——————————————————————Ll
f=open('ljqdpc.csv')
df=pd.read_csv(f)     #读入数据
data=df.iloc[:,0:614].values  #取列
#获取训练集
data_train=data[0:100]
#print data_train
data_train1=np.nan_to_num(data_train)
normalized_train_data= np.log10(data_train.max(axis=0))#标准化
print normalized_train_data


