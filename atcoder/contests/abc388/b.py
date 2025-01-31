"""
Existem N cobras

Inicialmente, a espessura da i-th cobra é Ti, e seu comprimento é Li

O peso de uma cobra é definito como produto de Ti (espessura) e Li (comprimento)

Para cada inteiro k que satisfaça 1 <= k <= D, encontre o peso da cobra mais pesada quando o comprimento (Li) de cada cobra aumento em k.


Saída:

Print D linhas. A k-th linha deve conter o peso da cobra mais pesada quando o comprimento de cada cobra tiver aumentado em k.
"""

N, D = map(int, input().split())


values = []
for _ in range(N):
    values.append(list(map(int, input().split())))

for i in range(D):
    values = [[t, l + 1] for t, l in values]
    m = max(values, key=lambda x: x[0] * x[1])
    print(m[0]*m[1])