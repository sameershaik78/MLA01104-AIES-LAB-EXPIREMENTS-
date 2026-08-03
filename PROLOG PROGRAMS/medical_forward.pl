% -------------------------
% Medical Expert System
% Using Forward Chaining
% -------------------------

% Facts (Symptoms)

symptom(fever).
symptom(cough).
symptom(headache).

% Rules (Forward Chaining)

disease(flu) :-
    symptom(fever),
    symptom(cough).

disease(viral_fever) :-
    symptom(fever),
    symptom(headache).

medicine(flu, paracetamol).
medicine(viral_fever, rest).

% Diagnosis Rule

diagnose :-
    disease(D),
    write('Disease Diagnosed: '),
    write(D),
    nl,
    medicine(D,M),
    write('Suggested Medicine: '),
    write(M),
    nl.