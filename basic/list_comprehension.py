noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]

print(noprimes)


primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)


# a = [ ["{} * {} = {}".format(j, i, i*j) for i in range(1, 5)] for j in range(1,i+1)]
# 
# print(a)

a = [i for x in ['b', 'c'] for i in ['a', x]]
print(a)