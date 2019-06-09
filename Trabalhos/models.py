from django.db import models
from EmpresaProfile.models import EmpresaProfile
from EstudanteProfile.models import EstudanteProfile


# Create your models here.
class Trabalho(models.Model):
    titulo = models.CharField(max_length=50)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    pagamento = models.FloatField()
    descricao = models.TextField()
    requisitos = models.TextField()

    business = models.ForeignKey(EmpresaProfile, related_name='trabalho', on_delete=models.DO_NOTHING)
    inscritos = models.ManyToManyField(EstudanteProfile, related_name='subscribers', blank=True)
    contratados = models.ManyToManyField(EstudanteProfile, related_name='contratados', blank=True)

    def __str__(self):
        return self.titulo + ' '.join(self.descricao.split(maxsplit=10)[:10]) + ' | Valor: ' + str(self.pagamento)
