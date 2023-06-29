from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')  # Redireciona para a página inicial após o login
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render(request, 'financeapp/login.html', {'error_message': error_message})
    return render(request, 'financeapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login') 