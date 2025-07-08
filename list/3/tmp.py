def manacher(s):
    # Transformar s em uma nova string com separadores para lidar com palíndromos de tamanho par
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    P = [0] * n
    center = right = 0
    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            P[i] = min(right - i, P[mirror])
        # Expande a partir de i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1
        # Atualiza center e right
        if i + P[i] > right:
            center, right = i, i + P[i]
    # P[i] indica o raio do palíndromo centrado em i na string transformada.
    # Para o maior palíndromo em s:
    max_len = max(P)
    center_index = P.index(max_len)
    start = (center_index - max_len) // 2  # converter para índice na s original
    return s[start: start + max_len]

# Exemplo:
s = "sssssssabacabadxxxxxxxxxxx"
print(manacher(s))  # -> maior substring palindrômica