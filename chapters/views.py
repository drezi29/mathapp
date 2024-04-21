from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .chapter_constans import (
    CLASS,
    EXERCISES,
    INDEX_OF_CHAPTERS,
    INDEX_OF_TOPICS,
    LEGEND,
    LVL_ADVANCED,
    LVL_BASIC,
    NOTES,
    TEST,
)
from .models import Chapter


class ChapterListView(ListView):
    classes_section = [1, 2, 3, 4]
    model = Chapter
    context_object_name = "chapters"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classes_section"] = self.classes_section
        context["index_of_chapters"] = INDEX_OF_CHAPTERS
        context["legend"] = LEGEND
        context["lvl_basic"] = LVL_BASIC
        context["lvl_advanced"] = LVL_ADVANCED
        context["class_const"] = CLASS
        return context


class ChapterDetailView(DetailView):
    model = Chapter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["index_of_topics"] = INDEX_OF_TOPICS
        context["notes"] = NOTES
        context["exercises"] = EXERCISES
        context["test"] = TEST
        return context
