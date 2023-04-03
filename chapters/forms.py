from django import forms
from .models import Chapter

CLASSES_CHOICES = (
    (1, "Klasa 1"),
    (2, "Klasa 2"),
    (3, "Klasa 3"),
    (4, "Klasa 4"),)

class ChaptersFilterForm(forms.Form):
    classes = forms.MultipleChoiceField(choices=CLASSES_CHOICES, label="Klasy")
    # elementary_level = forms.BooleanField(required=False, label='Poziom podstawowy')
    # extended_level = forms.BooleanField(required=False, label='Pokaż rozdziały z poziomu rozszerzonego')
    
    class Meta:
        model = Chapter

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)