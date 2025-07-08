N = int(input())

ls = set()
for _ in range(N):
    _, *s = map(int, input().split())
    ls.add("-".join(map(str, s)))

print(ls)
print(len(ls))