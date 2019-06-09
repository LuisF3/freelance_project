from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Trabalhos.models import Trabalho
from .models import EstudanteProfile


def home_page(request):
    user = request.user
    user_data = {'user': user,'proposals': Trabalho.objects.all(),
                 'work_detail': reverse('webapp:estudante:home_page')}

    return render(request, 'pages/student-mainpage.html', user_data)


def work_detail(request, work_pk):
    trabalho = Trabalho.objects.get(pk=work_pk)
    user_data = {'trabalho': trabalho,
                 'current_page': reverse('webapp:estudante:work_detail', kwargs={'work_pk': work_pk})}

    return render(request, 'pages/student-work-detail.html', user_data)


def subscribed_works(request):
    user = request.user
    subscribed_works = [work for work in user.estudanteprofile.subscribers.all()]
    subscribed_works += [work for work in user.estudanteprofile.contratados.all()]

    user_data = {'user': user, 'proposals': subscribed_works,
                 'work_detail': reverse('webapp:estudante:home_page')}

    return render(request, 'pages/student-mainpage.html', user_data)


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
    return render(request, 'created-account.html')


def subscribe(request, work_pk):
    trabalho = Trabalho.objects.get(pk=work_pk)
    trabalho.inscritos.add(request.user.estudanteprofile)
    return HttpResponseRedirect(reverse('webapp:estudante:work_detail', kwargs={'work_pk': work_pk}))


def unsubscribe(request, work_pk):
    trabalho = Trabalho.objects.get(pk=work_pk)
    trabalho.inscritos.remove(request.user.estudanteprofile)
    trabalho.contratados.remove(request.user.estudanteprofile)
    return HttpResponseRedirect(reverse('webapp:estudante:work_detail', kwargs={'work_pk': work_pk}))
