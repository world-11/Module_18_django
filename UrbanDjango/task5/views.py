from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.


def sign_up_by_html(request):
    users = ['Анатолий', 'Юрий', 'Александр', 'Алексей', 'Олег', 'Дмитрий']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_ = request.POST.get('password_')
        age = request.POST.get('age')
        if password != password_:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', info)
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            return render(request, 'registration_page.html', info)
        if username in users:
            info['error'] = f'Пользователь {username} уже существует!'
            return render(request, 'registration_page.html', info)
        info['welcome'] = f'Приветствуем, {username}'

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users = ['Анатолий', 'Юрий', 'Александр', 'Алексей', 'Олег', 'Дмитрий']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_ = form.cleaned_data['password_']
            age = form.cleaned_data['age']
        if password != password_:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', info)
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            return render(request, 'registration_page.html', info)
        if username in users:
            info['error'] = f'Пользователь {username} уже существует!'
            return render(request, 'registration_page.html', info)
        info['welcome'] = f'Приветствуем, {username}'
        info['form'] = form

    return render(request, 'registration_page.html', info)
