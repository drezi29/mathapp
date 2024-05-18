#!/bin/bash

projectPath="."

cd "$projectPath"

declare -a fixtures=(
    "chapters/fixtures/chapters.json"
    "chapters/fixtures/topics.json"
    "exercises/fixtures/exercises.json"
    "exercises/fixtures/exercises_steps_powers_sqrts.json"
    "formulas/fixtures/formula_card_titles.json"
    "formulas/fixtures/formula_card_absolute_note.json"
    "formulas/fixtures/formula_card_absolute_note.json"
    "formulas/fixtures/formula_card_log_note.json"
    "formulas/fixtures/formula_card_newton_note.json"
    "formulas/fixtures/formula_card_power_note.json"
    "notes/fixtures/notes.json"
    "notes/fixtures/sqrt_power_ne.json"
    "quizzes/fixtures/quizzes.json"
    "quizzes/fixtures/quiz_sqrt_power_questions.json"
    "quizzes/fixtures/quiz_sqrt_power_answers.json"
)

for fixturePath in "${fixtures[@]}"; do
    if [ -f "$fixturePath" ]; then
        echo "Loading fixture: $fixturePath"
        python manage.py loaddata "$fixturePath"
    else
        echo "Fixture file not found: $fixturePath"
    fi
done
