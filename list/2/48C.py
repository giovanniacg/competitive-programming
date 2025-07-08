def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    p = int(data[1])
    s = data[2].strip()
    
    half = n // 2
    if p > half:
        p = n - p + 1 

    total_change = 0
    diff_positions = []
    
    for i in range(1, half + 1):
        j = n - i + 1
        if s[i-1] != s[j-1]:
            diff = abs(ord(s[i-1]) - ord(s[j-1]))
            cost = min(diff, 26 - diff)
            total_change += cost
            diff_positions.append(i)
    
    if not diff_positions:
        print(0)
        return
    
    L = min(diff_positions)
    R = max(diff_positions)
    
    if p <= L:
        move_cost = R - p
    elif p >= R:
        move_cost = p - L
    else:
        move_cost = min(2*(p - L) + (R - p), 2*(R - p) + (p - L))
    
    print(total_change + move_cost)

if __name__ == '__main__':
    solve()
