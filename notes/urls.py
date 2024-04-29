from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import NoteView

urlpatterns = [
    path('<pk>/', login_required(NoteView.as_view()), name='note-detail'),
]

