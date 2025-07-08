N, X = map(int, input().split())
friends = list(map(int, input().split()))

X -= 1

know = [False for _ in range(N + 1)]
know[X] = True
count = 1

while True:
    if not know[friends[X] - 1]:
        know[friends[X] - 1] = True
        X = friends[X] - 1
        count += 1
    else:
        break

print(count)