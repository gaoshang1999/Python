
# a = [1, 2, 3, 4]
# 
# b = [1 , 3, 5, ]
# 
# print( a & b     )

a = {1, 2, 3}
b = {1, 3, 5}
print( a & b     )
print( a | b     )
print( a - b     )
print( a ^ b     )

a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

print(a, b)
print( type(a.keys() ))
print(a.keys() & b.keys())