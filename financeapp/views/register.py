from django.contrib.auth.models import User
from django.shortcuts import redirect, render
# >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# # Neste ponto, user é um objeto User que já foi salvo no banco de dados.
# # Você pode continuar a mudar seus atributos se você quiser mudar outros
# # campos.
# >>> user.is_staff = True
# >>> user.save()

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('/login')
    else:
        return render(request, 'financeapp/register.html')