from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views import generic
import datetime, time

from .models import Expense
from .forms import *

# Create your views here.
def monthExpense(request):
    day=datetime.datetime.today()
    month=day.month
    expenses=Expense.objects.filter(date__month=month)
    context={
    'expenses':expenses,
    'day':day,
    }
    return render(request, 'expenses.html', context)

def newExpense(request):
    form=ExpenseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(monthExpense)
    context={
    'form':form
    }
    return render(request, 'newExpense.html', context)
