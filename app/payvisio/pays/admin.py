from django.contrib import admin

# Register your models here.
from .models import Payment, Payer

admin.site.register(Payment)

admin.site.register(Payer)