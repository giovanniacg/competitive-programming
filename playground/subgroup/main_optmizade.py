from collections import defaultdict

l = list(map(int, input().split()))
l.sort()
n = len(l)

m = sum(l[-2:])

dp = defaultdict(int)
dp[0] = 1

for num in l:
    next_dp = dp.copy()
    for total in dp:
        new_total = total + num
        if new_total <= m:
            next_dp[new_total] += dp[total]
    dp = next_dp

print(max(dp.values()))
