import random

l = []
for i in range(10**3):
    l.append(random.randint(1, 2000))

with open("input.txt", "w") as f:
    f.write(" ".join([f"{x}" for x in l]))
