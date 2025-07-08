S = list(input())

response = ""
for c in S:
    if c.isupper():
        response += c

print(response)