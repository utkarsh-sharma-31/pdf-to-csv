import pandas as pd
import re
import numpy as np
import math

def table1_fix():
    filename = 'tables/table1.csv'
    df = pd.read_csv(filename)

    dp_id_arr=[]
    client_id_arr=[]
    account_details_arr=[]
    for name, value in df['Account Details'].iteritems():
        dp_id = re.search('DP ID:+(\w+)', value)
        if dp_id:
            dp_id_arr.append(dp_id.group(1))
        else:
            dp_id_arr.append(np.nan)

        client_id = re.search('Client ID:+(\w+)', value)
        if client_id:
            client_id_arr.append(client_id.group(1))
        else:
            client_id_arr.append(np.nan)
        account_details_arr.append(value.split('\n')[0])

    df=df.assign(DP_ID = dp_id_arr,Client_id=client_id_arr)
    df['Account Details']=account_details_arr
    df = df[['Account Type', 'Account Details', 'DP_ID', 'Client_id','No. of\nISINs / Schemes', 'Value in `']]
    # for name, value in df.iteritems():
    #     print(value)

    df.to_csv('tables/table1a.csv')



with open('tables/table5.csv','r') as in_file, open('tables/table5a.csv','w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)

filename = 'tables/table5a.csv'
df = pd.read_csv(filename)
df.columns = ['Mutual Fund Folios (F)', 'a','b','c','d','e','f','i','j','k']
df = df[pd.notnull(df['a'])]
df.to_csv('tables/table5.csv', index=False)

isin_arr = []
ucc_arr = []
for name, value in df['Mutual Fund Folios (F)'].iteritems():
    split_cel = value.split('\n')
    if len(split_cel)>0:
        isin_arr.append(split_cel[0])
    else:
        isin_arr.append(np.nan)

    if len(split_cel)>1:
        ucc_arr.append(split_cel[1])
    else:
        ucc_arr.append(np.nan)
df['Mutual Fund Folios (F)'] = isin_arr
df=df.assign(UCC = ucc_arr)
df = df[['Mutual Fund Folios (F)','UCC', 'a','b','c','d','e','f','i','j','k']]
df.to_csv('tables/table5a.csv', index=False)