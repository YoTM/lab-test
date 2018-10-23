from django.db import models

# Create your models here.

class Payer(models.Model):
    '''
        Модель данных для таблицы 2 - Информация о клиентах
    '''
    payer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, db_index=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        '''
            Метод переопределяет вывод информации об объекте Payer
            в консоли и админке приложения на строку вида:
            <Имя> <Фамилия> плательщика

        '''
        return '{}'.format(self.first_name+' '+self.last_name)



class Payment(models.Model):
    '''
        Модель данных для таблицы 1 - Информация о проведенных платежах
    '''
    payment_id = models.AutoField(primary_key=True)
    payer_id = models.ForeignKey(
        Payer,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    percent = models.SmallIntegerField()
    pay_date = models.DateTimeField()

    def __str__(self):
        '''
            Метод переопределяет вывод информации об объекте Payment
            в консоли и админке приложения, например:
            Sep. 11, 2018, 11:32 AM

        '''
        return '{}'.format(self.pay_date.strftime("%b. %d, %Y, %I:%M %p"))



