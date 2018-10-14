from django.shortcuts import render

from .models import Test


# Create your views here.
def pays_monitor(request):
    '''
        Ф-я обработки запроса страницы с диаграммой и гистограммой платежей
    :param request:
    :return:
    '''

    tests = Test.objects.all()

    return render(request, 'pays/index.html', context={'tests': tests})