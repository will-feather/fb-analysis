# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Odds_Probabilities_EV Table
class OddsProbEV(models.Model):

    Competição = models.CharField(max_length=50)
    Evento = models.CharField(max_length=50)
    Data = models.CharField(max_length=20)
    Hora = models.CharField(max_length=10)
    Casa = models.CharField(max_length=30)
    Fora = models.CharField(max_length=30)
    Mercado = models.CharField(max_length=25)
    Entrada = models.CharField(max_length=25)
    Odd = models.CharField(max_length=10)
    Probabilidade = models.CharField(max_length=10)
    EV = models.CharField(max_length=10)

    def __str__(self):
        return self.Evento

    class Meta:
        db_table = "app_odds_prob_ev"


class AtualizacaoApp(models.Model):
    texto = models.CharField(max_length=100, null=True)
    data = models.DateTimeField(default=timezone.now)

    """def __str__(self):
        return self.texto"""

    class Meta:
        db_table = "app_atualizacao"
