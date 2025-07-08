def solve():
    import sys
    data = sys.stdin.read().split()
    N, K = map(int, data[:2])
    arr = list(map(int, data[2:]))

    sub_arr = {}

    # start arr with K elements
    for i in range(K):
        sub_arr[arr[i]] = sub_arr.get(arr[i], 0) + 1
    best = len(sub_arr.keys())
    
    for i in range(1, N - K + 1):
        # remove last
        last = arr[i - 1]
        sub_arr[last] -= 1
        if sub_arr[last] == 0:
            sub_arr.pop(last)
        
        # add new
        new = arr[i + K - 1]
        sub_arr[new] = sub_arr.get(new, 0) + 1

        # sum diferentes keys
        count = len(sub_arr.keys())
        if count > best:
            best = count
    
    print(best)
        

if __name__ == '__main__':
    solve()