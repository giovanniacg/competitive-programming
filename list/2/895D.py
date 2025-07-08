def solve():
    import sys
    sys.setrecursionlimit(10**7)
    data = sys.stdin.read().split()
    if not data: 
        return
    a = data[0].strip()
    b = data[1].strip()
    n = len(a)
    mod = 10**9 + 7

    # Calcula a frequência de letras em a (o multiconjunto)
    freq_initial = [0] * 26
    for c in a:
        freq_initial[ord(c) - 97] += 1

    # Pré-calcula os fatoriais e invfatoriais até n
    fact = [1] * (n+1)
    invfact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i % mod
    invfact[n] = pow(fact[n], mod-2, mod)
    for i in range(n, 0, -1):
        invfact[i-1] = invfact[i] * i % mod

    # Retorna ways(rem, freq) = rem! / (Π (freq[l]!))
    def ways(rem, freq):
        res = fact[rem]
        for l in range(26):
            res = res * invfact[freq[l]] % mod
        return res

    # Conta quantas permutações (do multiconjunto) são lexicograficamente menores que x.
    def count_less(x, freq):
        total_rem = len(x)
        res = 0
        for i in range(len(x)):
            cur = ord(x[i]) - 97
            for l in range(cur):
                if freq[l] > 0:
                    freq[l] -= 1
                    res = (res + ways(total_rem - 1, freq)) % mod
                    freq[l] += 1
            if freq[cur] == 0:
                # x não pode ser formada (acabou a letra necessária)
                break
            freq[cur] -= 1
            total_rem -= 1
        return res

    # Calcula F(a) e F(b) usando cópias do vetor de frequências
    freq_a = freq_initial[:]  # cópia para calcular F(a)
    Fa = count_less(a, freq_a)
    freq_b = freq_initial[:]  # cópia para calcular F(b)
    Fb = count_less(b, freq_b)

    # O número de c tais que a < c < b é:
    # (número de permutações menores que b) - (número de permutações ≤ a)
    # Como a é uma permutação, seu rank (0-indexado) é F(a), assim:
    ans = (Fb - Fa - 1) % mod
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    solve()
