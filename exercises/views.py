from django.shortcuts import render
from django.views import View
from .models import Exercise
from chapters.models import Topic


class ExerciseListView(View):
    def get(self, request, pk):
        topic = Topic.objects.get(id=pk)
        exercises = Exercise.objects.filter(topic=pk)
        return render(request, 'exercises/exercise-list.html', {"exercises": exercises, "topic": topic})
