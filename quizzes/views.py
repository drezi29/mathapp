# from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from .models import Answer
from chapters.models import Topic
from .models import Quiz



class QuizView(View):
    def get(self, request, pk):
        topic = Topic.objects.get(id=pk)
        quiz = Quiz.objects.get(topic=pk)
        question_list = quiz.question_set.all()
        ids = [question.id for question in question_list ]
        answers = Answer.objects.filter(question__id__in=ids)
        return render(request, 'quizzes/quiz.html',
                      {"topic": topic,
                       "question_list": question_list,
                       "answers": answers})
