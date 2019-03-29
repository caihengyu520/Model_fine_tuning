import pandas as pd
data=pd.read_csv('附件2.csv',encoding='GB18030')
data.to_csv('zhuanhuan2.csv',index=None,encoding='utf-8')