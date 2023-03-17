from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import ChaptersFilterForm
from .models import Chapter


class ChapterListView(ListView):
    model = Chapter

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        classes_section = [1,2,3,4]
        filter_form = ChaptersFilterForm(self.request.GET)

        if filter_form.is_valid():
            selected_classes = filter_form.cleaned_data.get('classes', '')
            extended_level = filter_form.cleaned_data.get('extended_level', '')

            classes_section = list(map(lambda x : int(x), selected_classes))
            if len(selected_classes)>0:
                queryset = queryset.filter(lic_class__in=classes_section)
            if not(extended_level):
                queryset = queryset.filter(is_extended=False)

        return super().get_context_data(
            filter_form=filter_form,
            chapters=queryset,
            classes_section=classes_section,
            **kwargs)

class ChapterDetailView(DetailView):
    model = Chapter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context