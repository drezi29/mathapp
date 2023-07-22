from django.urls import path
from .views import StartQuizView, QuizView

urlpatterns = [
    path('start/<pk>', StartQuizView.as_view(), name='quiz-start'),
    path('quiz/<pk>', QuizView.as_view(), name='quiz-detail'),
]