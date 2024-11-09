def next_day_collect(current_day, q, r):
    if current_day % q == r:
        return current_day
    return current_day + (r - current_day % q + q) % q


N = int(input())
collects = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
consul = [tuple(map(int, input().split())) for _ in range(Q)]

results = list(
    map(
        lambda query: next_day_collect(query[1], *collects[query[0] - 1]),
        consul,
    )
)

print(*results, sep="\n")
