from django.db import models
from expense.choices import *

# Create your models here.
class Expense(models.Model):
    category=models.CharField(verbose_name=u"Data:", choices=cat, default=0, max_length=50)
    description=models.CharField(verbose_name=u'Description:', max_length=50)
    cost=models.DecimalField(verbose_name=u'Cost:', max_digits=5, decimal_places=2)
    date=models.DateField(verbose_name=u"Date:")
