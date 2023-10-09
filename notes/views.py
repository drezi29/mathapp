from django.views.generic.detail import BaseDetailView, DetailView

from chapters.chapter_constans import (
    CONTENT_IN_PREPARATION,
    EXERCISES,
    INDEX_OF_TOPICS,
    TEST,
)
from chapters.models import Topic

from .models import Note


class NoteBaseDetailView(BaseDetailView):
    def get_context_data(self, **kwargs):
        context = super(NoteBaseDetailView, self).get_context_data(**kwargs)
        context['index_of_topics'] = INDEX_OF_TOPICS
        context['content_in_preparation'] = CONTENT_IN_PREPARATION
        context['exercises'] = EXERCISES
        context['test'] = TEST
        return context


class NoteDetailView(NoteBaseDetailView, DetailView):
    model = Note
    slug_field = 'topic_id'

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        topic_id = self.kwargs['slug']
        note_elements = self.object.noteelement_set.all()
        context['note_elements'] = note_elements
        context['topic_id'] = topic_id
        context['elements_amount'] = len(note_elements)
        context['chapter_id'] = Topic.objects.get(id=topic_id).chapter.id
        return context
