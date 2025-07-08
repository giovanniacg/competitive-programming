def lr_insertion(N: int, S: str):
    left  = [-1] * (N+1)
    right = [-1] * (N+1)

    for i, c in enumerate(S, start=1):
        print(f"left:  {left}")
        print(f"right: {right}")
        print("-" * 10)
        if c == 'L':
            left[i]  = left[i-1]
            right[i] = i-1
            if left[i] != -1:
                right[left[i]] = i
            left[i-1] = i
        else:
            right[i] = right[i-1]
            left[i]  = i-1
            if right[i] != -1:
                left[right[i]] = i
            right[i-1] = i

    head = 0
    while left[head] != -1:
        head = left[head]

    result = []
    node = head
    while node != -1:
        result.append(node)
        node = right[node]

    return result


def solve():
    import sys
    data = sys.stdin.read().split()
    N, S = int(data[0]), data[1].strip()
    return  lr_insertion(N, S)
    

print(*solve())
