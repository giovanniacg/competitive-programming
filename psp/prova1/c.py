import sys

data = sys.stdin.read().split()

N, Q = map(int, data[:2])

R = []
for i in range(N):
    R.append([i, int(data[i + 2])])

# O(NlogN)
R.sort(key=lambda x: x[1])

# O(logN)
def binary_search(s, e, t):
    if abs(s - e) == 1:
        return min([s, abs(R[s][1] - t)], [e, abs(R[e][1] - t)], key=lambda x: x[1])

    m = (s + e) // 2

    if R[m][1] > t:
        return binary_search(s, m, t)
    elif R[m][1] < t:
        return binary_search(m, e, t)

    return [m, m]

# O(NlogN)
for i in range(Q):
    v = int(data[N + 2 + i])
    print(R[binary_search(0, N - 1, v)[0]][0] + 1)