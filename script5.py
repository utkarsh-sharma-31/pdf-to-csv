import pandas as pd
import re
import numpy as np
import math
import csv

df1 = pd.read_csv("tables/table4a.csv")
df2 = pd.read_csv("tables/table4b.csv")

if '\n' in str(df1['Unnamed: 2'][0]) :
    df=df1
    req_column1 = 'Unnamed: 2'
    req_column2 = 'Unnamed: 3'
    req_column3 = 'Unnamed: 4'
    table_file =  "tables/table4a.csv"
else:
    df=df2
    req_column1 = 'Unnamed: 1'
    req_column2 = 'Unnamed: 2'
    req_column3 = 'Unnamed: 3'
    table_file = "tables/table4b.csv"

current_bal = []
free_bal = []
lent_bal = []

for name, value in df[req_column1].iteritems():
    split_cel = str(value).split('\n')
    if len(split_cel):
        current_bal.append(split_cel[0])
    else:
        current_bal.append(np.nan)

    if len(split_cel) > 1:
        free_bal.append(split_cel[1])
    else:
        free_bal.append((np.nan))

    if len(split_cel) > 2:
        lent_bal.append(split_cel[2])
    else:
        lent_bal.append(np.nan)

df[req_column1] = current_bal
df['Unnamed: 6'] = free_bal
df['Unnamed: 7'] = lent_bal

safekeep_bal=[]
locked_bal= []
pledge_bal=[]

for name, value in df[req_column2].iteritems():
    split_cel = str(value).split('\n')
    if len(split_cel):
        safekeep_bal.append(split_cel[0])
    else:
        safekeep_bal.append(np.nan)

    if len(split_cel) > 1:
        locked_bal.append(split_cel[1])
    else:
        locked_bal.append((np.nan))

    if len(split_cel) > 2:
        pledge_bal.append(split_cel[2])
    else:
        pledge_bal.append(np.nan)

df[req_column2] = safekeep_bal
df['Unnamed: 8'] = locked_bal
df['Unnamed: 9'] = pledge_bal

pledged_bal=[]
earmarked_bal=[]
pledgee_bal=[]


for name, value in df[req_column3].iteritems():
    split_cel = str(value).split('\n')
    if len(split_cel):
        pledged_bal.append(split_cel[0])
    else:
        pledged_bal.append(np.nan)

    if len(split_cel) > 1:
        earmarked_bal.append(split_cel[1])
    else:
        earmarked_bal.append((np.nan))

    if len(split_cel) > 2:
        pledgee_bal.append(split_cel[2])
    else:
        pledgee_bal.append(np.nan)

df[req_column3] = pledged_bal
df['Unnamed: 10'] = earmarked_bal
df['Unnamed: 11'] = pledgee_bal

df.to_csv(table_file)

