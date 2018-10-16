from django.shortcuts import render

from .models import Payment, Payer


# Create your views here.
def pays_monitor(request):
    '''
        Ф-я обработки запроса страницы с диаграммой и гистограммой платежей
    :param request:
    :return:
    '''

    payments = Payment.objects.all()
    payers = Payer.objects.all()

    return render(request, 'pays/index.html', context={
        'payments': payments,
        'payers': payers
    })