import math

_ = input()

S = input().split()

"""
divisão:    1/2 / 3/4 -> a/b / c/d -> (a * d)/(b * c)
mult:       1/2 * 3/4 -> a/b * c/d -> (a * c)/(b * d)
soma:       1/2 + 3/4 -> a/b + c/d -> ((a * d) + (c * b))/(b * d)
sub:        1/2 - 3/4 -> a/b - c/d -> ((a * d) - (c * b))/(b * d)
"""

div = lambda a, b, c, d: f"{a * d}/{b * c}"
mul = lambda a, b, c, d: f"{a * c}/{b * d}"
som = lambda a, b, c, d: f"{(a * d) + (c * b)}/{b * d}"
sub = lambda a, b, c, d: f"{(a * d) - (c * b)}/{b * d}"

ops = {
    "/": div,
    "*": mul,
    "+": som,
    "-": sub,
}

def reduz_fracao(num, div):
    mdc = math.gcd(num, div)
    if mdc == 1:
        return f"{num}/{div}"
    return reduz_fracao(num // mdc, div // mdc)

is_op = lambda x: len(x) == 1

def get_first_op():
    first = -1
    for i, s in enumerate(S):
        if is_op(s) and (s == '*'):
            return i
        elif is_op(s) and (first == -1 or s == '/'):   
            first = i
    return first

while len(S) != 1:
    idx = get_first_op()
    f = ops[S[idx]]
    r = f(*map(int, S[idx - 1].split('/') + S[idx + 1].split('/')))
    S.pop(idx + 1); S.pop(idx)
    S[idx - 1] = r

print(reduz_fracao(*map(int, S[0].split('/'))))

