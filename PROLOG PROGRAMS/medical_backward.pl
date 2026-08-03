% Facts

symptom(fever).
symptom(cough).
symptom(headache).

% Rules

flu :-
    symptom(fever),
    symptom(cough).

viral_fever :-
    symptom(fever),
    symptom(headache).

cold :-
    symptom(cough).

% Medicines

medicine(flu, paracetamol).
medicine(viral_fever, rest).
medicine(cold, cetirizine).