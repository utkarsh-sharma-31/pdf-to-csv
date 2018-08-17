import csv
import subprocess
import re
import pandas as pd
import sys
from os.path import relpath
import os
import re
import numpy as np

index_dict = {
    "index1" : 10000,
    "index2" : 10000,
    "index3" : 10000,
    "index4" : 10000,
    "index5" : 10000,
    "index6" : 10000,
    "index7" : 10000,
    "index8" : 10000,
    "index9" : 10000,
    "index10" : 10000
}

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def decrypt_file(filepath,password=None):
    base_command = 'java -jar {} -l -p all -s {} -f CSV -o {} {}'
    cwd = os.getcwd()
    if os.path.exists(filepath):
        pdf_path = relpath(filepath, cwd)
        print("%%%%%%%",pdf_path)
        tabula_abs_path = ROOT_DIR+'/tabula-1.0.2.jar'
        print(tabula_abs_path)
        tabula_path = relpath(tabula_abs_path,cwd)
        print("@@@@@",tabula_path)
    else:
        raise Exception("Given file path doesn't exist.")


    csv_path = 'all_tables.csv'
    command = base_command.format(tabula_path, password, csv_path, pdf_path)

    try:
        subprocess.call(command,shell=True)
    except OSError as e:
        raise ValueError(e)

    main_logic()



def writeTable1(start_string, end_string, current_index, specific_index, line, csv_writter,end_string_index=0,start_string2=None):
    if line[0].startswith(start_string):
        if start_string2:
            if line[1].startswith(start_string2):
                index_dict[specific_index] = current_index
                csv_writter.writerow(line)
                return True
        else:
            index_dict[specific_index] = current_index
            csv_writter.writerow(line)
            return True

    elif current_index > index_dict.get(specific_index) and not line[end_string_index].startswith(end_string):
        if not ''.join(line).strip() or not line[0].startswith('Page'):
            csv_writter.writerow(line)
        return True

    elif current_index > index_dict.get(specific_index) and line[end_string_index].startswith(end_string):
        csv_writter.writerow(line)
        index_dict[specific_index] = 10000  # break for table
        return False
    else:
        return False


def writeTable2(start_string, end_string, current_index, specific_index, line, csv_writter,end_string_index=0,start_string2=None):
    if line[0].startswith(start_string):
        if start_string2:
            if line[1].startswith(start_string2):
                index_dict[specific_index] = current_index
                csv_writter.writerow(line)
                return True
        else:
            index_dict[specific_index] = current_index
            csv_writter.writerow(line)
            return True

    elif current_index > index_dict.get(specific_index) and not line[end_string_index].startswith(end_string):
        if not ''.join(line).strip() or not line[0].startswith('Page'):
            csv_writter.writerow(line)
        return True

    elif current_index > index_dict.get(specific_index) and line[end_string_index].startswith(end_string):
        index_dict[specific_index] = 10000  # break for table
        return False
    else:
        return False


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
    df.to_csv('tables/table1a.csv')
    if os.path.isfile("tables/table1.csv"):
        os.remove("tables/table1.csv")


def table5_fix():
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
        if len(split_cel):
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
    if os.path.isfile("tables/table5.csv"):
        os.remove("tables/table5.csv")

def table3_fix():
    with open('tables/table3.csv', 'r') as infile, \
            open('tables/table3a.csv', 'w') as outfile:
        file = csv.reader(infile, skipinitialspace=True)
        writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        # df.row.str.extract('(?P<fips>\d{5})((?P<state>[A-Z ]*$)|(?P<county>.*?), (?P<state_code>[A-Z]{2}$))')

        for index, line in enumerate(file):
            column1 = re.search("^[a-zA-Z\s+()]+", line[0]).group(0)
            line = re.sub("^[a-zA-Z\s+()]+", "", line[0])
            column2 = re.search("^[0-9]{1,2}?(,[0-9]{1,3})+.[0-9][0-9]|^[0-9]+.[0-9][0-9]", line)
            if column2:
                column2 = column2.group(0)
            else:
                column2 = ''
            column3 = re.sub("^[0-9]{1,2}?(,[0-9]{1,3})+.[0-9][0-9]|^[0-9]+.[0-9][0-9]", "", line)
            row = (column1 + '|' + column2 + '|' + column3).split('|')
            if index == 0:
                writer.writerow(['ASSET CLASS', 'Value in Rs', '%'])
            else:
                writer.writerow(row)
    if os.path.isfile("tables/table3.csv"):
        os.remove("tables/table3.csv")


