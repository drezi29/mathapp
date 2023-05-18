import nested_admin
from django.contrib import admin
from .models import Answer, Question, Quiz


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer


class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter']


admin.site.register(Quiz, QuizAdmin)
