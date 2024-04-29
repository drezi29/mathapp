import nested_admin
from django.contrib import admin
from .models import Exercise, Step


class StepAdmin(admin.ModelAdmin):
    list_display = ['exercise', 'title', 'instruction', 'order']


admin.site.register(Step, StepAdmin)


class StepInline(nested_admin.NestedStackedInline):
    model = Step
    sortable_field_name = "title"


class ExerciseAdmin(nested_admin.NestedModelAdmin):
    inlines = [StepInline]


admin.site.register(Exercise, ExerciseAdmin)
