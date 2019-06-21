from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.
def home(request):
    """
    Renderiza o html da mainpage caso o usuário não esteja logado. Do contrário o envia para a página devida
    :param request:
    :return: renderização do html
    """

    if hasattr(request.user, 'empresaprofile'):
        return HttpResponseRedirect(reverse('webapp:empresa:home_page'))
    elif hasattr(request.user, 'estudanteprofile'):
        return HttpResponseRedirect(reverse('webapp:estudante:home_page'))
    return render(request, 'pages/home.html')


def register_page(request):
    """
    rendereiza o a tela de escolher o tipo de cadastro
    :param request:
    :return:
    """

    return render(request, 'pages/newaccount.html', {'url_empresa': reverse('webapp:empresa:register_page'),
                                               'url_estudante': reverse('webapp:estudante:register_page')})


def login_page(request):
    """
    Renderiza a página de login
    :param request:
    :return:
    """
    return render(request, 'pages/login.html')


def login_attempt(request):
    """
    Loga um usuário
    :param request:
    :return:
    """
    if request.method != 'POST':
        raise Http404("Page not found")
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username[0] is not '@':
        username = '@' + username

    user = authenticate(username=username, password=password)

    if user is None:
        return render(request, 'pages/login.html', {'wrong_credentials': True})

    login(request, user)
    return HttpResponseRedirect(reverse('webapp:home_page'))


@login_required
def logout_page(request):
    """
    Desloga um usuário
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect(reverse('webapp:home_page'))


def profile_page(request, username):
    """
    Mostra os dados de um usuário
    :param request:
    :param username: usuario em questão
    :return:
    """
    user = get_object_or_404(User, username=username)
    extends = ''
    if request.user.is_anonymous:
        extends = 'webapp-navbar.html'
    else:
        if hasattr(request.user, 'estudanteprofile'):
            extends = 'student-navbar.html'
        elif hasattr(request.user, 'empresaprofile'):
            extends = 'business-navbar.html'

    return render(request, 'pages/webapp-profile_page.html', {'user': user,
                                                              'extends': extends})
