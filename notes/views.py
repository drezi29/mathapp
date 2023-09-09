from django.shortcuts import render
from django.views import View
from .models import Note
from chapters.models import Topic
from chapters.chapter_constans import CONTENT_IN_PREPARATION, EXERCISES, INDEX_OF_TOPICS, NOTES, TEST

class NoteView(View):
    def get(self, request, pk):
        note = Note.objects.get(topic=pk)
        note_elements = note.noteelement_set.all()
        chapter_id = Topic.objects.get(id=pk).chapter.id
        return render(request,
                      'chapters/note.html',
                      {
                          "note_elements": note_elements,
                          "note": note, "topic_id": pk,
                          "elements_amount": len(note_elements),
                          "chapter_id": chapter_id,
                          "index_of_topics" : INDEX_OF_TOPICS,
                          "exercises": EXERCISES,
                          "test": TEST,
                          "content_in_preparation": CONTENT_IN_PREPARATION
                      }
                      )
