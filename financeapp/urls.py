from django.urls import path 
from . import views

app_name = 'financeapp'

urlpatterns = [
    path('', views.DashboardApp.as_view(), name='index'),
]