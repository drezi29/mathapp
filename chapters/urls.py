from django.urls import path

from .views import ChapterDetailView, ChapterListView

urlpatterns = [
    path('', ChapterListView.as_view(), name='chapter-list'),
    path('chapter/<pk>/', ChapterDetailView.as_view(), name='chapter-detail'),
]
