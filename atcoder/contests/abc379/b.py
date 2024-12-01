from itertools import groupby
import sys


def max_strawberries(K, S):
    healthy_segments = [len(list(group)) for char, group in groupby(S) if char == "O"]

    strawberries = sum(segment // K for segment in healthy_segments)

    return strawberries


input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

S = data[2]
print(max_strawberries(K, S))
