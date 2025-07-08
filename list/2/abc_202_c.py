N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))

D = [0] * (N + 1)
for i in range(N):
    if N >= C[i]:
        D[B[C[i]]] += 1

count = 0
for x in A:
    count += D[x]

print(count)