#  импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

#  функция reverse_lazy позволяет получить URL по параметру "name" функции path()
#  берём, тоже пригодится
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

#  импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm, ContactForm, PostForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    # где login — это параметр "name" в path()
    template_name = "signup.html"


def user_contact(request):
    # проверим, пришёл ли к нам POST-запрос или какой-то другой:
    if request.method == 'POST':
        # создаём объект формы класса ContactForm и передаём в него полученные данные
        form = ContactForm(request.POST)

        # если все данные формы валидны - работаем с "очищенными данными" формы
        if form.is_valid():
            # берём валидированные данные формы из словаря form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['body']
            # при необходимости обрабатываем данные
            # ...
            # сохраняем объект в базу
            form.save()

            # Функция redirect перенаправляет пользователя
            # на другую страницу сайта, чтобы защититься
            # от повторного заполнения формы
            return redirect('/')

        # если условие if form.is_valid() ложно и данные не прошли валидацию -
        # передадим полученный объект в шаблон
        # чтобы показать пользователю информацию об ошибке

        # заодно заполним прошедшими валидацию данными все поля,
        # чтобы не заставлять пользователя вносить их повторно
        return render(request, 'contact.html', {'form': form})

    # если пришёл не POST-запрос - создаём и передаём в шаблон пустую форму
    # пусть пользователь напишет что-нибудь
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['group']
            text = form.cleaned_data['text']
            form.save()
            return redirect('')
        return render(request, 'newpost.html', {'form': form})
    form = PostForm()
    return render(request, 'newpost.html', {'form': form})
