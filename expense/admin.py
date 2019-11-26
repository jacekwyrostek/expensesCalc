from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display=('category', 'description', 'cost', 'date')
    list_filter=('category', 'description', 'date')
    search_fields=('category', 'description', 'date')
