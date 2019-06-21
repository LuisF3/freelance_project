from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.
def home(request):
    string = "Home<br>Is user logged?: " + str(request.user.is_authenticated)

    if hasattr(request.user, 'empresaprofile'):
        return HttpResponseRedirect(reverse('webapp:empresa:home_page'))
    elif hasattr(request.user, 'estudanteprofile'):
        return HttpResponseRedirect(reverse('webapp:estudante:home_page'))

    string += f"<br><a href='{reverse('webapp:login_page')}'>Login</a>" if not request.user.is_authenticated \
        else f"<br>{request.user.username}: <a href='{reverse('webapp:logout_page')}'>Logout</a>"
    return render(request, 'pages/home.html', {})


def register_page(request):
    return render(request, 'pages/newaccount.html', {'url_empresa': reverse('webapp:empresa:register_page'),
                                               'url_estudante': reverse('webapp:estudante:register_page')})


def login_page(request):
    return render(request, 'pages/login.html')


def login_attempt(request):
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
    logout(request)
    return HttpResponseRedirect(reverse('webapp:home_page'))


def profile_page(request, username):
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
                                                              'isStudent': hasattr(user, 'estudanteprofile'),
                                                              'extends': extends})
