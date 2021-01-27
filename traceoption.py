import pandas as pd
import datetime
import time
#显示所有列
pd.set_option('display.max_columns', 200)
#显示所有行
pd.set_option('display.max_rows', 200)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',250)

file='20210126'
df=pd.read_csv(file+'.csv')
df['dt']=file
df.shape
# df=df.drop('字段1',axis=1)
# df.columns=['Symbol','Expiration','Size','Strike','Spot','Received','Image','dt']
df['Type']=df['Image'].map(lambda x: 'Call' if 'QmCC' in x else 'Put')
df=df.drop('Image',axis=1)
# -----------------------------------------------------------------------------
boring_list=['AAPL','AMZN','MSFT','AMD','TSLA','BA','INTC','BAC','WFC','F','T','FB','C','MS']
df=df[~df.Symbol.isin(boring_list)].reset_index(drop=True)
# ----------------------------------------------------------
df['Cap']=df['Size'].map(lambda x: float(x[1:-1]) if 'K' in x else float(x[1:-1])*1000 )
df['diff'] = -df['Expiration'].map(lambda x: (datetime.datetime.strptime(time.strftime('%Y-%m-%d',time.localtime(time.time())),'%Y-%m-%d')-datetime.datetime.strptime(x,'%Y/%m/%d')).days)
df=df[df['diff']>0]
# --------------------------------------------------------------------
df_count=df['Cap'].groupby([df.Symbol,df.Type]).agg(['count','max']).sort_values(by='count',ascending=False).reset_index()
df_max=df['Cap'].groupby([df.Symbol,df.Type]).agg(['count','max']).sort_values(by='max',ascending=False).reset_index()


# --------------------------------------------------------------------------------------------------------------------------
# df_count_14=pd.read_csv('df_count_0114.csv',index_col=0)
# df_count_15=pd.read_csv('df_count_0115.csv',index_col=0)
def df_um(*kg):
    d=pd.DataFrame()
    for df in kg:
        d=pd.concat([d,df],axis=0)
    return d

    # df_um=df_count_14.merge(df_count_15,on='Symbol',how='inner')


