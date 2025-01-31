N = int(input())
A = list(map(int, input().split()))

r = A[1] / A[0]

for i in range(N - 1):
    if A[i] * r != A[i + 1]:
        exit(print("No"))
print("Yes")