from django.urls import path
from . import views

urlpatterns = [
    # path() для страницы регистрации нового пользователя
    # её полный адрес будет auth/signup/, но префикс auth/ обрабатывется в головном urls.py
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("ticket/", views.user_contact, name='ticket'),
    path("/new", views.new_post, name="new_post"),
]