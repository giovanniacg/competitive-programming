isogram(Phrase):-
    string_lower(Phrase, Lower),
    re_replace('[^A-Za-z0-9]'/g, '', Lower, Result),
    atom_codes(Result, List),
    is_set(List).