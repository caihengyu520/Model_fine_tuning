import pandas as pd
import numpy as np
import gc
import matplotlib.pyplot as plt
# pd.set_option('display.max_columns', None)
# #显示所有行
# pd.set_option('display.max_rows', None)
inputfile='zhuanhuan1.csv'
# data=pd.read_csv(inputfile,encoding='GB18030')
# data.to_csv('zhuanhuan1.csv',index=None,encoding='utf-8')
# print(data)
data=pd.read_csv(inputfile)
print(data.columns)
data['年'],data['月'],data['时间']=data['支付时间'].str.split('/').str
data.drop('支付时间',axis=1,inplace=True)
data['日'],data['具体时间']=data['时间'].str.split(' ',1).str
data.drop('时间',axis=1,inplace=True)
data=data[~data['具体时间'].str.contains('M')]
data['月'].astype(int)
print(data['月'].values.astype(int))
# print(data)
print(data)
###############完成任务1
# profix=64
# def get_index(group):
#     data_4month = group['月']
#     index = []
#     for i in data_4month.index:
#         if (data_4month[i] == '4'):
#             index.append(i)
#     return index
# def list_add(data):
#     sums=0
#     for i in range(len(data)):
#         data[i]=round(data[i])
#         sums+=data[i]
#     return sums
#
# jiaoyie=[]
# xiaoshouliang=[]
# indexs=[]
# # for name,group in data.groupby('设备ID'):
# #     index=get_index(group)
# #     jiaoyie.append(group['实际金额'][index].sum())
# #     xiaoshouliang.append(len(index))
# # jiaoyie.append(sum(jiaoyie))
# # xiaoshouliang.append(sum(xiaoshouliang))
# # b=map(lambda x:round(x,2),jiaoyie)
# # jiaoyie=list(b)
# # data_xiaoshou=list(zip(jiaoyie,xiaoshouliang))
# # # data_xiaoshou=np.array(data_xiaoshou)
# # data_xiaoshou=pd.DataFrame(data_xiaoshou,index=['1','2','3','4','5','总的'],columns=['销售额','销量'])
# # data_xiaoshou=data_xiaoshou.T
# # print(data_xiaoshou)
# import gc
# dict_={}
# for (k1,k2),group in data.groupby(['地点','月']):
#     # print((k1,k2))
#     # print(group)
#     k2=int(k2)
#     if(k2==4):
#         indexs.append(k1)
#         jiaoyie.append(round(group['实际金额'].sum(),2))
#         xiaoshouliang.append(len(group))
#     dingdanliang=round(len(group)/len(group['日'].value_counts()),2)
#     pingjun=round(sum(group['实际金额'])/len(group),2)
#     dict_[(k1,k2)]=(pingjun,dingdanliang)
# indexs.append('总的')
# jiaoyie.append(sum(jiaoyie))
# xiaoshouliang.append(sum(xiaoshouliang))
# dict_ = sorted(dict_.items(),key=lambda item:(item[0][0],item[0][1]))
# data_xiaoshou=pd.DataFrame(list(zip(jiaoyie,xiaoshouliang)),index=indexs,columns=['销售额','订单量']).T
# dict_=dict(dict_)
# print(dict_)
#
# # print(data['支付时间'])
# # data_4month=data['支付时间'].values
# # print(type(data_4month))
# # index=[]
# # for i in range(len(data_4month)):
# #     if(data_4month[i][5]=='4'):
# #         index.append(i)
# # print(len(index))
# # print(len(data_4month))
# # print(data_4month[index])


#################任务二
data_6month=data[data['月']=='6']
data_tongji=data_6month['商品'].value_counts()
data_tongji_top5=data_tongji[:5]
pd.DataFrame(data_tongji_top5).plot.bar()
plt.show()

jiaoyie=[]
xiaoshouliang=[]
indexs=[]
dict_={}
for (k1,k2),group in data.groupby(['地点','月']):
    k2=int(k2)
    if(k2==4):
        indexs.append(k1)
        jiaoyie.append(round(group['实际金额'].sum(),2))
        xiaoshouliang.append(len(group))
    dingdanliang=round(len(group)/len(group['日'].value_counts()),2)
    zongjiaoyi=round(sum(group['实际金额']))
    pingjun=round(sum(group['实际金额'])/len(group),2)
    dict_[(k1,k2)]=(pingjun,dingdanliang,zongjiaoyi)
indexs.append('总的')
jiaoyie.append(sum(jiaoyie))
xiaoshouliang.append(sum(xiaoshouliang))
dict_ = sorted(dict_.items(),key=lambda item:(item[0][0],item[0][1]))
data_xiaoshou=pd.DataFrame(list(zip(jiaoyie,xiaoshouliang)),index=indexs,columns=['销售额','订单量']).T
dict_=dict(dict_)
data_1=[]
for item in dict_.items():
    data_1.append(item[1][2])
data_1=np.array(data_1).reshape(5,12).T
data_frame_task2=pd.DataFrame(index=range(1,13),columns=['A','B','C','D','E'],data=data_1)
data_frame_task2.plot()
plt.show()

data_frame_task22=[]
def huanbizengzhang(data):
    for i in range(5):
        for j in range(12):
            if j==0:
                data_frame_task22.append(0)
            else:
                data_frame_task22.append((data[j,i]-data[j-1,i])/data[j-1,i])
huanbizengzhang(data_frame_task2.values)
data_2=np.array(data_frame_task22).reshape(5,12).T
data_frame_task22=pd.DataFrame(index=range(1,13),columns=['A','B','C','D','E'],data=data_2)
data_frame_task22.plot.bar()
plt.show()
data_kind=pd.read_csv('zhuanhuan2.csv')
data_zong=pd.merge(data,data_kind,on=['商品'],how='inner')
print(data_zong['大类'].unique())
dict_yinliao={}
data_yinliao=[]
data_yinliao_ration=[]
for (k1,k2),group in data_zong.groupby(['地点','大类']):
    dict_yinliao[(k1,k2)]=group['实际金额'].sum()*(0.2 if group['大类'].str=='非饮料' else 0.25)
for item in dict_yinliao.items():
    data_yinliao.append(item[1])
for i in range(0,10,2):
    data_yinliao_ration.append(data_yinliao[i]/(data_yinliao[i]+data_yinliao[i+1]))
    data_yinliao_ration.append(data_yinliao[i+1]/(data_yinliao[i]+data_yinliao[i+1]))
data_yinliao_ration=pd.DataFrame(index=['非饮料','饮料'],columns=['A','B','C','D','E'],data=np.array(data_yinliao_ration).reshape(2,5))
print(data_yinliao_ration)
fig,axes=plt.subplots(3,2)
axes[0,0].pie(data_yinliao_ration['A'],labels=data_yinliao_ration.index,autopct='%1.1f%%',shadow=False,startangle=90)
axes[0,1].pie(data_yinliao_ration['B'],labels=data_yinliao_ration.index,autopct='%1.1f%%',shadow=False,startangle=90)
axes[1,0].pie(data_yinliao_ration['C'],labels=data_yinliao_ration.index,autopct='%1.1f%%',shadow=False,startangle=90)
axes[1,1].pie(data_yinliao_ration['D'],labels=data_yinliao_ration.index,autopct='%1.1f%%',shadow=False,startangle=90)
axes[2,0].pie(data_yinliao_ration['E'],labels=data_yinliao_ration.index,autopct='%1.1f%%',shadow=False,startangle=90)
plt.show()

