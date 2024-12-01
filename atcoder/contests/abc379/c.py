n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))

if sum(a) != n:
    exit(print(-1))

c = s = 0

for pos, stones in sorted(zip(x, a)):
    if c < pos - 1:
        exit(print(-1))
    c += stones
    s += pos * stones

print(n * (n + 1) // 2 - s)
