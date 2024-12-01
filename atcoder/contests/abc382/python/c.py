N, M = map(int, input().split())

peoples = list(map(int, input().split()))

sushis = sorted(
    [(i, g) for i, g in enumerate([int(x) for x in input().split()], start=1)],
    key=lambda x: x[1],
    reverse=True,
)

response = []

last = 0
for s in sushis:
    for i in range(last, len(peoples)):
        if peoples[i] <= s[1]:
            last = i
            response.append((s[0], i + 1))
            break
    else:
        last = len(peoples)
        response.append((s[0], -1))

print("\n".join([str(i) for s, i in sorted(response, key=lambda x: x[0])]))
