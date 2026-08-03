parent(pam,bob).
parent(tom,bob).
parent(pam,liz).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).

male(tom).
male(bob).
male(pat).

female(pam).
female(liz).
female(ann).

father(X,Y):-
    parent(X,Y),
    male(X).

mother(X,Y):-
    parent(X,Y),
    female(X).

grandparent(X,Z):-
    parent(X,Y),
    parent(Y,Z).

brother(X,Y):-
    parent(P,X),
    parent(P,Y),
    male(X),
    X \= Y.

sister(X,Y):-
    parent(P,X),
    parent(P,Y),
    female(X),
    X \= Y.