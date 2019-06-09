from django.core.exceptions import ValidationError
from django.shortcuts import render, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Trabalho


def subscribe_student(request, pk):
    target_work = Trabalho.objects.get(pk=pk)
    string = '<br>'.join(target_work.details()) + '<br>'
    if not Trabalho.objects.filter(pk=pk, inscritos__pk=request.user.estudanteprofile.pk).exists():
        string += f"<a href='{reverse('webapp:trabalho:subscribe_student', kwargs={'pk': pk})}try/'>Inscrever-se</a> "
    else:
        string += f"<a href='" \
            f"{reverse('webapp:trabalho:unsubscribe_attempt', kwargs={'pk': pk})}" \
            f"'>Desinscrever-se</a> "

    string += f"<a href='{reverse('webapp:home_page')}'>Voltar</a>"

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


def students_subscribed_detail(request, work_pk, student_pk):
    estudante = request.user.empresaprofile.trabalho_set.get(pk=work_pk).inscritos.get(pk=student_pk)

    return HttpResponse(str(estudante) + '<br>' + estudante.user.email + f"<br><a href='{reverse('webapp:trabalho:students_subscribed',kwargs={'work_pk': work_pk})}'>Voltar</a>")
