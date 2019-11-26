from django.contrib import admin

# Register your models here.
@admin.register(Mass)
class ExpenseAdmin(admin.ModelAdmin):
    list_display=('category', 'description', 'cost', 'date')
    list_filter=('category', 'description', 'date')
    search_fields=('category', 'description', 'date')
