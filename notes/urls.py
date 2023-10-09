from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import NoteDetailView

urlpatterns = [
    path(
        'notes/<int:slug>', login_required(NoteDetailView.as_view()), name='note-detail'
    ),
]
