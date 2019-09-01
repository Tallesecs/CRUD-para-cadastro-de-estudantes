from django.db import models


class Estudante(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    CPF = models.IntegerField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    idade = models.CharField(max_length=12)
    bio = models.TextField(max_length=100)

    def __str__(self):
        return self.nome

    '''Função para retornar pelo nome'''