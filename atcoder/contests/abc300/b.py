H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

found = False
for s in range(H):
    for t in range(W):
        match = True
        for i in range(H):
            for j in range(W):
                if A[(i + s) % H][(j + t) % W] != B[i][j]:
                    match = False
                    break
            if not match:
                break
        if match:
            found = True
            break
    if found:
        break

print("Yes" if found else "No")
