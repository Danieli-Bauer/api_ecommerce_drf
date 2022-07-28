from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
