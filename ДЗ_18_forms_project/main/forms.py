# main/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    Наследуется от стандартной UserCreationForm и добавляет email и проверки.
    """
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        """
        Кастомная валидация: проверяет, что email уникален.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует.")
        return email

    # Пример дополнительной валидации (опционально)
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         raise ValidationError("Пользователь с таким именем уже существует.")
    #     return username


class LoginForm(AuthenticationForm):
    """
    Форма входа (авторизации) пользователя.
    Наследуется от стандартной AuthenticationForm.
    Можно оставить как есть или кастомизировать.
    """
    # В этом случае мы не добавляем ничего нового, используем стандартную форму.
    # Но можно, например, добавить placeholder'ы в виджеты.
    pass


class MessageForm(forms.Form):
    """
    Форма для отправки сообщения.
    """
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Ваш email")
    message = forms.CharField(widget=forms.Textarea, max_length=500, label="Сообщение")

    def clean_message(self):
        """
        Кастомная валидация: проверяет, что сообщение не пустое и не длиннее 500 символов.
        (Проверка max_length происходит автоматически, но можно добавить свою логику)
        """
        message = self.cleaned_data.get('message')
        if message and len(message.strip()) == 0:
            raise ValidationError("Сообщение не может быть пустым.")
        return message