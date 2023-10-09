from django.urls import path

from .views import ExerciseDetailView, ExercisesListView

urlpatterns = [
    path('exercises/', ExercisesListView.as_view(), name='exercises-list'),
    path(
        'exercises/detail/<pk>/', ExerciseDetailView.as_view(), name='exercise-detail'
    ),
]
