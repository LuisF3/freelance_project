import magic
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from Trabalhos.models import Trabalho
from .models import EmpresaProfile


@login_required
def home_page(request):
    """
    Renderiza o html da mainpage
    :param request:
    :return: renderização do html
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    user = request.user
    user_data = {'user': user, 'add_work_link': reverse('webapp:empresa:add_work'),
                 'proposals': user.empresaprofile.trabalho.all(),
                 'work_detail': reverse('webapp:empresa:home_page')}

    return render(request, 'pages/business-mainpage.html', user_data)


def register_page(request):
    """
    rendereiza o form de cadastro
    :param request:
    :return:
    """

    return render(request, 'pages/business-register-form.html')


def register_attempt(request):
    """
    Tenta criar uma nova empresa
    :param request:
    :return: página de criado com sucesso ou erro de validação ou erro de usuário já existente
    """

    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('nome_fantasia')
    last_name = request.POST.get('nome_juridico')
    cidade = request.POST.get('cidade')
    area = request.POST.get('area')
    password = request.POST.get('password')

    if username and username[0] != '@':
        username = '@' + username

    if username is None or email is None or first_name is None or last_name is None \
            or cidade is None or area is None or password is None:
        raise ValidationError('Algum dos valores é inválido')

    check_username = User.objects.filter(username=username).exists()
    check_email = User.objects.filter(email=email).exists()
    if check_username is True or check_email is True:
        return render(request, "pages/business-register-form.html", {'used_username': check_username,
                                                                     'used_email': check_email})
    new_user = User.objects.create_user(username=username, password=password, email=email,
                                        first_name=first_name, last_name=last_name)
    EmpresaProfile.objects.create(user=new_user, cidade=cidade,
                                  area=area)
    login(request, new_user)
    return render(request, 'created-account.html')


@login_required
def add_work(request):
    """
    Cria um trabalho
    :param request:
    :return: Retorna para a pagina inicial
    """
    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    titulo = request.POST.get('titulo')
    inicio = request.POST.get('inicio')
    fim = request.POST.get('fim')
    pagamento = request.POST.get('pagamento')
    descricao = request.POST.get('descricao')
    requisitos = request.POST.get('requisitos')

    if titulo is None or inicio is None or fim is None or pagamento is None or descricao is None or requisitos is None:
        raise ValidationError('Algum dos valores é inválido')

    Trabalho.objects.create(business=request.user.empresaprofile, titulo=titulo,
                            inicio=inicio, fim=fim, pagamento=pagamento,
                            descricao=descricao, requisitos=requisitos)

    return HttpResponseRedirect(reverse('webapp:home_page'))


@login_required
def work_detail(request, work_pk):
    """
    Renderiza a página de detalhe de um trabalho
    :param request:
    :param work_pk: trabalho em questão
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    trabalho = request.user.empresaprofile.trabalho.get(pk=work_pk)
    user_data = {'trabalho': trabalho,
                 'current_page': reverse('webapp:empresa:work_detail', kwargs={'work_pk': work_pk})}

    return render(request, 'pages/business-work-detail.html', user_data)


@login_required
def hire_student(request, work_pk, student_pk):
    """
    Separa um estudante
    :param request:
    :param work_pk: trabalho em questão
    :param student_pk: estudante em questão
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    trabalho = request.user.empresaprofile.trabalho.get(pk=work_pk)
    student = trabalho.inscritos.get(pk=student_pk)
    trabalho.contratados.add(student)
    trabalho.inscritos.remove(student)

    return HttpResponseRedirect(reverse('webapp:empresa:work_detail', kwargs={'work_pk': work_pk}))


@login_required
def refuse_student(request, work_pk, student_pk):
    """
    Recusa um estudante
    :param request:
    :param work_pk: trabalho em questão
    :param student_pk: estudante em questão
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    trabalho = request.user.empresaprofile.trabalho.get(pk=work_pk)
    student = trabalho.inscritos.get(pk=student_pk)
    trabalho.inscritos.remove(student)

    return HttpResponseRedirect(reverse('webapp:empresa:work_detail', kwargs={'work_pk': work_pk}))


@login_required
def fire_student(request, work_pk, student_pk):
    """
    Retira um estudante dos separados
    :param request:
    :param work_pk: trabalho em questão
    :param student_pk: estudante em questão
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    trabalho = request.user.empresaprofile.trabalho.get(pk=work_pk)
    student = trabalho.contratados.get(pk=student_pk)
    trabalho.inscritos.add(student)
    trabalho.contratados.remove(student)

    return HttpResponseRedirect(reverse('webapp:empresa:work_detail', kwargs={'work_pk': work_pk}))


@login_required
def work_delete(request, work_pk):
    """
    Delete um trabalho
    :param request:
    :param work_pk: trabalho em questão
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    trabalho = request.user.empresaprofile.trabalho.get(pk=work_pk).delete()

    return HttpResponseRedirect(reverse('webapp:empresa:home_page'))


@login_required
def private_control(request, work_pk):
    """
    Torna um trabalho público em privado e vice-versa
    :param request:
    :param work_pk: trabalho em questão
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    trabalho = request.user.empresaprofile.trabalho.get(pk=work_pk)
    trabalho.private = not trabalho.private
    trabalho.save()
    return HttpResponseRedirect(reverse('webapp:empresa:work_detail', kwargs={'work_pk': work_pk}))


@login_required
def account_information(request):
    """
    Renderiza a página de atualizar informações da empresa
    :param request:
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    return render(request, 'pages/business-account-information.html')


@login_required
def account_information_update(request):
    """
    Atualiza as informações da empresa
    :param request:
    :return:
    """

    if not hasattr(request.user, 'empresaprofile'):
        raise Http404

    user = request.user

    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.empresaprofile.cidade = request.POST.get('cidade')
    user.empresaprofile.area = request.POST.get('area')
    user.empresaprofile.description = request.POST.get('descricao')

    if request.FILES.get('profile_pic') is not None \
            and magic.from_buffer(request.FILES.get('profile_pic').read(), mime=True).startswith('image/'):
        user.empresaprofile.profile_pic.save(name=user.username + '_pic', content=request.FILES.get('profile_pic'))

    user.save()
    user.empresaprofile.save()

    return render(request, 'pages/business-account-information.html', {'successfully_modified': True})

