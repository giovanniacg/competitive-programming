H, W = map(int, input().split())

cells = []

for _ in range(H):
    cells.append(list(input()))

visits = cells.copy()

"""
Retangulos possiveis:

1: horizontais

# | ## | ### | ...

2: verticais

# | # | # | ...
  | # | # |
  |   | # |

3: 1 e 2 de largura N
"""

def verify_d(v, can):
    if v[0][0] != -1: # diagonal superior direita -> precisa ter cel para direita e para cima
        if cells[v[4][0]][v[4][1]] not in can: # Direita
            return False
        if cells[v[6][0]][v[6][1]] not in can: # Cima
            return False
    
    if v[1][0] != -1: # diagonal inferior direita -> precisa ter cel para direita e para baixo
        if cells[v[4][0]][v[4][1]] not in can: # Direita
            return False
        if cells[v[7][0]][v[7][1]] not in can: # Baixo
            return False
    
    if v[2][0] != -1: # diagonal superior esquerda -> precisa ter cel para esquerda e para cima
        if cells[v[5][0]][v[5][1]] not in can: # Esquerda
            return False
        if cells[v[6][0]][v[6][1]] not in can: # Cima
            return False
    
    if v[2][0] != -1: # diagonal inferior esquerda -> precisa ter cel para esquerda e para baixo
        if cells[v[5][0]][v[5][1]] not in can: # Esquerda
            return False
        if cells[v[7][0]][v[7][1]] not in can: # Baixo
            return False
    
    return True

def verify_s(v):
    if v[4][0] != -1: # Direita
        if v[6][0] != -1: # Cima
            if v[0][0] == -1: # Precisa ter diagonal superior direita
                return False
        if v[7][0] != -1: # Baixo
            if v[1][0] == -1: # Precisa ter diagonal inferior direita
                return False
    
    if v[5][0] != -1: # Esquerda
        if v[6][0] != -1: # Cima
            if v[2][0] == -1: # Precisa ter diagonal superior esquerda
                return False
        if v[7][0] != -1: # Baixo
            if v[3][0] == -1: # Precisa ter diagonal inferior esquerda
                return False
    
    return True

def solve(x, y):
    pos = [
            [1, 1],     # 0: Diagonal superior direita
            [-1, 1],    # 1: Diagonal inferior direita
            [1, -1],    # 2: Diagonal superior esquerda
            [-1, -1],   # 3: Diagonal inferior esquerda
            [0, 1],     # 4: Direita
            [0, -1],    # 5: Esquerda
            [1, 0],     # 6: Cima
            [-1, 0],    # 7: Baixo
        ]
    can = ['#', '?', '@']
    v = [[-1, -1]] * len(pos)
    for i, xy in enumerate(pos):
        cell = [x + xy[0], y + xy[1]]
        
        if cell[0] < 0 or cell[0] > H - 1:
            continue
        if cell[1] < 0 or cell[1] > W -1:
            continue
        
        if cells[cell[0]][cell[1]] in can:
            v[i] = cell
            visits[cell[0]][cell[1]] = '@'
    
    if not verify_d(v, can): # Diagonais
        return False
    
    if not verify_s(v):
        return False
    
    if v[4][0] != -1: # Direita
        r = solve(v[4][0], v[4][1])
        if not r:
            return False
    
    if v[7][0] != -1: # Direita
        r = solve(v[7][0], v[7][1])
        if not r:
            return False
    
    return True
    

for x in range(H):
    for y in range(W):
        if cells[x][y] == '#':
            r = solve(x, y)
            if r:
                exit(print("Yes"))

print("No")



        
