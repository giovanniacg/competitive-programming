import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    arr = list(map(int, data[1:]))

    total = N * (N - 1) // 2
    eq = {}
    for n in arr:
        eq[n] = eq.get(n, 0) + 1
    
    total_eq = 0
    for count in eq.values():
        total_eq += count * (count - 1) // 2
    
    print(total - total_eq)


if __name__ == '__main__':
    solve()
