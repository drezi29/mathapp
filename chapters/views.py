from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Chapter, Note, Topic


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
    
class NoteView(View):
    def get(self, request, pk):
        note = Note.objects.get(topic=pk)
        note_elements = note.noteelement_set.all()
        return render(request, 'chapters/note.html', {"note_elements": note_elements, "note": note})