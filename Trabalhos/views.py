from django.shortcuts import render, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Trabalho


# Create your views here.
def all_works(request):
    string = ''
    if hasattr(request.user, 'empresaprofile'):
        if len(request.user.empresaprofile.trabalho_set.all()) == 0:
            string = 'Nenhum trabalho cadastrado <br>'
        for work in request.user.empresaprofile.trabalho_set.all():
            string += str(work) + f" <a href='" \
                f"{reverse('webapp:trabalho:students_subscribed',kwargs={'work_pk': work.pk})}" \
                f"'>Inscritos</a> <br>"
        string += f"<a href='{reverse('webapp:trabalho:add_work')}'>Adicionar trabalho</a> " \
            f"<a href='{reverse('webapp:home_page')}'>Voltar</a>"
    elif hasattr(request.user, 'estudanteprofile'):
        if len(Trabalho.objects.all()) == 0:
            string = 'Nenhum trabalho disponível <br>'
        for work in Trabalho.objects.all():
            string += str(work) + f"<a href='{reverse('webapp:trabalho:subscribe_student', kwargs={'pk': work.pk})}" \
                f"'> Inscrever</a><br>"
        string += f"<a href='{reverse('webapp:home_page')}'>Voltar</a>"

    return HttpResponse(string)


def add_work(request):
    return render(request, 'add-work.html')


def add_work_attempt(request):
    print(request.POST['inicio'], request.POST['fim'])
    titulo = request.POST['titulo']
    inicio = request.POST['inicio']
    fim = request.POST['fim']
    pagamento = request.POST['pagamento']
    descricao = request.POST['descricao']
    requisitos = request.POST['requisitos']

    Trabalho.objects.create(business=request.user.empresaprofile, titulo=titulo,
                            inicio=inicio, fim=fim, pagamento=pagamento,
                            descricao=descricao, requisitos=requisitos)

    return HttpResponseRedirect(reverse('webapp:trabalho:all_works'))


def subscribe_student(request, pk):
    target_work = Trabalho.objects.get(pk=pk)
    string = '<br>'.join(target_work.details()) + '<br>'
    if not Trabalho.objects.filter(pk=pk, inscritos__pk=request.user.estudanteprofile.pk).exists():
        string += f"<a href='{reverse('webapp:trabalho:subscribe_student', kwargs={'pk': pk})}try/'>Inscrever-se</a> "
    else:
        string += f"<a href='" \
            f"{reverse('webapp:trabalho:unsubscribe_attempt', kwargs={'pk': pk})}" \
            f"'>Desinscrever-se</a> "

    string += f"<a href='{reverse('webapp:trabalho:all_works')}'>Voltar</a>"

    return HttpResponse(string)


def subscribe_student_attempt(request, pk):
    if hasattr(request.user, 'estudanteprofile'):
        target_work = Trabalho.objects.get(pk=pk)
        target_work.inscritos.add(request.user.estudanteprofile)
    return HttpResponse(f"Inscrito com sucesso!<br><a href='"
                        f"{reverse('webapp:trabalho:subscribe_student', kwargs={'pk': pk})}'>Voltar</a>")


def unsubscribe_student_attempt(request, pk):
    if hasattr(request.user, 'estudanteprofile'):
        target_work = Trabalho.objects.get(pk=pk)
        target_work.inscritos.remove(request.user.estudanteprofile)
    return HttpResponse(f"Desinscrito com sucesso!<br><a href='"
                        f"{reverse('webapp:trabalho:subscribe_student', kwargs={'pk': pk})}'>Voltar</a>")


def students_subscribed(request, work_pk):
    string = ''
    if not hasattr(request.user, 'empresaprofile'):
        raise Http404()

    for subscriber in request.user.empresaprofile.trabalho_set.get(pk=work_pk).inscritos.all():
        string += str(subscriber) + f" <a href='" \
            f"{reverse('webapp:trabalho:students_subscribed_detail',kwargs={'work_pk': work_pk, 'student_pk': subscriber.pk})}" \
            f"'>Detalhes</a><br>"

    string += f"<a href='{reverse('webapp:trabalho:all_works')}'>Voltar</a>"

    return HttpResponse(string)


def students_subscribed_detail(request, work_pk, student_pk):
    estudante = request.user.empresaprofile.trabalho_set.get(pk=work_pk).inscritos.get(pk=student_pk)

    return HttpResponse(str(estudante) + '<br>' + estudante.user.email + f"<br><a href='{reverse('webapp:trabalho:students_subscribed',kwargs={'work_pk': work_pk})}'>Voltar</a>")
