def solve():
    import sys
    from itertools import permutations
    data = sys.stdin.read().split()
    S = data[0]
    K = int(data[1])
    
    perms = set(permutations(S))
    perms_str = ["".join(s) for s in perms]
    perms_str.sort()
    
    print(perms_str[K - 1])

if __name__ == '__main__':
    solve()