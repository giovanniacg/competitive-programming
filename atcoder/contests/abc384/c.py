from itertools import combinations

TYPES = ['A', 'B', 'C', 'D', 'E']
VALUES = list(map(int, input().split()))
l = list(zip(TYPES, VALUES))

all_players = []
for i in range(1, len(TYPES) + 1):
    for c in combinations(l, i):
        all_players.append(c)

sums = []

for p in all_players:
    p = list(p)
    sums.append(sum([x[1] for x in p]))

all_players = list(zip(all_players, sums))

all_players.sort()
all_players.sort(reverse=True, key=lambda x: x[1])

for p in all_players:
    p = list(p[0])
    p.sort(key=lambda x: x[0])
    print("".join([f"{a[0]}" for a in p]))