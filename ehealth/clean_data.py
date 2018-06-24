import re
from datetime import datetime
from datetime import timedelta  
import csv

def clean_date(dt): 
    '''
    :type dt: str, messy date 
    :rtype: str, clean date 
    '''
    ret = ""
    if re.match(r"\w+\s\d+\s\d+", dt) : 
        ret = datetime.strptime(dt, '%b %d %Y')
    elif re.match(r"(\d+)/(\d+)/(\d+)", dt) : 
        ret = datetime.strptime(dt, '%m/%d/%Y')
    elif re.match(r"(\d+)\-(\d+)\-(\d+)", dt) : 
        ret = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
    elif re.match(r"\d+", dt) :
        ret =  datetime.strptime("2010-12-01", '%Y-%m-%d')  + timedelta(days=( int(dt)-40513 ))  

    return ret.strftime('%Y-%m-%d') if ret else ""

def clean_id(cust_id):
    if cust_id:
        return str(int(float(cust_id)))
    return ""

if __name__ == '__main__':
    path = "C:/Users/gaosh/Downloads/data/"
    
    with open(path+'data3.csv') as infile, open(path+'data4.csv', 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        for cols in reader:   
            cols[1] = clean_id(cols[1])
            cols[2] = clean_date(cols[2])
            print(",".join(cols), file= outfile)