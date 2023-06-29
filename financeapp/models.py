from django.db import models
from django.contrib.auth.models import User

class CategoryEarnings(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'Categoria dos ganhos'
        verbose_name_plural = u'Categorias dos ganhos'
    
class CategoryExpenses(models.Model):
        
    name = models.CharField(max_length=100, verbose_name='Nome')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'Categoria das despesas'
        verbose_name_plural = u'Categorias das despesas'

class UniqueID(models.Model):
    unique_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.unique_id)

class Earnings(models.Model):

    unique = models.ForeignKey(UniqueID, on_delete=models.CASCADE, verbose_name='ID único')
    description = models.CharField(max_length=100, verbose_name='Descrição')
    value = models.DecimalField(max_digits=50000000000000, decimal_places=2, verbose_name='Valor')
    date = models.DateField(verbose_name='Data')
    recurrence = models.BooleanField(default=False, verbose_name='Recorrência')
    category = models.ForeignKey(CategoryEarnings, on_delete=models.CASCADE, verbose_name='Categoria')
    type = models.CharField(max_length=15, verbose_name='Tipo', default='earning')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = u'Ganho'
        verbose_name_plural = u'Ganhos'
    
class Expenses(models.Model):

    unique = models.ForeignKey(UniqueID, on_delete=models.CASCADE, verbose_name='ID único')
    description = models.CharField(max_length=100, verbose_name='Descrição')
    value = models.DecimalField(max_digits=50000000000000, decimal_places=2, verbose_name='Valor')
    date = models.DateField(verbose_name='Data')
    recurrence = models.BooleanField(default=False, verbose_name='Despesa recorrente')
    category = models.ForeignKey(CategoryExpenses, on_delete=models.CASCADE, verbose_name='Categoria')
    type = models.CharField(max_length=100, verbose_name='Tipo', default='expense')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = u'Despesa'
        verbose_name_plural = u'Despesas'