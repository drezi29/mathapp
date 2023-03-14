from django.urls import path
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Chapter
from .views import ChapterListView
# from .views import getAllChapters

urlpatterns = [
    path('chapter/list',
         ChapterListView.as_view(),
         name='chapter-list'),
]
