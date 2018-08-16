import PyPDF2
import os
# import tabula


filename='june_e_statement.pdf'

pdfFile = PyPDF2.PdfFileReader(open(filename,'rb'))
# if pdfFile.isEncrypted:
#     try:
#         pdfFile.decrypt('AMZPS1060M')
#         print('File Decrypted (PyPDF2)')
#     except:
command="cp "+filename+" temp.pdf; qpdf --password='utka3112' --decrypt temp.pdf "+filename
os.system(command)
print('File Decrypted (qpdf)')
#re-open the decrypted file
fp = open(filename)
pdfFile = PyPDF2.PdfFileReader(open(filename,'rb'))
print(pdfFile,"%%%%%")
# else:
#     print('File Not Encrypted')


# tabula.convert_into(filename, "output.json", output_format="csv",multiple_tables=True, encoding='utf-8',
#           pages = "2", guess = True, lattice = True, pandas_options={'header':None})
#
#
#
#
# with open('output.csv', 'r') as t1, open('table1.csv', 'w') as outFile1:
#     file = t1.readlines()
#     # writer = csv.writer(outFile1, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     for index,line in enumerate(file):
#
#         # if index > 2:
#         #     print(line)
#         if line.split(',')[0] == 'Your Demat Account and Mutual Fund Folios':
#             break
#         outFile1.write(line+'\n')
#
#         # if
#
#
