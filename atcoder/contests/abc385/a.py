l = list(map(int, input().split()))

cs = {}

for i in range(1, 1 << 3):
    c = [l[j] for j in range(3) if (i & (1 << j)) > 0]
    s = sum(c)
    if s in cs:
        print("Yes")
        break
    cs[s] = 1
else:
    print("No")
