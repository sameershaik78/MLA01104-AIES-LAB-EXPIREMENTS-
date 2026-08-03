bird(parrot).
bird(sparrow).
bird(pigeon).
bird(penguin).
bird(ostrich).

cannot_fly(penguin).
cannot_fly(ostrich).

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).