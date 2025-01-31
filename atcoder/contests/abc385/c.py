N = int(input())
l = list(map(int, input().split()))

s: dict = {}

for i, n in enumerate(l):
    if n in s:
        s[n] = [*s[n], i]
    else:
        s[n] = [i]


m = 0
for n in s.items():
    interval = 0
    last = -1
    count = 1

    if len(n[1]) == 1:
        m = max(count, m)
        continue

    for v in n[1]:
        if interval != 0:
            if interval != v - last:
                interval = v - last
                count = 1
        elif last != -1:
            interval = v - last
        last = v
        count += 1
        m = max(count, m)

print(m)
