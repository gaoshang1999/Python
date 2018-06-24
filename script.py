import re

f = open('C:/Learn/scala/scala-workspace/Scala/src/leetcode/dp/test.txt')
c = 0
a1 = set()
a2 = set()
a3 = set()
a_other = set()
for line in f :
    line = line.strip()
    if line:
        if line[1] == "1":
            a1.add(line)
        if line[2] == "1":
            a2.add(line)
        if line[3] == "1":
            a3.add(line)
        if "1" not in line[1:]:
            a_other.add(line)
            print(line)

print(len(a1))
print(len(a2))
print(len(a3))
print(len(a_other))
print(  (a1 & a2))  
print(  (a1 & a3)) 
print(  (a2 & a3)) 
print(  (a1 & a2 & a3))

print( len(a1 & a2))
print( len(a1 & a3))
print( len(a2 & a3))
print( len(a1 & a2 & a3))
print( len(a1 | a2  ))
print( len(a1 | a2 | a3))