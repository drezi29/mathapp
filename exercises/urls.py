from django.urls import path
from .views import ExerciseListView,exercise_view

urlpatterns = [
    path('<pk>/', ExerciseListView.as_view(), name='exercises-list'),
    path('detail/<pk>', exercise_view, name='exercise-detail'),
]

