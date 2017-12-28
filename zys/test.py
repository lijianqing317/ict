# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#定义常量
rnn_unit=10       #hidden layer units
input_size=613
output_size=1
lr=0.0006         #学习率
#——————————————————导入数据——————————————————————Ll
f=open('ljqdpc.csv')
df=pd.read_csv(f)     #读入数据
data=df.iloc[:,0:614].values  #取列
#获取训练集
def get_train_data(time_step=1,train_begin=0,train_end=100):
    data_train=data[train_begin:train_end]
    normalized_train_data=data_train #标准化
    print normalized_train_data
    train_x,train_y=[],[]   #训练集
    for i in range(len(normalized_train_data)-time_step):
        x=normalized_train_data[i:i+time_step,:613]
        y=normalized_train_data[i:i+time_step,613,np.newaxis]
        train_x.append(x.tolist())
        train_y.append(y.tolist())
    return train_x,train_y




#获取测试集
def get_test_data(time_step=1,test_begin=100):
    data_test=data[test_begin:]
    normalized_test_data=data_test  #标准化
    size=(len(normalized_test_data)+time_step-1)//time_step  #有size个sample
    test_x,test_y=[],[]
    for i in range(size-1):
        x=normalized_test_data[i*time_step:(i+1)*time_step,:613]
        y=normalized_test_data[i*time_step:(i+1)*time_step,613]
        test_x.append(x.tolist())
        test_y.extend(y)
    test_x.append((normalized_test_data[(i+1)*time_step:,:613]).tolist())
    test_y.extend((normalized_test_data[(i+1)*time_step:,613]).tolist())
    print len(test_x),len(test_y)
    return test_x,test_y
print get_train_data(),'==='
print get_test_data(),'------'


print df.shape
print data
train_begin = 0
train_end = 100
data_train=data[train_begin:train_end]
data_test =data[train_end:]
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=5)]
estimator = tf.contrib.learn.LinearRegressor(feature_columns=feature_columns)
estimator.fit(x= data_train[:100],y=data_train[0:100], batch_size=4,steps=300)
print(estimator.evaluate(data_train[:613],y=data_train[613]))
print(estimator.evaluate(input_fn=data_train[:613]))