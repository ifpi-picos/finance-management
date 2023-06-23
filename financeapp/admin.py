from django.contrib import admin
from .models import CategoryEarnings, CategoryExpenses, Earnings, Expenses

admin.site.register(CategoryEarnings)
admin.site.register(CategoryExpenses)
admin.site.register(Earnings)
admin.site.register(Expenses)
