import csv
import re
with open('tables/table3.csv', 'r') as infile, \
        open('tables/table3a.csv', 'w') as outfile:
    file = csv.reader(infile, skipinitialspace=True)
    writer = csv.writer(outfile,delimiter=',',quoting=csv.QUOTE_MINIMAL)

    # df.row.str.extract('(?P<fips>\d{5})((?P<state>[A-Z ]*$)|(?P<county>.*?), (?P<state_code>[A-Z]{2}$))')

    for index,line in enumerate(file):
        # print(line[0])
        column1 = re.search("^[a-zA-Z\s+()]+",line[0]).group(0)
        line = re.sub("^[a-zA-Z\s+()]+","",line[0])
        # print(type(line))
        column2 = re.search("^[0-9]{1,2}?(,[0-9]{1,3})+.[0-9][0-9]|^[0-9]+.[0-9][0-9]",line)
        if column2:
            column2 = column2.group(0)
        else:
            column2 = ''
        # print(column3)
        column3= re.sub("^[0-9]{1,2}?(,[0-9]{1,3})+.[0-9][0-9]|^[0-9]+.[0-9][0-9]","",line)
        row = (column1 + '|' + column2 + '|' + column3).split('|')
        if index == 0:
            writer.writerow(['ASSET CLASS','Value in Rs','%'])
        else:
            writer.writerow(row)
