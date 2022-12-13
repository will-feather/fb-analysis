# -*- encoding: utf-8 -*-
from django import template
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from scripts import process as prc
from .models import OddsProbEV

from .models import AtualizacaoApp


@login_required(login_url="/login/")
def index(request):
    
    context = {'segment': 'index'}
    context['atualizacao'] = AtualizacaoApp.objects.all().last()

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):

    # All resource paths end in .html.
    context = {}
    
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


# ------------------- >>
# ---- App Views ---- >>

@login_required
def prob_ev_list(request):

    context = {}
    odds_prob_ev = OddsProbEV.objects.all()
    context['odds_prob_ev'] = odds_prob_ev
    context['atualizacao'] = AtualizacaoApp.objects.all().last()

    return render(request, 'console/odds_prob_ev.html', context)


@login_required
def exec_app(request):

    context = {}
    result = prc.main()

    if result:
        msg = 'Processo Finalizado!'
        flag = True
        AtualizacaoApp.objects.create()
        context['atualizacao'] = AtualizacaoApp.objects.all().last()
    else:
        msg = 'Um Erro Ocorreu No Processo!'
        flag = False

    context['msg'] = msg
    context['flag'] = flag

    odds_prob_ev = OddsProbEV.objects.all()
    context['odds_prob_ev'] = odds_prob_ev

    return render(request, 'console/odds_prob_ev.html', context)







# Testes

@login_required(login_url="/login/")
def tables(request):

    context = {'segment': 'tables'}

    html_template = loader.get_template('console/odds_prob_ev.html')
    return HttpResponse(html_template.render(context, request))