from django.shortcuts import render
from django.views import View
from .models import Note


class NoteView(View):
    def get(self, request, pk):
        note = Note.objects.get(topic=pk)
        note_elements = note.noteelement_set.all()
        return render(request, 'chapters/note.html', {"note_elements": note_elements, "note": note, "topic_id": pk, "elements_amount": len(note_elements)})
