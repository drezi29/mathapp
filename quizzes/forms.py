from django import forms
from .models import Answer, Question


class QuizForm(forms.Form):
    def __init__(self, questions, data=None, *args, **kwargs):
        super(QuizForm, self).__init__(data, *args, **kwargs)
        self.questions = questions
        for question in questions:
            field_name = question.pk
            choices = []
            for answer in question.answer_set.all():
                choices.append((answer.pk, answer.answer_content,))
            field = forms.ChoiceField(label=question.question_content, required=True,
                                      choices=choices, widget=forms.RadioSelect)
            self.fields[field_name] = field
