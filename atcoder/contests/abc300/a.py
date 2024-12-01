NAB = map(int, input().split())
N, A, B = NAB
choices = list(map(int, input().split()))
print(choices.index(A + B) + 1)
