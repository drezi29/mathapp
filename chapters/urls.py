from django.urls import path

from .views import ChapterDetailView, ChapterListView

urlpatterns = [
    path("chapters/", ChapterListView.as_view(), name="chapter-list"),
    path("chapters/<pk>/", ChapterDetailView.as_view(), name="chapter-detail"),
]
