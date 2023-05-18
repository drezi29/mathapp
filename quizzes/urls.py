from django.urls import path
from .views import QuizView

urlpatterns = [
    path('quiz/<pk>', QuizView.as_view())
]