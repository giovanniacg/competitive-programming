def dfs(start):
    stack = [start]
    acc = 0

    while stack:
        c = stack.pop()
        if visit[c]:
            continue
        visit[c] = True

        acc += moves[c]

        for m in adj[c]:
            stack.append(m - 1)
    
    return acc


N = int(input())

adj = [[] for _ in range(N)]
visit = [False] * N
moves = []

for i in range(N):
    t, l, *ls = map(int, input().split())
    moves.append(t)

    if l:
        adj[i] = ls

print(dfs(N - 1))


