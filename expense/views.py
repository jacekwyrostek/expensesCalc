from django.shortcuts import render

# Create your views here.
def monthExpense(request):
    day=datetime.datetime.today().isocalendar()[1]
    expenses=Expense.objects.filter(day__month=day)
    context={
    expenses
    }
    return render(request, 'expenses.html', context)
