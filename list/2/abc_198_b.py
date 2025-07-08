S = input()
x = S.count('0') + 1

for i in range(x):
    T = "0" * i + S
    if T == T[::-1]:
        exit(print("Yes"))

print("No")