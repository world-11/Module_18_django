from django.shortcuts import render

# Create your views here.
def cart(request):
    title = 'Корзина'
    text8 = 'Извините, ваша корзина пуста'
    text9 = 'Вернулься обратно'
    adr1 = '/platform'
    context = {
        'title': title,
        'text8': text8,
        'text9': text9,
        'adr1': adr1
    }
    return render(request, 'cart.html', context)

def games(request):
    title = 'Магазин игр'
    text0 = 'Игры:'
    text1 = 'PUBG: BUTTLEGROUND'
    text2 = 'Cyberpunk 2077'
    text3 = 'Red Dead Redeption 2'
    text4 = 'Купить'
    text5 = 'Вернуться обратно'
    adr1 = '/platform'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4,
        'text5': text5,
        'adr1': adr1
    }
    return render(request, 'games.html', context)

def platform(request):
    title = 'Видеоигры'
    text0 = 'Обзор популярных видеоигр'
    text1 = 'На главную'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {
        'title': title,
        'text0': text0,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'platform.html', context)