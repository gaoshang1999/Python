import csv
import json

path = "C:/Users/gaosh/Downloads/data/"
with open(path+'data2.csv') as infile, open(path+'t1.txt', 'w') as t1: #, open(path+'t2.txt', 'w') as t2:
    reader = csv.reader(infile)
    i = 1
    for cols in reader:
        print(i); i+=1
#         sql1 = "insert into invoice values('{0}', {1}, '{2}', '{3}');" 
        sql1 = "{0}\t{1}\t{2}\t{3}"
        s = sql1.format(cols[0], cols[1] or "", cols[2], cols[3])
        print(s, file= t1)
        
#         sql2 = "insert into purchase values('{0}', '{1}', {2}, '{3}', {4});"
#         sql2 = "{0}\t{1}\t{2}\t{3}\t{4}"
#         print(",".join(cols[4:]))
#         items = eval(",".join(cols[4:]).replace("\\", "\\\\"))
#         for it in items:
#             s2 = sql2.format(cols[0], it['ItemNo'],  it['UnitPrice'], it['Description'].replace("'", "\\'"), it['Quantity'])
#             print(s2, file= t2)