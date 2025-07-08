_ = input()
T = list(input())

dir_map = {
    0: (1, 0),
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}

current_dir_map = (0, 0)
current_dir = 0

sum_map = lambda x, y, z: [x[i] + n for i, n in enumerate(y[z])]
sum_dir = lambda x: x + 1 if x < 3 else 0

funcs = {
    "S": lambda: sum_map(current_dir_map, dir_map, current_dir),
    "R": lambda: sum_dir(current_dir)
}

for d in T:
    if d == "S":
        current_dir_map = funcs[d]()
    else:
        current_dir = funcs[d]()

print(*current_dir_map)