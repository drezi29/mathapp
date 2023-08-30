from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(label='Nazwa użytkownika', min_length=3, max_length=50)
    email = forms.EmailField(label='Adres e-mail')
    password1 = forms.CharField(label='Podaj hasło', widget=forms.PasswordInput, help_text=('Hasło musi zawierać przynajmniej 8 znaków, w tym litery, cyfry i znaki specjalne'))
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        users_number = User.objects.filter(email=email).count()
        if users_number > 0:
            raise ValidationError('Użytkownik o tym adresie mailowym został już zarejestrowany.')
        return email

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
