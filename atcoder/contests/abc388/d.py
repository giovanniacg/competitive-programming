"""
Em um certo planeta, existem N aliens, todos menores de idade.

O i-th alien atualmente tem Ai pedras, e consegue ser adulto exatamente i anos depois.

Quando alguem vira adulto nesse planeta, todo adulto que tem pelo menos uma pedra dá exatamnte 
uma pedra como presente de felicitação ao aliem que acabou de se tornar adulto.

Descubra quantas pedras cada alienígena terá depois de N anos.

Suponha que nenhum novo aliem nascerá no futuro
""" 

N = int(input())

aliens = list(map(int, input().split()))

delta = [0] * (N + 1)

give_stones = 0

for i in range(N):
    give_stones += delta[i]
    aliens[i] += give_stones

    end = min(N - 1, i + aliens[i])

    aliens[i] -= end - i

    delta[i] += 1
    delta[end + 1] -= 1
    give_stones += 1

print(" ".join(map(str, aliens)))
