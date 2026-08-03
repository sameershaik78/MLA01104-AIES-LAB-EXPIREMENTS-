disease(fever,flu).
disease(cough,cold).
disease(headache,migraine).
disease(stomach_pain,gastritis).

diagnose(Symptom,Disease):-
    disease(Symptom,Disease).