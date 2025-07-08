:- initialization(main).

main :-
    read_line_to_codes(user_input, Line),   % https://www.swi-prolog.org/pldoc/man?predicate=read_line_to_codes/2
    string_codes(Str, Line),                % https://www.swi-prolog.org/pldoc/doc_for?object=string_codes/2
    split_string(Str, " ", "", [KS, SS]),   % https://www.swi-prolog.org/pldoc/doc_for?object=split_string/4
    number_string(K, KS),                   % https://www.swi-prolog.org/pldoc/doc_for?object=number_string/2
    number_string(S, SS),
    count_valid_triples(K, S, Count),
    writeln(Count),                         % https://www.swi-prolog.org/pldoc/doc_for?object=writeln/1
    halt.
    
count_valid_triples(K, S, Count) :-
    findall(_, (                            % https://www.swi-prolog.org/pldoc/man?predicate=findall/3
        between(0, K, X),                   % https://www.swi-prolog.org/pldoc/man?predicate=between/3
        between(0, K, Y),
        Z is S - X - Y,
        Z >= 0,
        Z =< K
    ), Triples),
    length(Triples, Count).                 % https://www.swi-prolog.org/pldoc/doc_for?object=length/2
