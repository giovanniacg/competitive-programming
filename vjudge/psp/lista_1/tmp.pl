% Define peoples fact
% Esteban, Gustavo, Jaime, Malena, and Valeria.
people(esteban).
people(gustavo).
people(jaime).
people(malena).
people(valeria).

% Define the 'chatty' fact
chatty(people(gustavo)).
chatty(people(valeria)).

% Define the 'likes' fact
likes(people(esteban), people(malena)).
likes(people(malena), people(esteban)).
likes(people(gustavo), people(valeria)).

% Define the 'pairing' rule
pairing(people(A), people(B)) :-
    chatty(people(A));
    chatty(people(B));
    (
        likes(people(A), people(B)),
        likes(people(B), people(A))
    ).

% Define the 'seating' rule
seating(people(A), people(B), people(C), people(D), people(E)) :-
    pairing(A, B),
    pairing(B, C),
    pairing(C, D),
    pairing(D, E),
    is_set([A, B, C, D, E]).
