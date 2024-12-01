_, D = map(int, input().split())
s = list(input())

for i in range(len(s) - 1, -1, -1):
    if D == 0:
        exit(print("".join(s)))

    if s[i] == "@":
        s[i] = "."
        D -= 1

print("".join(s))
