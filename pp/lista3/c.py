N = int(input())

min_t = 1
min_a = 1
for _ in range(N):
    t, a = map(int, input().split())
    k1 = (min_t + t - 1) // t
    k2 = (min_a + a - 1) // a
    k  = max(k1, k2)
    min_t = k * t
    min_a = k * a

print(int(min_a + min_t))