def solve():
    import sys
    data = sys.stdin.read().splitlines()
    
    S = data[0].strip()
    A = data[1].strip()
    B = data[2].strip()

    forward = False
    pos_A = S.find(A)
    if pos_A != -1:
        pos_B = S.find(B, pos_A + len(A))
        if pos_B != -1:
            forward = True

    backward = False
    S_rev = S[::-1]
    pos_A_rev = S_rev.find(A)
    if pos_A_rev != -1:
        pos_B_rev = S_rev.find(B, pos_A_rev + len(A))
        if pos_B_rev != -1:
            backward = True

    if forward and backward:
        print("both")
    elif forward:
        print("forward")
    elif backward:
        print("backward")
    else:
        print("fantasy")

if __name__ == '__main__':
    solve()
