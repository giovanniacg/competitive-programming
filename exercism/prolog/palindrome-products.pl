palindrome(Num) :-
    number_chars(Num, Chars),
    reverse(Chars, Chars).

all_palindromic_products(Min, Max, Pairs) :-
    findall(
        Prod-(X,Y),
        (
            between(Min, Max, X),
            between(X, Max, Y),
            Prod is X * Y,
            palindrome(Prod)
        ),
        Pairs
    ).

smallest(MinFactor, MaxFactor, Smallest, Factors) :-
    all_palindromic_products(MinFactor, MaxFactor, Pairs),
    pairs_keys(Pairs, Prods),
    min_list(Prods, Smallest),
    findall(
        (X,Y),
        member(Smallest-(X,Y), Pairs),
        Factors
    ).

largest(MinFactor, MaxFactor, Largest, Factors) :-
    all_palindromic_products(MinFactor, MaxFactor, Pairs),
    pairs_keys(Pairs, Prods),
    max_list(Prods, Largest),
    findall(
        (X,Y),
        member(Largest-(X,Y), Pairs),
        Factors
    ).
