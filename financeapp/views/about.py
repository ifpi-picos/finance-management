from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

class AboutApp(View):
    template_name = 'financeapp/about.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redireciona o usuário para a página de login
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    


