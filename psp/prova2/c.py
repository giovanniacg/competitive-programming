N = int(input())
print(1)

can_use = set()

for i in range(2, 2*N+2):
    can_use.add(i)


aoki = int(input())
while aoki:
    can_use.remove(aoki)
    print(can_use.pop())
    aoki = int(input())
