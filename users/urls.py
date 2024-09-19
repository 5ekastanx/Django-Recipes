from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import (UserLoginView, logout_view, profile_view, 
                         CreateUserView, UserProfileView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'), # Вход
    path('logout/', logout_view, name='logout'), # Выход
    path('registration/', CreateUserView.as_view(), name='registration'),  # Регистрация
    path("profile/", profile_view, name="profile"), # Профиль пользователя
    path('profile/<int:pk>', login_required(UserProfileView.as_view()), name='edit_profile'),  # Редактировать профиль
]