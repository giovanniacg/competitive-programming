def solve():
    S, T, X = map(int, input().split())
    
    invert = False
    if S > T:
        invert = True
    
    if invert:
        if (X < T) or (X >= S and X <= 23):
            print("Yes")
        else:
            print("No")
    else:
        if (X >= S and X <= T):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()