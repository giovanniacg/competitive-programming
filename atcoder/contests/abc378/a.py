from collections import defaultdict

hash_table = defaultdict(int)
[hash_table.__setitem__(x, hash_table[x] + 1) for x in map(int, input().split())]

print(sum(1 for count in hash_table.values() if count > 1))
