from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

graph = [dict() for _ in range(N)]
adj = [set() for _ in range(N)]

for i in range(M):
    x, y, c = map(lambda x: int(x) - 1 if x.isdigit() else x, sys.stdin.readline().split())

    if c in graph[x]:
        graph[x][c].append(y)
    else:
        graph[x][c] = [y]
    if c in graph[y]:
        graph[y][c].append(x)
    else:
        graph[y][c] = [x]
    
    adj[x].add(y)
    adj[y].add(x)

# BFS

visited = [False] * (N * N)
q = deque()

start = 0
end = N - 1

INF = 10 ** 9
best = INF

"""
u = left search
v = right search
d = current distance
"""
q.append((start, end, 0)) # u, v, d

while q:
    u, v, d = q.popleft()

    if u == v:
        candidate = d * 2
        if candidate < best:
            best = candidate
    else:
        if v in adj[u]:
            candidate = d * 2 + 1
            if candidate < best:
                best = candidate
    
    if 2 * (d + 1) >= best:
        continue

    commom_c = set(graph[u].keys()) & set(graph[v].keys())

    for c in commom_c:
        for next_u in graph[u][c]:
            for next_v in graph[v][c]:
                idx = next_u * N + next_v
                if not visited[idx]:
                    q.append((next_u, next_v, d + 1))
                    visited[idx] = True
    
if best == INF:
    sys.stdout.write('-1\n')
else:
    sys.stdout.write(f"{best}\n")


