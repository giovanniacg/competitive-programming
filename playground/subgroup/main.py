from tqdm import tqdm


def get_package(i, l):  # O(n)
    p = []
    q = []

    for b in l:
        if b > i:
            return p

        if b == i:
            p.append([i])
        else:
            c = 0
            while q:
                if q[c] + b > i:
                    return p
                elif q[c] + b == i:
                    p.append([q.pop(c), b])
                    break
                else:
                    c += 1

                if c >= len(q):
                    q.append(b)
                    break
            else:
                q.append(b)
    return p


l = list(map(int, input().split()))

l.sort()  # O(n.log(n))

m = sum(l[-2:])

packages = []

for i in tqdm(range(1, m + 1), desc="Processando", unit="iteração"):  # O(m.n)
    p = get_package(i, l)

    if p:
        packages.append(p)

print(
    "\n".join(
        [f"{i:5}: {content}" for i, content in [(sum(p[0]), p) for p in packages]]
    )
)
print()

p_counts = [len(pkg) for pkg in packages]
print(max(p_counts))
