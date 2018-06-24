def my(array):
    mylist = []
    for i in range(len(array)):
        for j in range(len(array)):
            e1 = array[i]
            e2 = array[j]
            if e1 == e2 and i != j:
                if e2 not in mylist:
                    mylist.append(e2)
    return mylist


def my2(array):
    n = len(array)
    mylist = [0 for _ in range(n)]
    dictionary = {}
    for i in range(n):
        a = array[i]
        if a in dictionary:
            if dictionary[a] >= 0: # if element appears twice, mark index of mylist to 1
                mylist[dictionary[a]] = 1
            dictionary[a] = -1
        else: # record the index where first time an element appear
            dictionary[a] = i

    print(dictionary)
    print(mylist)
    return [x[1] for x in zip(mylist,array) if x[0] == 1]
        


from random import randint

for _ in range(1):
    a = [ randint(0,9) for _ in range(10)]
    
    print(a)
    
    print(my(a))
    print(my2(a))
    print(my(a) ==  my2(a) )
    assert(my(a) ==  my2(a) )

def myImplement(array):
    n = len(array)
    mylist = [0 for _ in range(n)]
    dictionary = {}
    for i in range(n):
        a = array[i]
        if a in dictionary:
            if dictionary[a] >= 0: # if element appears twice, mark index of mylist to 1
                mylist[dictionary[a]] = 1
            dictionary[a] = -1
        else: # record the index where first time an element appear
            dictionary[a] = i

    return [x[1] for x in zip(mylist,array) if x[0] == 1]