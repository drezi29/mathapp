from django.urls import path
from .views import ChapterListView, ChapterDetailView, NoteView

urlpatterns = [
    path('', ChapterListView.as_view(), name='chapter-list'),
    path('chapter/<pk>/', ChapterDetailView.as_view(), name='chapter-detail'),
    path('note/<pk>', NoteView.as_view(), name='chapter-note' )
]

