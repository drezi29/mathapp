from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from .models import Exercise, Step
from chapters.models import Topic


class ExerciseListView(View):
    def get(self, request, pk):
        topic = Topic.objects.get(id=pk)
        exercises = Exercise.objects.filter(topic=pk).order_by('order')
        return render(request, 'exercises/exercise-list.html', {"exercises": exercises, "topic": topic})


def exercise_view(request, pk):
    exercise = Exercise.objects.get(id=pk)
    topic = Topic.objects.get(id=exercise.topic.id)
    steps = Step.objects.filter(exercise=pk)

    p = Paginator(steps, 1)
    page = request.GET.get('page')
    page_steps = p.get_page(page)

    return render(request, 'exercises/exercise.html', {"exercise": exercise, "topic": topic, "steps": page_steps})