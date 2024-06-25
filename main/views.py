from django.shortcuts import render, redirect

def base_view(request):
    return render(request, 'main/base.html')

def login_view(request):
    if request.method == 'POST':
        # Processar o formulário de cadastro
        pass
    return render(request, 'main/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        # Processar o formulário de cadastro
        pass
    return render(request, 'main/cadastro.html')

def denuncia_view(request):
    if request.method == 'POST':
        # Processar o formulário de cadastro
        pass
    return render(request, 'main/denuncia.html')

def reset_view(request):
    if request.method == 'POST':
        # Processar o formulário de cadastro
        pass
    return render(request, 'main/reset.html')
def external_redirect(request):
    return redirect('https://www.ctbdigital.com.br/')