def table4_fix():
    filename = 'tables/table4.csv'
    df = pd.read_csv(filename, error_bad_lines=False)
    df.to_csv('tables/table4a.csv',index=False)

    with open('tables/table4.csv','r') as in_file, open('tables/table4a.csv','r') as in_file2, open('tables/table4b.csv','w') as outfile:
        reader1 = csv.reader(in_file2)
        row_list = list(reader1)
        reader2 = csv.reader(in_file)
        writer = csv.writer(outfile)
        for row in reader2:
            if row not in row_list:
                writer.writerow(row)
    if os.path.isfile("tables/table4.csv"):
        os.remove("tables/table4.csv")

    df1 = pd.read_csv("tables/table4a.csv")
    df2 = pd.read_csv("tables/table4b.csv")
    for name, value in df.iteritems():
        print(value)
        # split_cel = value.split('\n')
        # if len(split_cel)>0:
        #     isin_arr.append(split_cel[0])
        # else:
        #     isin_arr.append(np.nan)
        #
        # if len(split_cel)>1:
        #     ucc_arr.append(split_cel[1])
        # else:
        #     ucc_arr.append(np.nan)


def main_logic():
    with open('all_tables.csv', 'r', encoding='utf8') as t1, \
            open('tables/table1.csv', 'w') as outFile1, \
            open('tables/table2.csv', 'w') as outFile2, \
            open('tables/table3.csv', 'w') as outFile3, \
            open('tables/table4.csv', 'w') as outFile4, \
            open('tables/table5.csv', 'w') as outFile5, \
            open('tables/table6.csv', 'w') as outFile6, \
            open('tables/table7.csv', 'w') as outFile7, \
            open('tables/table8.csv', 'w') as outFile8, \
            open('tables/table9.csv', 'w') as outFile9, \
            open('tables/table10.csv', 'w') as outFile10:
        file = csv.reader(t1, skipinitialspace=True)
        writer1 = csv.writer(outFile1,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer2 = csv.writer(outFile2,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer3 = csv.writer(outFile3,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer4 = csv.writer(outFile4,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer5 = csv.writer(outFile5,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer6 = csv.writer(outFile6,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer7 = csv.writer(outFile7,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer8 = csv.writer(outFile8,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer9 = csv.writer(outFile9,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer10 = csv.writer(outFile10,delimiter=',',quoting=csv.QUOTE_MINIMAL)


        for index,line in enumerate(file):
            if writeTable1(start_string='Account Type',
                       end_string='Grand Total',
                       current_index=index,
                       end_string_index=1,
                       specific_index="index1",
                       line= line,
                       csv_writter = writer1) == True:
                continue

            if writeTable2(start_string='Month',
                       end_string='Summary of value of',
                       current_index=index,
                       specific_index="index2",
                       line= line,
                       csv_writter = writer2) == True:
                continue


            if writeTable1(start_string='ASSET CLASS',
                       end_string='TOTAL',
                       current_index=index,
                       specific_index="index3",
                       line= line,
                       csv_writter = writer3) == True:
                continue


            if writeTable1(start_string='Equities (E)',
                       end_string='Total',
                       current_index=index,
                       specific_index="index4",
                       line= line,
                       csv_writter = writer4) == True:
                continue

            if writeTable1(start_string='Mutual Fund Folios (F)',
                       end_string='Total',
                       current_index=index,
                       specific_index="index5",
                       line= line,
                       csv_writter = writer5) == True:
                continue


            if writeTable2(start_string='Date',
                        start_string2='Transaction Details',
                       end_string='NSDL DEMAT ACCOUNT',
                       current_index=index,
                       specific_index="index7",
                       line= line,
                          # end_string_index=1,
                       csv_writter = writer7) == True:
                continue

            if writeTable2(start_string='NSDL DEMAT ACCOUNT',
                       end_string='CDSL DEMAT ACCOUNT',
                       current_index=index,
                       specific_index="index8",
                       line= line,
                       csv_writter = writer8) == True:
                continue


            if writeTable2(start_string='CDSL DEMAT ACCOUNT',
                       end_string='Folio No.',
                       current_index=index,
                       specific_index="index9",
                       line= line,
                       csv_writter = writer9) == True:
                continue


            if writeTable2(start_string='Folio No.',
                       end_string='Page 7',
                       current_index=index,
                       specific_index="index10",
                       line= line,
                       csv_writter = writer10) == True:
                continue

    table1_fix()
    table5_fix()
    table3_fix()
    table4_fix()



if __name__ == "__main__":
    if len(sys.argv) > 2:
        decrypt_file(sys.argv[1],sys.argv[2])
    else:
        decrypt_file(sys.argv[1])