from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.http import HttpResponseRedirect
from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses
from django.contrib import messages
import decimal

class DashboardApp(ListView):
    template_name = 'financeapp/dashboard.html'
    model = Earnings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryearnings'] = CategoryEarnings.objects.all()
        context['categoryexpenses'] = CategoryExpenses.objects.all()

        return context

class ExtractApp(ListView):
    template_name = 'financeapp/extract.html'
    model = Earnings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryearnings'] = CategoryEarnings.objects.all()
        context['categoryexpenses'] = CategoryExpenses.objects.all()

        return context

def convert_value(value):

    if ',' in value:
        value = value.replace('.', '').replace(',', '.')
    else:
        value = value.replace(',', '')

    value_decimal = decimal.Decimal(value)
    value_decimal = value_decimal.quantize(decimal.Decimal('0.00'))

    return float(value_decimal)

def create_earnings(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        value = convert_value(request.POST.get('value'))
        date = request.POST.get('date')
        recurrent = request.POST.get('recurrent')
        category = CategoryEarnings.objects.get(
            id=int(request.POST.get('category')
            )
        )

        earning = Earnings(description=description, value=value, date=date, recurrence=int(recurrent), category=category)
        earning.save()

        messages.success(request, 'Receita adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')

def create_expenses(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        value = convert_value(request.POST.get('value'))
        date = request.POST.get('date')
        recurrent = request.POST.get('recurrent')
        category = CategoryExpenses.objects.get(
            id=int(request.POST.get('category')
            )
        )
        
        expense = Expenses(description=description, value=value, date=date, recurrence=int(recurrent), category=category)
        expense.save()

        messages.success(request, 'Despesa adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')
    
def create_category_earnings(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        category = CategoryEarnings(name=description)
        category.save()

        messages.success(request, 'Categoria de receita adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')
    
def create_category_expenses(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        category = CategoryExpenses(name=description)
        category.save()

        messages.success(request, 'Categoria de despesa adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')
    
def delete_category_earnings(request):
    if request.method == 'POST':
        category = request.POST.get('delete-category')
        category = CategoryEarnings.objects.get(id=int(category))
        category.delete()

        messages.success(request, 'Categoria de receita deletada com sucesso!')
        return HttpResponseRedirect('/dashboard')

def delete_category_expenses(request):
    if request.method == 'POST':
        category = request.POST.get('delete-category')
        category = CategoryExpenses.objects.get(id=int(category))
        category.delete()

        messages.success(request, 'Categoria de despesa deletada com sucesso!')
        return HttpResponseRedirect('/dashboard')
    
