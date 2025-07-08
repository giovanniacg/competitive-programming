p(a, b).
p(a, c).
p(b, c).
p(b, a).
p(b).

g(a).
g(b).
g(a, b).
g(c, a).

is_algo(X, Y) :-
    g(X, Y),
    p(Y, X).
