S = input().split()

def strip(text: str) -> str:
    start = 0
    end = len(text)
    while start < end and not text[start].isalpha():
        start += 1
    while end > start and not text[end-1].isalpha():
        end -= 1
    return text[start:end]

for i in range(1, len(S)):
    if strip(S[i - 1].lower()) == "daniel" and strip(S[i].lower()) == "sad":
        a_idx = S[i].lower().find('a')
        S[i] = S[i][:a_idx] + S[i][a_idx] + S[i][a_idx:]

print(" ".join(S))