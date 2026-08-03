rain.
wet_grass :- rain.
slippery :- wet_grass.

forward :-
    wet_grass,
    slippery,
    write('Forward chaining successful.'),
    nl.