from itertools import permutations
from functools import reduce

N = int(input())
A = list(map(int, input().split()))


def solve(n, l: list, xors: dict):
    for c in permutations(range(n), 2):
        lc = l.copy()
        lc[c[1]] += lc[c[0]]
        lc.pop(c[0])
        r = reduce(lambda x, y: x ^ y, l)
        if not xors.get(r):
            xors[r] = 1
        s = solve(n - 1, lc, xors)

        for i in s:
            if not xors.get(i):
                xors[i] = 1
    return xors


xors = {}
s = solve(N, A, xors)
print(s)
print(len(s))