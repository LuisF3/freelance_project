from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import EstudanteProfile


# Create your views here.
def register_page(request):
    return render(request, 'pages/student-register-form.html')


def register_attempt(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    universidade = request.POST.get('university')
    curso = request.POST.get('curso')
    previsao_formatura = request.POST.get('formatura', 0)
    password = request.POST.get('password')
    print(username, email, first_name, last_name, universidade, curso, previsao_formatura, password)

    if username is None or email is None or first_name is None or last_name is None \
            or universidade is None or curso is None or password is None:
        raise ValidationError('Algum dos valores é inválido')

    check_username = User.objects.filter(username=username).exists()
    check_email = User.objects.filter(email=email).exists()
    if check_username is True or check_email is True:
        return render(request, "pages/student-register-form.html", {'used_username': check_username,
                                                                    'used_email': check_email})

    new_user = User.objects.create_user(username=username, password=password, email=email,
                                        first_name=first_name, last_name=last_name)
    EstudanteProfile.objects.create(user=new_user, universidade=universidade,
                                    curso=curso, previsao_de_formatura=int(previsao_formatura))
    login(request, new_user)
    return render(request, 'created-account.html', {'home': '/webapp/'})
