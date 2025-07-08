D = False

if D:
    from pprint import pprint

N, M = map(int, input().split())


n = [list(map(int, input().split())) for _ in range(N)]
m = [list(map(int, input().split())) for _ in range(M)]

manhattan = lambda start, target: abs(start[0] - target[0]) + abs(start[1] - target[1])

for xy in n:
    if D:
        pprint(xy)
    r = []
    for i, _xy in enumerate(m):
        if _xy:
            r.append([i, manhattan(xy, _xy), _xy])
    
    if D:
        pprint(r)
    
    idx = min(r, key=lambda arr: arr[1])[0]
    # Can repeat?
    # m[idx] = []
    print(idx + 1)