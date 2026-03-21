from django.db import models   

class Pokemon(models.Model):

    nome = models.CharField(max_length=100)
    numero = models.IntegerField()
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
# Create your models here.
