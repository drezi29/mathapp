from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
from .forms import QuizForm
from .models import Answer, Quiz
from chapters.models import Topic
from formulas.models import Title, FormulaNote


@login_required
def quiz_result(request):
    score = request.session['score']
    questions_amount = request.session['questions_amount']
    incorrect_responses = request.session['incorrect_responses']
    return render(request, 'quizzes/results.html', {'score': score, 'questions_amount': questions_amount, 'incorrect_responses': incorrect_responses.items()})


@login_required
def render_quiz(request, pk):
    topic = Topic.objects.get(id=pk)
    quiz = Quiz.objects.get(topic=pk)
    formula_chapters = Title.objects.all()
    form = QuizForm(questions=quiz.question_set.all())
    if request.method == 'POST':
        post_data = request.POST
        score_counter = 0
        incorrect_responses = {}
        for question in quiz.question_set.all():
            answers = question.answer_set.all()
            answered_correctly = False
            answer_content = ''
            for answer in answers:
                answered_correctly = False
                if answer.is_correct:
                    answer_content = answer.answer_content
                    if answer.id == int(post_data[str(question.id)]):
                        score_counter += 1
                        answered_correctly = True
                        break
            if not answered_correctly:
                incorrect_responses[question.question_content] = answer_content
        request.session['score'] = score_counter
        request.session['questions_amount'] = len(quiz.question_set.all())
        request.session['incorrect_responses'] = incorrect_responses
        return redirect('/quiz/result')
    return render(request, 'quizzes/quiz.html', {'topic': topic, 'form': form, 'formula_chapters': formula_chapters})


class StartQuizView(View):
    def get(self, request, pk):
        topic = Topic.objects.get(id=pk)
        quiz = Quiz.objects.get(topic=pk)
        question_list = quiz.question_set.all()
        return render(request, 'quizzes/quizstartpage.html', {'topic': topic, 'questions': len(question_list)})
