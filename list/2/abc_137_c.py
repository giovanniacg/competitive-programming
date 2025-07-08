from functools import reduce
from math import factorial

N = int(input())

hashtable = {}

for _ in range(N):
    tmp = "".join(sorted(input()))

    if tmp in hashtable:
        hashtable[tmp] += 1
    else:
        hashtable[tmp] = 0

for x in hashtable.keys():
    v = hashtable[x]
    hashtable[x] = v if v <= 1 else factorial(v + 1)/(2 * factorial(v + 1 - 2))
    

print(int(reduce(lambda x, y: x + y, hashtable.values())))