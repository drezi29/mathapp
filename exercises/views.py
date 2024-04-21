from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from chapters.chapter_constans import (
    CONTENT_IN_PREPARATION,
    INDEX_OF_TOPICS,
    NOTES,
    TEST,
)
from chapters.models import Topic
from formulas.models import Title

from .exercises_constans import (
    EXERCISE,
    LIST_OF_EXERCISES,
    PLACE_FOR_SOLUTION,
    SHOW_SOLUTION,
    STEP,
)
from .models import Exercise


class ExercisesListView(ListView):
    model = Exercise

    def get_context_data(self, **kwargs):
        context = super(ExercisesListView, self).get_context_data(**kwargs)
        topic_id = self.request.GET.get('topic')
        topic = get_object_or_404(Topic, id=topic_id)
        queryset = Exercise.objects.filter(topic=topic_id).order_by('order')
        context['exercises'] = queryset
        context['topic'] = topic
        context['exercises_amount'] = len(queryset)
        context['list_of_exercises'] = LIST_OF_EXERCISES
        context['index_of_topics'] = INDEX_OF_TOPICS
        context['content_in_preparation'] = CONTENT_IN_PREPARATION
        return context


class ExerciseDetailView(DetailView):
    model = Exercise
    formula_chapters = Title.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExerciseDetailView, self).get_context_data(**kwargs)
        context['formula_chapters'] = self.formula_chapters
        context['topic'] = Topic.objects.get(id=self.object.topic.id)
        context['steps'] = self.get_related_steps()
        context['test_const'] = TEST
        context['notes_const'] = NOTES
        context['step_const'] = STEP
        context['list_of_exercises'] = LIST_OF_EXERCISES
        context['place_for_solution'] = PLACE_FOR_SOLUTION
        context['show_solution'] = SHOW_SOLUTION
        context['exercise_const'] = EXERCISE
        return context

    def get_related_steps(self):
        queryset = self.object.step_set.all()
        paginator = Paginator(queryset, 1)
        page = self.request.GET.get('page')
        page_steps = paginator.get_page(page)
        return page_steps
