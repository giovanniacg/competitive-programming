from collections import defaultdict

N = int(input())

A = list(map(int, input().split()))

last_occurrence = defaultdict(lambda: -1)
B = []

for i in range(0, N):
    value = A[i]
    B.append(last_occurrence[value])
    last_occurrence[value] = i + 1

print(" ".join(map(str, B)))
