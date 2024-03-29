from django.db import models

# modelo para armazenar os ativos
class Ativo(models.Model):
    id_ativo = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    delay = models.IntegerField(default=1000)
    limite_superior = models.FloatField(null=True, blank=True)
    limite_inferior = models.FloatField(null=True, blank=True)
    datas = models.JSONField(null=True, blank=True)

# modelo apenas para salvar o email
class Email(models.Model):
    id_email = models.IntegerField(default=1)
    email = models.TextField(max_length=255)
