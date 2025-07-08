n = int(input())

p = pow(2, 31)
less = p * -1
greater = p - 1

if n <= greater and n >= less:
    print("Yes")
else:
    print("No")