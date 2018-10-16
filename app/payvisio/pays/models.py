from django.db import models

# Create your models here.


# class Test(models.Model):
#     title = models.CharField(max_length=150, db_index=True)
#     slug = models.SlugField(max_length=150, unique=True)
#     body =  models.TextField(blank=True, db_index=True)
#     date_pub = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '{}'.format(self.title)

class Payer(models.Model):
    '''
        Модель данных для таблицы 2 - Информация о клиентах
    '''
    payer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, db_index=True)
    country = models.CharField(max_length=50)


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

