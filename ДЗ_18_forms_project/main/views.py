# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, MessageForm
from .models import Profile


def register_view(request):
    """Представление для страницы регистрации."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            # messages.success(request, 'Регистрация прошла успешно!')
            # Вместо сообщения, можно сразу залогинить пользователя и перенаправить
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}! Вы успешно зарегистрировались.')
                return redirect('profile')  # Перенаправляем на страницу профиля
            else:
                # На случай, если authenticate по каким-то причинам не сработал
                messages.info(request, 'Пожалуйста, войдите в систему.')
                return redirect('login')
        # Если форма не валидна, она автоматически отрендерится с ошибками
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    """Представление для страницы входа."""
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Вы вошли в систему как {username}.")
                # Попытка получить 'next' параметр из URL
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('profile')  # Или 'home', если будет главная страница
            else:
                # authenticate не сработал, но форма валидна - странно, но возможно
                messages.error(request, "Неверное имя пользователя или пароль.")
        # Если форма не валидна, она автоматически отрендерится с ошибками
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    """Представление для выхода из системы."""
    logout(request)
    messages.info(request, "Вы вышли из системы.")
    return redirect('login')  # Или 'home'


@login_required
def profile_view(request):
    """Представление для страницы профиля пользователя."""
    # request.user.profile создается автоматически сигналами
    # Но на всякий случай, можно получить или создать
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    # Здесь можно добавить логику для отображения сообщений пользователя и т.д.
    context = {
        'profile': profile,
        # 'user_messages': ... # Добавим позже, когда будет модель сообщений
    }
    return render(request, 'main/profile.html', context)


def message_view(request):
    """Представление для страницы отправки сообщения."""
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Здесь должна быть логика обработки сообщения
            # Например, сохранение в БД или отправка email
            # Пока просто покажем сообщение об успехе
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message']
            # print(f"Получено сообщение от {name} ({email}): {message_text}") # Для отладки
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            # Очищаем форму после успешной отправки
            form = MessageForm()  # Создаем новую пустую форму
            # return redirect('message') # Или оставляем на той же странице
        # Если форма не валидна, она автоматически отрендерится с ошибками
    else:
        form = MessageForm()
    return render(request, 'main/message.html', {'form': form})


from django.shortcuts import render


