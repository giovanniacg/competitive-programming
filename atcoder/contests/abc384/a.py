import re

_, C1, C2 = map(str, input().split())

print(re.sub(rf"[^{C1}]", C2, input()))
