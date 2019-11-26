#from django.forms import ModelForm
from .models import Expense
from flatpickr import DatePickerInput
from django import forms
from django.forms import ModelForm
from expense.choices import *

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields=['category', 'description', 'date']
        widgets = {
            'date': DatePickerInput(),
        }
