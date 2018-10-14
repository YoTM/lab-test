from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pays_monitor(request):
    '''
        Ф-я обработки запроса страницы с диаграммой и гистограммой платежей
    :param request:
    :return:
    '''
    return HttpResponse('<h1>Здесь будет главная страница приложения</h1>')