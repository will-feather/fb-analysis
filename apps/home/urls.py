# -*- encoding: utf-8 -*-

from django.urls import path, re_path

from apps.home import views

urlpatterns = [ 
    path('', views.index, name='home'), # The home page
    path('tabelas_base/', views.tabelas_base, name='tabelas_base'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('downloads/', views.downloads, name='downloads'),
    path('analise_evento', views.analise_evento, name='analise_evento'),
    path('prob_eventos/', views.prob_ev_list, name='prob_eventos'),
    path('execucao/', views.exec_app, name='exec_app'),

    path('graficos', views.graficos, name='graficos'),
    #path('graficos_jogos_desempenho/', views.graf_jg_des, name='graf_jg_des'),
    #path('graficos_probabilidades/', views.graf_prob, name='graf_prob'),
    #path('graficos_odds_ev/', views.graf_odds_ev, name='graf_odds_ev'),

    path('get/redirect/redirect_graficos', views.redirect_graficos, name='redirect_graficos'),

    #testes
    path('tables/', views.tables, name='tables'),
    path('teste/', views.teste, name='teste'),
    path('graficos_teste', views.graficos_teste, name='graficos_teste'),
    re_path(r'^.*\.*', views.pages, name='pages'), # Matches any html file
]
