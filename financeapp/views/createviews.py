from django.http import HttpResponseRedirect
from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses
from django.contrib import messages
import decimal
from django.shortcuts import redirect
from django.contrib.auth.models import User


def convert_value(value: str):

    if ',' in value:
        value = value.replace('.', '').replace(',', '.')
    else:
        value = value.replace(',', '')

    value_decimal = decimal.Decimal(value)
    value_decimal = value_decimal.quantize(decimal.Decimal('0.00'))

    return float(value_decimal)

def create_earnings(request):

    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        description = request.POST.get('description')
        value = convert_value(request.POST.get('value'))
        date = request.POST.get('date')
        recurrent = request.POST.get('recurrent')
        category = CategoryEarnings.objects.get(
            id=int(request.POST.get('category')
            )
        )
        user = request.user


        earning = Earnings(description=description, value=value, date=date, recurrence=int(recurrent), category=category, user=user)
        earning.save()

        messages.success(request, 'Receita adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')

def create_expenses(request):

    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        description = request.POST.get('description')
        value = convert_value(request.POST.get('value'))
        date = request.POST.get('date')
        recurrent = request.POST.get('recurrent')
        category = CategoryExpenses.objects.get(
            id=int(request.POST.get('category')
            )
        )
        user = request.user
        
        expense = Expenses(description=description, value=value, date=date, recurrence=int(recurrent), category=category, user=user)
        expense.save()

        messages.success(request, 'Despesa adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')
    
def create_category_earnings(request):

    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        description = request.POST.get('description')
        category = CategoryEarnings(name=description, user=request.user)
        category.save()

        messages.success(request, 'Categoria de receita adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')
    
def create_category_expenses(request):

    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        description = request.POST.get('description')
        category = CategoryExpenses(name=description, user=request.user)
        category.save()

        messages.success(request, 'Categoria de despesa adicionada com sucesso!')
        return HttpResponseRedirect('/dashboard')