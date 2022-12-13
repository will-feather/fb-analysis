# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from apps.home import views

urlpatterns = [ 
    path('', views.index, name='home'), # The home page
    path('prob_eventos/', views.prob_ev_list, name='prob_eventos'),
    path('execucao/', views.exec_app, name='exec_app'),
    path('tables/', views.tables, name='tables'),
    re_path(r'^.*\.*', views.pages, name='pages'), # Matches any html file
]
