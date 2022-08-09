from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from loja.models import Cliente

def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Usuario ja existe')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ja existe')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                email=email, first_name=first_name)
                cliente = Cliente.objects.create(usuario=user, nome=first_name, email=email)
                user.save()
                cliente.save()
                messages.info(request, 'Usuario criado com sucesso')
                return redirect('login')


        else:
            messages.info(request, 'Senhas nao conferem')
            return redirect(register)
            

    else:
        return render(request, 'registration/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('loja')
        else:
            messages.info(request, 'Usuario ou senha invalidos')
            return redirect('login_user')



    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('loja')