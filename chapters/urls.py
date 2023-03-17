from django.urls import path
from .models import Chapter
from .views import ChapterListView, ChapterDetailView

urlpatterns = [
    path('', ChapterListView.as_view(), name='chapter-list'),
    path('chapter/<pk>/', ChapterDetailView.as_view(), name='chapter-detail')
]
