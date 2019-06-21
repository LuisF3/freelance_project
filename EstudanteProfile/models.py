from django.db import models
from django.contrib.auth.models import User
# from TrabalhoApp.models import Trabalho


# Create your models here.
class EstudanteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    universidade = models.CharField(max_length=10, blank=True)
    curso = models.CharField(max_length=50, blank=True)
    previsao_de_formatura = models.IntegerField(null=True)
    descricao = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='student-profile_pic',
                                    default='profile-placeholder.png')

    def __str__(self):
        return f'{self.user.first_name} ({self.user.username})'
