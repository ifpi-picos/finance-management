from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.http import HttpResponseRedirect
from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses
from django.contrib import messages
from django.db.models import Q
import decimal
from datetime import datetime
import json
from django.db.models import Sum
from django.db.models import QuerySet

class DashboardApp(ListView):
    template_name = 'financeapp/dashboard.html'
    model = Earnings

    def get_sums_data_and_labels(self, earnings: QuerySet, expenses: QuerySet, start_date: str, end_date: str):
        # Passanso a data de string para datetime e pegando a quantidade de meses
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        
        # Mapeamento dos nomes dos meses em português
        month_names = {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
            6: 'Junho',
            7: 'Julho',
            8: 'Agosto',
            9: 'Setembro',
            10: 'Outubro',
            11: 'Novembro',
            12: 'Dezembro'
        }
        # Pegando os dados dos ganhos e gastos referente ao período e os labels
        labels = []
        earnings_sum = []
        expenses_sum = []

        for i in range(months + 1):
            month = (start_date.month + i) % 12
            if month == 0:
                month = 12
            month_name = month_names[month]
            labels.append(month_name)

            earnings_month_sum = earnings.filter(date__month=month).aggregate(total=Sum('value'))['total'] or 0
            earnings_sum.append(int(earnings_month_sum))

            expenses_month_sum = expenses.filter(date__month=month).aggregate(total=Sum('value'))['total'] or 0
            expenses_sum.append(int(expenses_month_sum))

        return labels, earnings_sum, expenses_sum

    def get_context_data(self, **kwargs):
        # Feito e comentado por: Jean Carlos
        context = super().get_context_data(**kwargs)
        context['categoryearnings'] = CategoryEarnings.objects.all()
        context['categoryexpenses'] = CategoryExpenses.objects.all()

        # Pegando a data de início e fim passada pelo usuário
        user_start_date = self.request.GET.get('start_date')
        user_end_date = self.request.GET.get('end_date')

        # Pegando a data de início e fim do ano atual, caso não seja passado pelo usuário
        if user_start_date or user_end_date:
            start_date = user_start_date 
            end_date = user_end_date
        else:
            start_date = datetime.strftime(datetime(datetime.now().year, 1, 1).date(), '%Y-%m-%d')
            end_date = datetime.now().date().strftime('%Y-%m-%d')
        
        # Passando a data para o template
        context['start_date'] = start_date
        context['end_date'] = end_date

        # Dados dos ganhos e gastos referente ao período
        earnings = Earnings.objects.filter(date__range=[start_date, end_date])
        expenses = Expenses.objects.filter(date__range=[start_date, end_date])

        # Pegando os dados dos ganhos e gastos referente ao período e os labels
        labels, earnings_sum, expenses_sum = self.get_sums_data_and_labels(earnings, expenses, start_date, end_date)   

        # Passando os dados para json, para serem usados no gráfico
        labels = json.dumps(labels)
        earnings_sum = json.dumps(earnings_sum)
        expenses_sum = json.dumps(expenses_sum)
        
        # Passando os dados para o template
        context['labels'] = labels
        context['earnings_list'] = earnings_sum
        context['expenses_list'] = expenses_sum

        decimal_sum_earning = decimal.Decimal(earnings.aggregate(total=Sum('value'))['total'] or 0)
        context['sum_earnings'] = decimal_sum_earning.quantize(decimal.Decimal('0.00'))
        decimal_sum_expenses = decimal.Decimal(expenses.aggregate(total=Sum('value'))['total'] or 0)
        context['sum_expenses'] = decimal_sum_expenses.quantize(decimal.Decimal('0.00'))
        context['balance'] = (decimal_sum_earning - decimal_sum_expenses).quantize(decimal.Decimal('0.00'))
        
        # Dados para o gráfico de pizza
        context['doughnut_data'] = [int(context['sum_earnings']), int(context['sum_expenses'])]

        # Dados para o gráfico de rosca
        context['doughnut_data'] = [int(context['sum_earnings']), int(context['sum_expenses'])]

        return context

class ExtractApp(ListView):
    template_name = 'financeapp/extract.html'
    model = Earnings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryearnings'] = CategoryEarnings.objects.all()
        context['categoryexpenses'] = CategoryExpenses.objects.all()
        earnings = Earnings.objects.all()
        expenses = Expenses.objects.all()

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        search_box = self.request.GET.get('search')

        if search_box:
            earnings = earnings.filter(
                Q(description__icontains=search_box) | Q(value__icontains=search_box) | Q(date__icontains=search_box)
            )
            expenses = expenses.filter(
                Q(description__icontains=search_box) | Q(value__icontains=search_box) | Q(date__icontains=search_box)
            )
        
        elif start_date or end_date:
            context['start_date'] = start_date
            context['end_date'] = end_date

            if start_date and end_date:
                earnings = earnings.filter(date__range=[start_date, end_date])
                expenses = expenses.filter(date__range=[start_date, end_date])
            elif start_date:
                earnings = earnings.filter(date__gte=start_date)
                expenses = expenses.filter(date__gte=start_date)
            elif end_date:
                earnings = earnings.filter(date__lte=end_date)
                expenses = expenses.filter(date__lte=end_date)

        context['earnings'] = earnings
        context['expenses'] = expenses

        return context

def convert_value(value: str):

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
    
def delete_earnings(request, id):
    earning = Earnings.objects.get(id=int(id))
    earning.delete()

    messages.success(request, 'Receita deletada com sucesso!')
    return HttpResponseRedirect('/extract')

def delete_expenses(request, id):
    expense = Expenses.objects.get(id=int(id))
    expense.delete()

    messages.success(request, 'Despesa deletada com sucesso!')
    return HttpResponseRedirect('/extract')

def update_earnings(request, id):
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
    