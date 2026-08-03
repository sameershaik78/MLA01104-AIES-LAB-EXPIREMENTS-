human(socrates).

mortal(X):-
    human(X).

goal:-
    mortal(socrates),
    write('Socrates is mortal.'),
    nl.