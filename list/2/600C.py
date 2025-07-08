def solve():
    import sys
    s = sys.stdin.readline().strip()
    n = len(s)
    
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    
    allowed = 1 if n % 2 == 1 else 0
    
    odd_count = sum(1 for count in freq if count % 2 == 1)
    
    while odd_count > allowed:
        i = 0
        j = 25
        while i < 26 and freq[i] % 2 == 0:
            i += 1
        while j >= 0 and freq[j] % 2 == 0:
            j -= 1
        freq[i] += 1
        freq[j] -= 1
        odd_count -= 2
    
    left_half = []
    middle = ""
    for i in range(26):
        if freq[i] % 2 == 1:
            middle = chr(i + ord('a'))
        left_half.append(chr(i + ord('a')) * (freq[i] // 2))
    
    left_half_str = "".join(left_half)
    right_half_str = left_half_str[::-1]
    
    result = left_half_str + middle + right_half_str
    sys.stdout.write(result)

if __name__ == '__main__':
    solve()
