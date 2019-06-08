from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import EmpresaProfile


# Create your views here.
def register_page(request):
    return render(request, 'pages/business-register-form.html')


def register_attempt(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('nome_fantasia')
    last_name = request.POST.get('nome_juridico')
    city = request.POST.get('city')
    area = request.POST.get('area')
    password = request.POST.get('password')

    if username is None or email is None or first_name is None or last_name is None \
            or city is None or area is None or password is None:
        raise ValidationError('Algum dos valores é inválido')

    check_username = User.objects.filter(username=username).exists()
    check_email = User.objects.filter(email=email).exists()
    if check_username is True or check_email is True:
        return render(request, "pages/business-register-form.html", {'used_username': check_username,
                                                                     'used_email': check_email})
    new_user = User.objects.create_user(username=username, password=password, email=email,
                                        first_name=first_name, last_name=last_name)
    EmpresaProfile.objects.create(user=new_user, cidade=city,
                                  area=area)
    login(request, new_user)
    return render(request, 'created-account.html', {'home': '/webapp/'})
