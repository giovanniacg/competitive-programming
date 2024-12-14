RANGE_1 = [1600, 2799]
RANGE_2 = [1200, 2399]
RANGES = [RANGE_1, RANGE_2]

N, R = map(int, input().split())

for i in range(N):
    d, a = map(int, input().split())
    R += a if R >= RANGES[d - 1][0] and R <= RANGES[d - 1][1] else 0

print(R)
