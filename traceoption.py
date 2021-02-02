import pandas as pd
import datetime
import time
#显示所有列
pd.set_option('display.max_columns', 200)
#显示所有行
pd.set_option('display.max_rows', 200)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',250)

file='20210201'
df=pd.read_csv(file+'.csv')
df['dt']=file
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
df.to_csv('df_'+file[-4:]+'.csv')

# --------------------------------------------------------------------------------------------------------------------------
# df_count_14=pd.read_csv('df_count_0114.csv',index_col=0)
# df_count_15=pd.read_csv('df_count_0115.csv',index_col=0)
def um(cols=['01','02']):
    d=pd.DataFrame()
    import os
    for j in cols:
        for i in os.listdir(os.getcwd()):
            if 'df_'+j in i:
                df=pd.read_csv(i,index_col=0)
                d = pd.concat([d, df], axis=0,ignore_index=True)
    d['today'] = -d['Expiration'].map(lambda x: (
                datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())),
                                           '%Y-%m-%d') - datetime.datetime.strptime(x, '%Y/%m/%d')).days)
    d=d[d.today>0]
    d.reset_index(drop=True,inplace=True)
    return d

df_union=um()
df_union.to_csv('df_union.csv')
# df_union=pd.read_csv('df_union.csv')
a=df_union['dt'].groupby(df_union.Symbol).nunique()
b=df_union['dt'].groupby(df_union.Symbol).count()
c=df_union[df_union.Type=='Call']['dt'].groupby(df_union.Symbol).count()
d=df_union[df_union.Type=='Put']['dt'].groupby(df_union.Symbol).count()
e=pd.concat([a,b,c,d],axis=1)
e=e.reset_index()
e.columns=['Symbol','u_cnt','cnt','call','put']
e['if']=e.Symbol.map(lambda x:1 if x in df.Symbol.values else 0)
e=e.sort_values(by='u_cnt',ascending=True)



