sequencia(1, Acc) :-
    Acc = Acc + 2.

sequencia(2, Acc) :-
    Acc = Acc + 1.

sequencia(N, Acc) :-
    N > 2,
    sequencia(N - 1, Acc).

lucas(N, X) :-
    Acc = 0,
    sequencia(N, Acc),
    Acc =:= X.
