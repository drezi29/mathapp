import nested_admin
from django.contrib import admin
from .models import Answer, Question, Quiz


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    # sortable_field_name = "answer_content"


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline,]
    sortable_field_name = "question_content"


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline,]


admin.site.register(Quiz, QuizAdmin)



