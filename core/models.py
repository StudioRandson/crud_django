from django.db import models

# Create your models here.
class usuario(models.Model):
    matricula = models.IntegerField(max_length=12)
    nome = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    armario = models.IntegerField(blank=True, null=True)

    def __str__(self):
         return self.nome