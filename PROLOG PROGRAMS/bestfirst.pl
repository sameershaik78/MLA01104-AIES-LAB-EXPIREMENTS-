edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(e,g).

best_first(Start,Goal):-
    path(Start,Goal).

path(Goal,Goal):-
    write(Goal),nl.

path(Start,Goal):-
    write(Start),
    write(' -> '),
    edge(Start,Next),
    path(Next,Goal).