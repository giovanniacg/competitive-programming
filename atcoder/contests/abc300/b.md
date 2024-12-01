### Enunciado do Problema

Takahashi está desenvolvendo um RPG. Ele decidiu escrever um código para verificar se dois mapas são iguais.

Temos grades \( A \) e \( B \) com \( H \) linhas horizontais e \( W \) colunas verticais. Cada célula da grade contém um símbolo `#` ou `.`. Os símbolos na célula localizada na \( i \)-ésima linha a partir do topo e na \( j \)-ésima coluna a partir da esquerda em \( A \) e \( B \) são denotados por \( A_{i,j} \) e \( B_{i,j} \), respectivamente.

As seguintes duas operações são chamadas de **deslocamento vertical** e **deslocamento horizontal**:

1. Para cada \( j = 1, 2, \ldots, W \), faça simultaneamente:
   - Substitua simultaneamente \( A_{1,j}, A_{2,j}, \ldots, A_{H-1,j}, A_{H,j} \) por \( A_{2,j}, A_{3,j}, \ldots, A_{H,j}, A_{1,j} \).
   
2. Para cada \( i = 1, 2, \ldots, H \), faça simultaneamente:
   - Substitua simultaneamente \( A_{i,1}, A_{i,2}, \ldots, A_{i,W-1}, A_{i,W} \) por \( A_{i,2}, A_{i,3}, \ldots, A_{i,W}, A_{i,1} \).

O objetivo é determinar se existe um par de inteiros não-negativos \( (s, t) \) que satisfaça a seguinte condição:

Após aplicar \( s \) deslocamentos verticais e \( t \) deslocamentos horizontais, \( A \) é igual a \( B \).

Aqui, \( A \) é considerado igual a \( B \) se e somente se \( A_{i,j} = B_{i,j} \) para todos os pares de inteiros \( (i, j) \) tais que \( 1 \leq i \leq H \) e \( 1 \leq j \leq W \).

---

### Restrições
- \( 2 \leq H, W \leq 30 \)
- \( A_{i,j} \) é `#` ou `.`, assim como \( B_{i,j} \).
- \( H \) e \( W \) são inteiros.

---

### Entrada
A entrada é fornecida no seguinte formato:

```
H W
A_{1,1} A_{1,2} ... A_{1,W}
A_{2,1} A_{2,2} ... A_{2,W}
⋮
A_{H,1} A_{H,2} ... A_{H,W}
B_{1,1} B_{1,2} ... B_{1,W}
B_{2,1} B_{2,2} ... B_{2,W}
⋮
B_{H,1} B_{H,2} ... B_{H,W}
```

---

### Saída
Imprima `Yes` se existe um par \( (s, t) \) que satisfaz a condição. Caso contrário, imprima `No`.

---

### Exemplos de Entrada e Saída

#### Entrada 1
```
4 3
..#
...
.#.
...
#..
...
.#.
...
```

#### Saída 1
```
Yes
```

Explicação: Escolhendo \( (s, t) = (2, 1) \), \( A \) se torna igual a \( B \).

---

#### Entrada 2
```
3 2
##
##
#.
..
#.
#.
```

#### Saída 2
```
No
```

Explicação: Nenhuma escolha de \( (s, t) \) torna \( A \) igual a \( B \).

---

#### Entrada 3
```
4 5
#####
.#...
.##..
..##.
...##
#...#
#####
...#.
```

#### Saída 3
```
Yes
```

---

#### Entrada 4
```
10 30
..........##########..........
..........####....###.....##..
.....##....##......##...#####.
....####...##..#####...##...##
...##..##..##......##..##....#
#.##....##....##...##..##.....
..##....##.##..#####...##...##
..###..###..............##.##.
.#..####..#..............###..
#..........##.................
................#..........##.
######....................####
....###.....##............####
.....##...#####......##....##.
.#####...##...##....####...##.
.....##..##....#...##..##..##.
##...##..##.....#.##....##....
.#####...##...##..##....##.##.
..........##.##...###..###....
...........###...#..####..#...
```

#### Saída 4
```
Yes
```