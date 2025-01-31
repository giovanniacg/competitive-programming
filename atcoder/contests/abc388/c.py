"""
Há N mochi (bolinhos de arroz) dispostos em ordem crescente de tamanho. O tamanho do i-th mochi (1 <= i <= N) é Ai.

Dado dois mochis A e B, com tamanhos a e b respectivamente, voce consegue pegar um kagamiochi (um bolo de arroz empilhado), colocando mochi A no topo do mochi B se e apenas se a é no máximo metade de b.

Você escolhe dois mochis dentre N mochi e coloque um em cima do outro para formar um kagamiochi.

Descubra quantos tipos diferentes de kagamiochi podem ser feitos.

Dois kagamiochis são distinguidos pelo menos um dos miochi for diferente, mesmo que os tamanhos dos mochi sejam os mesmos.

Nota: Posso empilhar no máximo 2 bolinhos
"""
N = int(input())

mochis = list(map(int, input().split()))

last = N - 1
result = 0
for i in range(N - 1, -1, -1):
    m = mochis[i]
    while m / 2 < mochis[last]:
        if last == 0:
            exit(print(result))
        last -= 1
    result += last + 1

print(result)

