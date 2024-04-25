from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Chapter


class ChapterListView(ListView):
    model = Chapter
    classes_section = [1, 2, 3, 4]
    context_object_name = 'chapters'

    def get_context_data(self, *args, **kwargs):
        context = super(ChapterListView, self).get_context_data(**kwargs)
        context['classes_section'] = self.classes_section
        return context


class ChapterDetailView(DetailView):
    model = Chapter
