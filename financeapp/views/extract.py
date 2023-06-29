from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView


class ExtractApp(ListView):
    template_name = 'financeapp/extract.html'
    model = Earnings
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redireciona o usuário para a página de login
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id

        context['categoryearnings'] = CategoryEarnings.objects.filter(user_id=user_id)
        context['categoryexpenses'] = CategoryExpenses.objects.filter(user_id=user_id)
        context['username'] = self.request.user.first_name + ' ' + self.request.user.last_name
        
        earnings = Earnings.objects.filter(user_id=user_id)
        expenses = Expenses.objects.filter(user_id=user_id)

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

        context['earnings'] = earnings.order_by('-date')
        context['expenses'] = expenses.order_by('-date')

        return context