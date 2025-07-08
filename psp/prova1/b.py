N, M = map(int, input().split())

E = list(map(int, input().split()))
B = list(map(int, input().split()))

# O(NlogN)
E.sort(reverse=True)
B.sort(reverse=True)

i = 0
j = 0

count = 0

# O(N)
while i < N and j < M:
    if E[i] >= B[j]:
        count += 1
        i += 1
    j += 1

print(count)