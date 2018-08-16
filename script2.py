import os
import csv

base_command = 'java -jar tabula-1.0.2.jar -l -p all -f CSV -o {} {}'

# for filename in os.listdir(pdf_folder):
pdf_path = 'NSDL-CAS.pdf'
csv_path = 'all_tables.pdf'.replace('.pdf', '.csv')
command = base_command.format(csv_path, pdf_path)
os.system(command)


# def writeTable(start_string, end_string, current_index, specific_index, line, csv_writter):
#     if line[0].startswith(start_string):
#         specific_index = current_index
#         csv_writter.writerow(line)
#
#     elif current_index > specific_index and not line[0].startswith(end_string):
#         writer2.writerow(line)
#
#     elif index > specific_index and line[0].startswith(end_string):
#         specificIndex = 10000  # break for table2


with open('all_tables.csv', 'r', encoding='utf8') as t1, \
        open('tables/table1.csv', 'w') as outFile1, \
        open('tables/table2.csv', 'w') as outFile2, \
        open('tables/table3.csv', 'w') as outFile3, \
        open('tables/table4.csv', 'w') as outFile4, \
        open('tables/table5.csv', 'w') as outFile5, \
        open('tables/table6.csv', 'w') as outFile6, \
        open('tables/table7.csv', 'w') as outFile7, \
        open('tables/table8.csv', 'w') as outFile8, \
        open('tables/table9.csv', 'w') as outFile9:
    file = csv.reader(t1, skipinitialspace=True)
    writer1 = csv.writer(outFile1,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer2 = csv.writer(outFile2,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer3 = csv.writer(outFile3,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer4 = csv.writer(outFile4,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer5 = csv.writer(outFile5,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer6 = csv.writer(outFile6,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer7 = csv.writer(outFile8,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer9 = csv.writer(outFile9,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    # writer10 = csv.writer(outFile10,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    # writer11 = csv.writer(outFile11,delimiter=',',quoting=csv.QUOTE_MINIMAL)

    index1 = 10000
    index2 = 10000
    index3 = 10000
    index4 = 10000
    index5 = 10000
    index6 = 10000
    index7 = 10000
    index8 = 10000
    index9 = 10000

    for index,line in enumerate(file):
        print(line)
    #Table 1
        if line[0] == 'Account Type':
            index1=index
            writer1.writerow(line)

        elif index > index1 and line[0] != "Your e-Insurance Account (eIA) :  NONE WITH NSDL NATIONAL INSURANCE REPOSITORY(NIR)":
            writer1.writerow(line)

        elif index > index1 and line[0] == "Your e-Insurance Account (eIA) :  NONE WITH NSDL NATIONAL INSURANCE REPOSITORY(NIR)":
            index1=10000        # break for table1


    #Table2
        elif line[0] == 'Month':
            index2=index
            writer2.writerow(line)

        elif index > index2 and not line[0].startswith('Summary of value of'):
            writer2.writerow(line)

        elif index > index2 and line[0].startswith('Summary of value of'):
            index2=10000        # break for table2

    #Table3


        elif line[0] == 'ASSET CLASSValue in `%':
            index3=index
            writer3.writerow(line)


        elif index > index3 and not line[0].startswith('TOTAL'):

            writer3.writerow(line)

        elif index > index3 and line[0].startswith('TOTAL'):
            writer3.writerow(line)
            index3=10000        # break for table3

    #table4


        elif line[0] == 'Equities (E)':
            index4=index
            writer4.writerow(line)


        elif index > index4 and not line[0].startswith('Mutual Fund Folios (F)'):

            writer4.writerow(line)

        elif index > index4 and line[0].startswith('Mutual Fund Folios (F)'):
            index4=10000        # break for table4

    #table5


        elif line[0] == 'Mutual Fund Folios (F)':
            index5=index
            writer5.writerow(line)


        elif index > index5 and not line[0].startswith('ISIN'):

            writer5.writerow(line)

        elif index > index5 and line[0].startswith('ISIN'):
            index5=10000        # break for table4









