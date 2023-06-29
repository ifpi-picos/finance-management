from django.http import HttpResponseRedirect
from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect

def delete_category_earnings(request):
    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        category = request.POST.get('delete-category')
        category = CategoryEarnings.objects.get(id=int(category))
        category.delete()

        messages.success(request, 'Categoria de receita deletada com sucesso!')
        return HttpResponseRedirect('/dashboard')

def delete_category_expenses(request):
    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    if request.method == 'POST':
        category = request.POST.get('delete-category')
        category = CategoryExpenses.objects.get(id=int(category))
        category.delete()

        messages.success(request, 'Categoria de despesa deletada com sucesso!')
        return HttpResponseRedirect('/dashboard')
    
def delete_earnings(request, id):
    
    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    earning = Earnings.objects.get(id=int(id))
    earning.delete()

    messages.success(request, 'Receita deletada com sucesso!')
    return HttpResponseRedirect('/extract')

def delete_expenses(request, id):

    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/login')
    
    expense = Expenses.objects.get(id=int(id))
    expense.delete()

    messages.success(request, 'Despesa deletada com sucesso!')
    return HttpResponseRedirect('/extract')