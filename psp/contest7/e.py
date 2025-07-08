def solve():    
    N, M = map(int, input().split())

    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

    parent = list(range(N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    for e in edges:
        union(*e)

    v_count = [0] * N
    e_count = [0] * N

    for i in range(N):
        v_count[find(i)] += 1

    for u, _ in edges:
        e_count[find(u)] += 1

    roots = {find(i) for i in range(N)}
    for s in roots:
        if v_count[s] != e_count[s]:
            return 0
            
    return pow(2, len(roots), 998244353)


print(solve())
