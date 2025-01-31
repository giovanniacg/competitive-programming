N = int(input())

mochis = list(map(int, input().split()))

i = 0
j = N // 2

count = 0

while i < N // 2 and j < N:
    if mochis[i] * 2 >= mochis[j]:
        count += 1
        i += 1
    
    j += 1

print(count)

