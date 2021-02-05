# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

df=pd.read_csv('Webull_Orders_Records.csv')

def df_stock(var,orient=True):
    var=str.upper(var)
    df_t=df.loc[(df.Symbol==var)&(df.Status=='Filled')]
    add1=(df_t.loc[df.Side=='Buy']['Filled']*df_t.loc[df.Side=='Buy']['Avg Price']).sum()
    add2 = (df_t.loc[df.Side == 'Sell']['Filled'] * df_t.loc[df.Side == 'Sell']['Avg Price']).sum()
    if orient==True:
        add=add2-add1
    else:
        add = add1 - add2
    print("%d 美元"%(round(add)))
    return df_t
def profit():
    for i in df.代码.uniques():
        add1 = (df.loc[df.方向 == '买入']['已成交'] * df.loc[df.方向 == '买入']['成交均价']).sum()
        add2 = (df.loc[df.方向 == '卖出']['已成交'] * df.loc[df.方向 == '卖出']['成交均价']).sum()


# spac=pd.read_csv(r'C:\Users\Marcus\Downloads\SPAC Spreadsheet - Sort, filter, and export the SPACTRAX list.csv')
# array(['2. Seeking Target', '5. Merger Complete', '1. New / Forming','3. Target Announced', '4. Deal Approved']




