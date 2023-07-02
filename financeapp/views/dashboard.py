from django.views.generic import ListView
from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses
import decimal
from datetime import datetime
import json
from django.db.models import Sum
from django.db.models import QuerySet
from django.shortcuts import redirect

def get_sums_data_and_labels(earnings: QuerySet, expenses: QuerySet, start_date: str, end_date: str):
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

    return (
        json.dumps(labels),
        json.dumps(earnings_sum),
        json.dumps(expenses_sum)
    )

def get_data_based_on_category(user_id, earnings: QuerySet, expenses: QuerySet, start_date: str, end_date: str, filters_category_earnings: list, filters_category_expenses: list):
    
    # Verificando a necessidade de filtrar por categoria
    if not filters_category_earnings and not filters_category_expenses:
        categoryEarnings = list(CategoryEarnings.objects.values_list('name', flat=True).filter(user_id=user_id))
        categoryExpenses = list(CategoryExpenses.objects.values_list('name', flat=True).filter(user_id=user_id))
    else:
        if filters_category_earnings and filters_category_expenses:
            categoryEarnings = list(CategoryEarnings.objects.filter(id__in=filters_category_earnings, user_id=user_id).values_list('name', flat=True))
            categoryExpenses = list(CategoryExpenses.objects.filter(id__in=filters_category_expenses, user_id=user_id).values_list('name', flat=True))
        elif filters_category_earnings:
            categoryEarnings = list(CategoryEarnings.objects.filter(id__in=filters_category_earnings, user_id=user_id).values_list('name', flat=True))
            categoryExpenses = list(CategoryExpenses.objects.values_list('name', flat=True).filter(user_id=user_id))
        elif filters_category_expenses:
            categoryEarnings = list(CategoryEarnings.objects.values_list('name', flat=True).filter(user_id=user_id))
            categoryExpenses = list(CategoryExpenses.objects.filter(id__in=filters_category_expenses, user_id=user_id).values_list('name', flat=True))

    dataEarning = []
    dataExpenses = []

    for category in categoryEarnings:
        category_sum = earnings.filter(category__name=category, date__range=[start_date, end_date]).aggregate(total=Sum('value'))['total'] or 0
        dataEarning.append(int(category_sum))

    for category in categoryExpenses:
        category_sum = expenses.filter(category__name=category, date__range=[start_date, end_date]).aggregate(total=Sum('value'))['total'] or 0
        dataExpenses.append(int(category_sum))
    
    return (
            json.dumps(categoryExpenses), 
            json.dumps(categoryEarnings), 
            json.dumps(dataEarning), 
            json.dumps(dataExpenses)
        )

class DashboardApp(ListView):
    template_name = 'financeapp/dashboard.html'
    model = Earnings

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redireciona o usuário para a página de login
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pegando os dados do usuário
        user_start_date = self.request.GET.get('start_date')
        user_end_date = self.request.GET.get('end_date')
        filters_category_earnings = self.request.GET.getlist('categoryEarnings')
        filters_category_expenses = self.request.GET.getlist('categoryExpenses')
        user_id = self.request.user.id

        # Pegando a data de início e fim do ano atual, caso não seja passado pelo usuário
        if user_start_date or user_end_date:
            start_date = user_start_date 
            end_date = user_end_date
        else:
            start_date = datetime.strftime(datetime(datetime.now().year, 1, 1).date(), '%Y-%m-%d')
            end_date = datetime.now().date().strftime('%Y-%m-%d')
        
        # Dados dos ganhos e gastos referente ao período e os filtros
        if self.request.method == 'GET':
            if filters_category_earnings:
                earnings = Earnings.objects.filter(date__range=[start_date, end_date], user_id=user_id, category__id__in=filters_category_earnings)
            else:
                earnings = Earnings.objects.filter(date__range=[start_date, end_date], user_id=user_id)
            if filters_category_expenses:
                expenses = Expenses.objects.filter(date__range=[start_date, end_date], user_id=user_id, category__id__in=filters_category_expenses)
            else:
                expenses = Expenses.objects.filter(date__range=[start_date, end_date], user_id=user_id)

        # Pegando os dados dos ganhos e gastos referente ao período e os labels
        labels, earnings_sum, expenses_sum = get_sums_data_and_labels(earnings, expenses, start_date, end_date)   
        
        # Dados para o gráfico de pizza
        categoryExpenses, categoryEarnings, data_earnings_category, data_expenses_category = get_data_based_on_category(
            user_id,
            earnings, 
            expenses, 
            start_date, 
            end_date,
            filters_category_earnings,
            filters_category_expenses
        )

        # Dados dos gráficos
        context['labels'] = labels
        context['earnings_list'] = earnings_sum
        context['expenses_list'] = expenses_sum
        context['category_earnings'] = categoryEarnings
        context['category_expenses'] = categoryExpenses
        context['data_earnings_category'] = data_earnings_category
        context['data_expenses_category'] = data_expenses_category

        # Dados para o template
        context['categoryearnings'] = CategoryEarnings.objects.filter(user_id=user_id)
        context['categoryexpenses'] = CategoryExpenses.objects.filter(user_id=user_id)
        context['sum_earnings'] = decimal.Decimal(earnings.aggregate(total=Sum('value'))['total'] or 0).quantize(decimal.Decimal('0.00'))
        context['sum_expenses'] = decimal.Decimal(expenses.aggregate(total=Sum('value'))['total'] or 0).quantize(decimal.Decimal('0.00'))
        context['balance'] = (context['sum_earnings'] - context['sum_expenses']).quantize(decimal.Decimal('0.00'))
        context['username'] = f'{self.request.user.first_name} {self.request.user.last_name}'
        context['start_date'] = start_date
        context['end_date'] = end_date
        context['earnings_and_expenses'] = earnings.union(expenses).order_by('-unique_id')

        return context