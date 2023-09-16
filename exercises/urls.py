from django.urls import path

from .views import ExerciseListView, ExerciseView

urlpatterns = [
    path('<pk>/', ExerciseListView.as_view(), name='exercises-list'),
    path('detail/<pk>', ExerciseView.as_view(), name='exercise-detail'),
]
