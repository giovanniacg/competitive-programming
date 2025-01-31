A = list(map(int, input().split()))

last = -1
swap = 0

for i in range(len(A)):
    if A[i] > last:
        last = A[i]
        continue

    tmp = A[i - 1]
    A[i - 1] = A[i]
    A[i] = tmp
    last = tmp
    swap += 1

if swap == 1:
    print("Yes")
else:
    print("No")