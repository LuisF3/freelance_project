from django.db import models
from django.contrib.auth.models import User
# from TrabalhoApp.models import Trabalho


# Create your models here.
class EmpresaProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=35, blank=True)
    area = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} ({self.user.username})'
