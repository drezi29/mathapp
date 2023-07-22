from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
from .forms import QuizForm
from chapters.models import Topic
from .models import Answer
from .models import Quiz


def quiz_result(request):
    score = request.session['score']
    questions_amount = request.session['questions_amount']
    return render(request, 'quizzes/results.html', {'score': score, 'questions_amount': questions_amount})


def render_quiz(request, pk):
    topic = Topic.objects.get(id=pk)
    quiz = Quiz.objects.get(topic=pk)
    form = QuizForm(questions=quiz.question_set.all())
    if request.method == 'POST':
        post_data = request.POST
        score_counter = 0
        for question in quiz.question_set.all():
            answers = question.answer_set.all()
            for answer in answers:
                if answer.id == int(post_data[str(question.id)]) and answer.is_correct:
                    score_counter += 1
        request.session['score'] = score_counter
        request.session['questions_amount'] = len(quiz.question_set.all())
        return redirect('/quiz/result')
    return render(request, 'quizzes/quiz.html', {'topic': topic, 'form': form})


class StartQuizView(View):
    def get(self, request, pk):
        topic = Topic.objects.get(id=pk)
        quiz = Quiz.objects.get(topic=pk)
        question_list = quiz.question_set.all()
        return render(request, 'quizzes/quizstartpage.html', {'topic': topic, 'questions': len(question_list)})
