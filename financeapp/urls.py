from django.views.generic import RedirectView
from django.urls import path 
from . import views

app_name = 'financeapp'

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard'), name='dashboard'),
    path('dashboard', views.DashboardApp.as_view(), name='dashboard'),
    path('extract', views.ExtractApp.as_view(), name='extract'),
]