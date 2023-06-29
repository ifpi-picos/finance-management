from django.http import HttpResponseRedirect
from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses
from django.contrib import messages
import decimal
from django.contrib.auth.models import User
from django.shortcuts import redirect

def convert_value(value: str):

    if ',' in value:
        value = value.replace('.', '').replace(',', '.')
    else:
        value = value.replace(',', '')

    value_decimal = decimal.Decimal(value)
    value_decimal = value_decimal.quantize(decimal.Decimal('0.00'))

    return float(value_decimal)

def update_earnings(request, id):
    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        earning = Earnings.objects.get(id=int(id))
        earning.description = request.POST.get('description')
        earning.value = convert_value(request.POST.get('value'))
        earning.date = request.POST.get('date')
        earning.recurrence = int(request.POST.get('recurrent'))
        earning.category = CategoryEarnings.objects.get(
            id=int(request.POST.get('category')
            )
        )
        earning.save()

        messages.success(request, 'Receita atualizada com sucesso!')
        return HttpResponseRedirect('/extract')
    
def update_expenses(request, id):
    
    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        expense = Expenses.objects.get(id=int(id))
        expense.description = request.POST.get('description')
        expense.value = convert_value(request.POST.get('value'))
        expense.date = request.POST.get('date')
        expense.recurrence = int(request.POST.get('recurrent'))
        expense.category = CategoryExpenses.objects.get(
            id=int(request.POST.get('category')
            )
        )
        expense.save()

        messages.success(request, 'Despesa atualizada com sucesso!')
        return HttpResponseRedirect('/extract')
    