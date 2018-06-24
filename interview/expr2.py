import re
import sys
import requests

from stack import Stack


url = "http://variableapi.azurewebsites.net/api/variable/" 
       
def expr(line):
    exprs = list(filter((lambda x: len(x) > 0 ), line.split(" ")))  
 
    if len(exprs) == 0 : 
        return ""
    stack = Stack()
    
    for e in exprs:              
        if re.match(r"@[a-z]+[0-9]+", e) : 
            r = requests.get(url + e[1:]) 
            stack.push(int(r.content))            
        elif re.match(r"-?\d+", e) :
            stack.push(e)
        elif re.match(r"[+|\-|*|/]", e):
            r = stack.pop()
            l = stack.pop()
            v = eval(str(l) + e + str(r) )
            stack.push(v)
        else :
            raise Exception("Illegal input at "+e)
        
    if stack.size() != 1:
        raise Exception("Illegal input of expression! ")     
           
    return stack.pop();       
            
if __name__=="__main__":          
    for line in sys.stdin:
        line = line.rstrip()
        if(line == 'q') : exit()
        try:
            print(expr(line))
        except Exception as ex:
            print(ex)
        
        

    


 

