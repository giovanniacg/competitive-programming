def solve():
    s = input()
    n_total = len(s)
    s = s.lstrip("a")
    n_left = len(s)
    s = s.rstrip("a")
    n_right = len(s)

    if n_total - n_left > n_left - n_right and n_right != 0:
        return "No"
    
    n = len(s)
    for i in range(len(s) // 2):
        if s[i] != s[n - 1 - i]:
            return "No"
    return "Yes"

print(solve())