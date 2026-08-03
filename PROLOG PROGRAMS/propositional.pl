% ---------- Facts ----------

% Apple and vegetables are food
food(apple).
food(vegetable).

% John likes peanuts
likes(john, peanuts).

% Anil eats peanuts and is alive
eats(anil, peanuts).
alive(anil).

% Harry eats everything that Anil eats
eats(harry, X) :-
    eats(anil, X).

% ---------- Rules ----------

% John likes all kinds of food
likes(john, X) :-
    food(X).

% Anything anyone eats and is not killed is food
food(X) :-
    eats(_, X),
    \+ killed_by(X).

% Facts about things that are not killed
killed_by(poison).