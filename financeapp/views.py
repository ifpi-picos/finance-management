from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from financeapp.models import CategoryEarnings, CategoryExpenses, Earnings, Expenses



class DashboardApp(ListView):
    template_name = 'financeapp/dashboard.html'
    model = Earnings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryearnings'] = CategoryEarnings.objects.all()
        context['categoryexpenses'] = CategoryExpenses.objects.all()

        return context

