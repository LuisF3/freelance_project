from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.
def home(request):
    string = "Home<br>Is user logged?: " + str(request.user.is_authenticated)

    if hasattr(request.user, 'empresaprofile'):
        string += f"<br><a href='{reverse('webapp:trabalho:all_works')}'>Trabalhos publicados</a>"
    elif hasattr(request.user, 'estudanteprofile'):
        string += f"<br><a href='{reverse('webapp:trabalho:all_works')}'>Trabalhos disponíveis</a>"

    string += f"<br><a href='{reverse('webapp:login_page')}'>Login</a>" if not request.user.is_authenticated \
        else f"<br>{request.user.username}: <a href='{reverse('webapp:logout_page')}'>Logout</a>"
    return HttpResponse(string)


def register_page(request):
    return render(request, 'newaccount.html', {'url_empresa': reverse('webapp:empresa:register_page'),
                                               'url_estudante': reverse('webapp:estudante:register_page')})


def login_page(request):
    return render(request, 'login.html')


def login_attempt(request):
    if request.method != 'POST':
        raise Http404("Page not found")
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is None:
        return render(request, 'login.html', {'wrong_credentials': True})

    login(request, user)
    return HttpResponseRedirect(reverse('webapp:home_page'))


def logout_page(request):
    logout(request)
    return HttpResponse(f"Logged out<br><a href='{reverse('webapp:home_page')}'>Voltar para a pagina principal</a>")

