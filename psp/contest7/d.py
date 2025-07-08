from math import gcd

N = int(input())

towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

spells = set()

for i in range(N):
    for j in range(N):
        if j == i:
            continue
        x, y = (towns[i][0] - towns[j][0], towns[i][1] - towns[j][1])
        d = gcd(x, y)
        x, y = x // d, y // d 
        spells.add((x, y))


print(len(spells))