from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Chapter, Topic


class ChapterListView(ListView):
    model = Chapter

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        classes_section = [1,2,3,4]

        return super().get_context_data(
            chapters=queryset,
            classes_section=classes_section,
            **kwargs)

class ChapterDetailView(DetailView):
    model = Chapter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context