time('5am, wood again', 2, 'mg').
time('Amigos do Mortandela', 3, 'mg').
time('C++ ou uma linguagem misteriosa?', 2, 'go').
time('Lone Wolves', 2, 'df').
time('Monkeys', 1, 'go').
time('Teorema de Off', 1, 'df').
time('Teorema do Chin^es Viajante', 3, 'df').
time('Torcida P~ao de Alho', 1, 'mg').

campeao(X) :- time(X, 1, _).
selecionado(X) :- campeao(X).
selecionado(X) :- 
    time(X, _, 'mg'),
    \+ campeao(X).