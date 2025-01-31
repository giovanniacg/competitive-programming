def insert(x):
    queue[last_i[0]] = [x, head[0]]
    head[0] += x
    last_i[0] += 1

def remove():
    r = queue[r_count[0]]
    r_count[0] += 1
    r_values[0] += r[0]

def consult(x):
    x = queue[x - 1 + r_count[0]]
    print(x[1] - r_values[0])

head = [0]
r_values = [0]
r_count = [0]
last_i = [0]

op = [insert, remove, consult]
queue = [[0, 0]] * 300_005 # [len, current_head]

N = int(input())

for _ in range(N):
    i = list(map(int, input().split()))
    if len(i) == 1:
        op[1]()
    else:
        op[i[0] - 1](i[1])