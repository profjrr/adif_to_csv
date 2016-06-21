import pandas as pd
import numpy as np

df=pd.read_csv("asian2016.csv")

#Group by call sign
band_grouping = df[['call','srx_string']].groupby('call')
#Count the sent Strings
bgc = band_grouping[['srx_string']].count().reset_index()
#Filter into an array of onlt Multiple QSO's
multi_qso=bgc[(bgc.srx_string != 1)]


multi_qso_full=pd.merge(df, multi_qso, on='call', how='inner')
multi_band_exchange=pd.pivot_table(multi_qso_full,index=['call','band'],values=['srx_string_x']).unstack().reset_index().fillna(0)


''' 
Loop through the rows
If someone sends more than 1 number - list the call - so I can check it
We would want to take the latest
'''
for index, row in multi_band_exchange.iterrows():
    sent_list=[]
    for items in range (1,len(row)):
        #print(str.format("{} -> {}",len(row),row[items]))
        if row[items] > 1.0:
            sent_list.append(row[items])
            #print(str.format("{} -> {}",row[0],row[items]))
        
    if len(list(set(sent_list)))>1:
        print(str.format("Check {} ",row[0]))
    
