# url:

# E - Permute K times 2

# Plan:

# 1. Transformar P em 0-indexed
# 2. Encontrar o ciclo de P que se repete
# 3. Calcular resto da divisão de K pelo tamanho do ciclo
# 4. Aplicar o resto da divisão de K vezes em P
# 4. Transformar P em 1-indexed


def perform_operations(N, K, P):
    P = [p - 1 for p in P]

    visited = [-1] * N
    cycle_length = 0
    current = 0

    while visited[current] == -1:
        visited[current] = cycle_length
        current = P[current]
        cycle_length += 1

    K %= cycle_length

    for _ in range(K):
        P = [P[p] for p in P]

    P = [p + 1 for p in P]

    return P


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    result = perform_operations(N, K, P)
    print(*result)


main()
