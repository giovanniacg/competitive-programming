"""
Declaração do problema
Você recebe uma string
Sde comprimento
3composto por letras maiúsculas em inglês.

Determinar se é possível reorganizar os caracteres em
Spara fazer com que corresponda à string ABC.

Restrições
Sé uma sequência de comprimento
3composto por letras maiúsculas em inglês.
"""

S: str = input()

if "A" in S and "B" in S and "C" in S:
    print("Yes")
else:
    print("No")
