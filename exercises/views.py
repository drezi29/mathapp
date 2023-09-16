from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from chapters.chapter_constans import (CONTENT_IN_PREPARATION, INDEX_OF_TOPICS,
                                       NOTES, TEST)
from chapters.models import Topic
from formulas.models import FormulaNote, Title

from .exercises_constans import (EXERCISE, LIST_OF_EXERCISES,
                                 PLACE_FOR_SOLUTION, SHOW_SOLUTION, STEP)
from .models import Exercise, Step


class ExerciseListView(View):
    def get(self, request, pk):
        topic = Topic.objects.get(id=pk)
        exercises = Exercise.objects.filter(topic=pk).order_by('order')
        return render(
            request,
            'exercises/exercise-list.html',
            {
                'exercises': exercises,
                'topic': topic,
                'exercises_amount': len(exercises),
                'list_of_exercises': LIST_OF_EXERCISES,
                'index_of_topics': INDEX_OF_TOPICS,
                'content_in_preparation': CONTENT_IN_PREPARATION,
            },
        )


class ExerciseView(View):
    def get(self, request, pk):
        exercise = Exercise.objects.get(id=pk)
        topic = Topic.objects.get(id=exercise.topic.id)
        steps = Step.objects.filter(exercise=pk)
        formula_chapters = Title.objects.all()

        p = Paginator(steps, 1)
        page = request.GET.get('page')
        page_steps = p.get_page(page)

        return render(
            request,
            'exercises/exercise.html',
            {
                'exercise': exercise,
                'topic': topic,
                'steps': page_steps,
                'formula_chapters': formula_chapters,
                'test_const': TEST,
                'notes_const': NOTES,
                'step_const': STEP,
                'list_of_exercises': LIST_OF_EXERCISES,
                'place_for_solution': PLACE_FOR_SOLUTION,
                'show_solution': SHOW_SOLUTION,
                'exercise_const': EXERCISE,
            },
        )
