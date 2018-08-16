import pandas as pd


filename = str('tables/table1.csv')
df = pd.read_csv(filename,usecols=[1])
# print(df)
for name, values in df.iteritems():
    # print(type(name))
    print('{values}'.format(values=values))