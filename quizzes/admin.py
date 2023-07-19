import nested_admin
from django.contrib import admin
from .models import Answer, Question, Quiz

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer_content', 'is_correct']


admin.site.register(Answer, AnswerAdmin)


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer


class QuestionAdmin(nested_admin.NestedModelAdmin):
    list_display = ['quiz', 'question_content']
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic']


admin.site.register(Quiz, QuizAdmin)
