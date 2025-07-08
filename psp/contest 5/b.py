H, W = map(int, input().split())

m = []
for i in range(H):
    m.append(input().split())

m_t = []

for i in range(W):
    l_t = []
    for j in range(H):
        l_t.append(m[j][i])
    m_t.append(l_t)

for i in range(W):
    print(" ".join(m_t[i]))