# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Tabela Base de Dados
class FootballMatches(models.Model):

    div = models.CharField(max_length=50)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    hometeam = models.CharField(max_length=50)
    awayteam = models.CharField(max_length=50)
    fthg = models.IntegerField(default=0)
    ftag = models.IntegerField(default=0)
    hthg = models.IntegerField(default=0)
    htag = models.IntegerField(default=0)
    htg = models.IntegerField(default=0)
    ftg = models.IntegerField(default=0)
    htr = models.CharField(max_length=1, null=True)
    ftr = models.CharField(max_length=1, null=True)
    ambas_marcam = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.div

    class Meta:
        db_table = "app_football_matches"


# Tabela Base de Dados
class Odds(models.Model):

    competicao = models.CharField(max_length=50)
    evento = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    mercado = models.CharField(max_length=50)
    selecao = models.CharField(max_length=50)
    a_favor = models.CharField(max_length=10)
    contra = models.CharField(max_length=10)

    def __str__(self):
        return self.evento

    class Meta:
        db_table = "app_odds"


# Tabela Odds_Probabilidades_EV
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


# Tabela Atualização Projeto
class AtualizacaoApp(models.Model):
    texto = models.CharField(max_length=100, null=True)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto

    class Meta:
        db_table = "app_atualizacao"


# Tabela Agendamento Tarefas
class TarefasAgendadas(models.Model):
    frequencia = models.CharField(max_length=20, null=False)
    tempo = models.CharField(max_length=6, null=False)
    descricao = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = "app_tarefas_agendadas"


# Tabela Taxa Diária
'''class TaxaDiaria(models.Model):
    data = models.DateTimeField(default=timezone.now)
    taxa_diaria_total = models.CharField(max_length=6, null=False)

    def __str__(self):
        return self.data

    class Meta:
        db_table = "app_tarefas_agendadas"'''
