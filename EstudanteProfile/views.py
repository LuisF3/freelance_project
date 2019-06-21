from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from Trabalhos.models import Trabalho
from .models import EstudanteProfile


@login_required
def home_page(request):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

    user = request.user
    user_data = {'user': user, 'proposals': Trabalho.objects.filter(private=False),
                 'work_detail': reverse('webapp:estudante:home_page')}
    return render(request, 'pages/student-mainpage.html', user_data)


@login_required
def work_detail(request, work_pk):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

    trabalho = Trabalho.objects.get(pk=work_pk)
    user_data = {'trabalho': trabalho,
                 'current_page': reverse('webapp:estudante:work_detail', kwargs={'work_pk': work_pk})}

    return render(request, 'pages/student-work-detail.html', user_data)


@login_required
def subscribed_works(request):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

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

    if username and username[0] != '@':
        username = '@' + username

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


@login_required
def subscribe(request, work_pk):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

    trabalho = Trabalho.objects.get(pk=work_pk)
    trabalho.inscritos.add(request.user.estudanteprofile)
    return HttpResponseRedirect(reverse('webapp:estudante:work_detail', kwargs={'work_pk': work_pk}))


@login_required
def unsubscribe(request, work_pk):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

    trabalho = Trabalho.objects.get(pk=work_pk)
    trabalho.inscritos.remove(request.user.estudanteprofile)
    trabalho.contratados.remove(request.user.estudanteprofile)
    return HttpResponseRedirect(reverse('webapp:estudante:work_detail', kwargs={'work_pk': work_pk}))


@login_required
def account_information(request):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

    return render(request, 'pages/student-account-information.html', {'user': request.user})


@login_required
def account_information_update(request):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

    user = request.user

    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.estudanteprofile.universidade = request.POST.get('universidade')
    user.estudanteprofile.curso = request.POST.get('curso')
    user.estudanteprofile.descricao = request.POST.get('descricao')

    if request.FILES.get('profile_pic') is not None:
        user.estudanteprofile.profile_pic.save(name=user.username + '_pic', content=request.FILES.get('profile_pic'))

    user.save()
    user.estudanteprofile.save()

    return render(request, 'pages/student-account-information.html', {'successfully_modified': True})


@login_required
def search_works(request):
    if not hasattr(request.user, 'estudanteprofile'):
        raise Http404

    key = request.GET.get('key')
    user = request.user
    user_data = {'user': user, 'proposals': Trabalho.objects.filter(private=False, titulo__icontains=key),
                 'work_detail': reverse('webapp:estudante:home_page')}

    return render(request, 'pages/student-mainpage.html', user_data)
