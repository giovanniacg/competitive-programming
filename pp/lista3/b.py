N, X = map(int, input().split())

boxes = list(map(int, input().split()))

# N >= 2

prev = boxes[0]

eats = 0
for i in range(1, N):
    excess = max(0, prev + boxes[i] - X)
    eats += excess
    prev = max(0, boxes[i] - excess)

print(eats)