import sys
import threading


def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    H, W, K = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(H)]
    total_paths = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[False] * W for _ in range(H)]

    def dfs(x, y, moves_left):
        nonlocal total_paths
        if moves_left == 0:
            total_paths += 1
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < H
                and 0 <= ny < W
                and grid[nx][ny] == "."
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                dfs(nx, ny, moves_left - 1)
                visited[nx][ny] = False

    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                visited[i][j] = True
                dfs(i, j, K)
                visited[i][j] = False

    print(total_paths)


threading.Thread(target=main).start()
