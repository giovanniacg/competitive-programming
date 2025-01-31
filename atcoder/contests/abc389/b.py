N = int(input())

r = 1
s = 1
for i in range(N):
    if s == N:
        break
    s *= r
    r += 1

print(r - 1) 
