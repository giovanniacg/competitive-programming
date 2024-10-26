# URL: https://atcoder.jp/contests/abc337/tasks/abc337_c

# Plan:
# 1. Calcular o tatal de espaços no tabuleiro.
# 2. Criar uma tupla para armazenar as casas que as peças podem atacar e as que ocupam.
# 3. Interar sobre as peças para adicionar na tupla as casas que os cavalos podem atacar e as casas que eles ocupam.
#      Obs: As casas não podem ser negativas e nem maiores que o tamanho do tabuleiro.
# 4. Calcular o total de casas adicionadas na tupla.
# 5. subtrair do total de casas do tabuleiro.

"""
input:
8 6
1 4
2 1
3 8
4 5
5 2
8 3

output:
38
"""


def main():
    n, m = map(int, input().split())  # n = table size, m = number of pieces
    horses = [
        (x, y) for x, y in [map(int, input().split()) for _ in range(m)]
    ]  # list of horses positions
    board = n**2
    attack = set()
    for x, y in horses:
        if x - 2 > 0 and y - 1 > 0:
            attack.add((x - 2, y - 1))
        if x - 2 > 0 and y + 1 <= n:
            attack.add((x - 2, y + 1))
        if x + 2 <= n and y - 1 > 0:
            attack.add((x + 2, y - 1))
        if x + 2 <= n and y + 1 <= n:
            attack.add((x + 2, y + 1))
        if x - 1 > 0 and y - 2 > 0:
            attack.add((x - 1, y - 2))
        if x - 1 > 0 and y + 2 <= n:
            attack.add((x - 1, y + 2))
        if x + 1 <= n and y - 2 > 0:
            attack.add((x + 1, y - 2))
        if x + 1 <= n and y + 2 <= n:
            attack.add((x + 1, y + 2))

        attack.add((x, y))

    print(board - len(attack))


main()
