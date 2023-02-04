from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, null=True)
    disponivel = models.BooleanField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

