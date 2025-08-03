# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('message/', views.message_view, name='message'),
    # path('', views.home_view, name='home'), # Добавим позже, если будет главная страница
]