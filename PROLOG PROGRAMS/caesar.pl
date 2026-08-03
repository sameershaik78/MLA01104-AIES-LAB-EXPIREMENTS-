% Facts

man(marcus).
pompeian(marcus).

ruler(caesar).

% Rules

roman(X) :-
    pompeian(X).

loyal_to(X, caesar) :-
    roman(X).

loyal_to(X, someone) :-
    man(X).

assassinate(X, Y) :-
    ruler(Y),
    \+ loyal_to(X, Y).