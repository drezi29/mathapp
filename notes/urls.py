from django.urls import path
from .views import NoteView

urlpatterns = [
    path('<pk>/', NoteView.as_view(), name='note-detail'),
]

