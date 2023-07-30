from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import StartQuizView, render_quiz

urlpatterns = [
    path('start/<pk>', login_required(StartQuizView.as_view()), name='quiz-start'),
    path('quiz/<pk>', render_quiz, name='quiz-detail'),
]