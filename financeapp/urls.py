from django.views.generic import RedirectView
from django.urls import path 
from . import views

app_name = 'financeapp'

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard'), name='dashboard'),
    path('dashboard', views.DashboardApp.as_view(), name='dashboard'),
    path('extract', views.ExtractApp.as_view(), name='extract'),
    path('createearnings', views.create_earnings, name='createearnings'),
    path('createexpenses', views.create_expenses, name='createexpenses'),
    path('createcategoryearnings', views.create_category_earnings, name='createcategoryearnings'),
    path('createcategoryexpenses', views.create_category_expenses, name='createcategoryexpenses'),
    path('deletecategoryearnings', views.delete_category_earnings, name='deletecategoryearnings'),
    path('deletecategoryexpenses', views.delete_category_expenses, name='deletecategoryexpenses'),
    path('deleteearnings/<int:id>', views.delete_earnings, name='deleteearnings'),
    path('deleteexpenses/<int:id>', views.delete_expenses, name='deleteexpenses'),
]