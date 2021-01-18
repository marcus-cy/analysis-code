import pandas as pd
import datetime
import time
#显示所有列
pd.set_option('display.max_columns', 200)
#显示所有行
pd.set_option('display.max_rows', 200)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',200)


df=pd.read_csv('20210114.csv')
df.shape
df=df.drop('字段1',axis=1)
df.columns=['Symbol','Expiration','Size','Strike','Spot','Received','image']
df['Type']=df['image'].map(lambda x: 'Call' if 'QmCC' in x else 'Put')
df=df.drop('image',axis=1)
# -----------------------------------------------------------------------------
boring_list=['AAPL','AMZN','MSFT','AMD','TSLA','BA','INTC','BAC','WFC','F','T']
df=df[~df.Symbol.isin(boring_list)].reset_index(drop=True)
# ----------------------------------------------------------
df['Cap']=df['Size'].map(lambda x: float(x[1:-1]) if 'K' in x else float(x[1:-1])*1000 )
df['diff'] = -df['Expiration'].map(lambda x: (datetime.datetime.strptime(time.strftime('%Y-%m-%d',time.localtime(time.time())),'%Y-%m-%d')-datetime.datetime.strptime(x,'%Y/%m/%d')).days)

# --------------------------------------------------------------------
df_count=df['Cap'].groupby([df.Symbol,df.Type]).agg(['count','max']).sort_values(by='count',ascending=False).reset_index()



