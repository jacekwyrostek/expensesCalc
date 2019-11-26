from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views import generic
import datetime, time

from .models import Expense
from .forms import *

# Create your views here.
def monthExpense(request):
    day=datetime.datetime.today().month
    expenses=Expense.objects.filter(date__month=day)
    context={
    'expenses':expenses,
    }
    return render(request, 'expenses.html', context)
