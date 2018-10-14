from django.shortcuts import render


# Create your views here.
def pays_monitor(request):
    '''
        Ф-я обработки запроса страницы с диаграммой и гистограммой платежей
    :param request:
    :return:
    '''

    n = 'Tim'

    return render(request, 'pays/index.html', context={'name': n})