from django.db import models
from django.contrib.auth.models import User


class EmpresaProfile(models.Model):
    """
    Objeto representante de uma empresa
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=35, blank=True)
    area = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='business-profile_pic',
                                    default='profile-placeholder.png')

    def __str__(self):
        return f'{self.user.first_name} ({self.user.username})'
