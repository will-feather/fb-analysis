# -*- encoding: utf-8 -*-
from sre_constants import SUCCESS
import sys
from django import template
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from scripts import process as prc
from .models import OddsProbEV, AtualizacaoApp, FootballMatches, Odds
from .forms import OddsProbEVForm


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required(login_url="/login/")
def index(request):
    
    context = {'segment': 'index'}
    context['atualizacao'] = AtualizacaoApp.objects.all().last()

    html_template = loader.get_template('home/index-dashboard.html')
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

# SIDEBAR

@login_required
def tabelas_base(request):

    context = {}
    context['odds'] = Odds.objects.all()
    context['base'] = FootballMatches.objects.all()

    html_template = loader.get_template('console/tabelas-base.html')
    return HttpResponse(html_template.render(context, request))


@login_required
def tarefas(request):

    context = {'segment': 'tarefas'}

    html_template = loader.get_template('console/tarefas.html')
    return HttpResponse(html_template.render(context, request))


@login_required
def downloads(request):

    context = {'segment': 'downloads'}

    html_template = loader.get_template('console/downloads.html')
    return HttpResponse(html_template.render(context, request))


@login_required
def analise_evento(request):

    context = {'segment': 'analise_evento'}

    form = OddsProbEVForm()
    context['form'] = form
    
    if request.method == 'POST':
        competicao = request.POST.get("competicao", "")
        context['competicoes'] = OddsProbEV.objects.filter(Competição=competicao).values_list('Competição', flat=True).distinct()
        context['eventos'] = OddsProbEV.objects.filter(Competição=competicao).values_list('Evento', flat=True).distinct()
    else:    
        context['competicoes'] = OddsProbEV.objects.order_by().values_list('Competição', flat=True).distinct()
        context['eventos'] = OddsProbEV.objects.order_by().values_list('Evento', flat=True).distinct()

    html_template = loader.get_template('console/analise-evento.html')
    return HttpResponse(html_template.render(context, request))


@login_required
def prob_ev_list(request):

    context = {}
    odds_prob_ev = OddsProbEV.objects.all()
    context['odds_prob_ev'] = odds_prob_ev
    context['atualizacao'] = AtualizacaoApp.objects.all().last()

    return render(request, 'console/odds_prob_ev.html', context)


# GRAFICOS

def redirect_graficos(request):

    if request.method == "GET":
        evento = request.GET.get("evento", None)
        pag_graficos = request.GET.get("pag_graficos", None)

        request.session['evento'] = evento
        request.session['pag_graficos'] = pag_graficos
        return redirect('graficos')

    return JsonResponse({}, status=400)


@login_required
def graficos(request):

    context = {}
    evento = request.session.get('evento')
    pag_graficos = request.session.get('pag_graficos')

    if evento and pag_graficos:

        times = evento.split(' x ')
        time_casa = times[0]
        time_fora = times[1]
  
        # context['pag_graficos'] = OddsProbEV.objects.filter(Competição=competicao).values_list('Evento', flat=True).distinct()

        if pag_graficos == '1':

            context['home_team'] = FootballMatches.objects.filter(hometeam=time_casa).values_list('hometeam', flat=True).first()
            context['away_team'] = FootballMatches.objects.filter(hometeam=time_fora).values_list('hometeam', flat=True).first()

            context['home_matches_home'] = FootballMatches.objects.filter(hometeam=time_casa)
            context['home_matches_all'] = FootballMatches.objects.filter(hometeam=time_casa) | FootballMatches.objects.filter(awayteam=time_casa)
            
            context['away_matches_away'] = FootballMatches.objects.filter(awayteam=time_fora)
            context['away_matches_all'] = FootballMatches.objects.filter(hometeam=time_fora) | FootballMatches.objects.filter(awayteam=time_fora)

            html_template = loader.get_template('console/graf-jogos-desempenho.html')
            return HttpResponse(html_template.render(context, request))

        elif pag_graficos == '2':

            #return render(request, 'console/graf-probabilidades.html', context)
            html_template = loader.get_template('console/graf-probabilidades.html')
            return HttpResponse(html_template.render(context, request))

        elif pag_graficos == '3':

            return render(request, 'console/graf-odds-ev.html', context)

        else:

            return redirect('/')

    else:

        return redirect('/')


@login_required
def graf_prob(request):

    context = {'segment': 'graf_prob'}

    html_template = loader.get_template('console/graf-probabilidades.html')
    return HttpResponse(html_template.render(context, request))

@login_required
def graf_prob(request):

    context = {'segment': 'graf_prob'}

    html_template = loader.get_template('console/graf-probabilidades.html')
    return HttpResponse(html_template.render(context, request))


@login_required
def graf_odds_ev(request):

    context = {'segment': 'graf_odds_ev'}

    html_template = loader.get_template('console/graf-odds-ev.html')
    return HttpResponse(html_template.render(context, request))



def graf_testa(request):

    try:
        competicao = request.GET.get("competicao", None)
        # perform operations on the user name.

    except:
        e = sys.exc_info()
        return HttpResponse(e)
    return HttpResponse(SUCCESS)




# EXECUÇÃO PROJETO

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
def teste(request):

    context = {'segment': 'teste'}

    form = OddsProbEVForm()
    context['form'] = form
    
    if request.method == 'POST':
        competicao = request.POST.get("competicao", "")
        context['mtest'] = OddsProbEV.objects.filter(Competição=competicao).values_list('Competição', flat=True).distinct()
    else:    
        context['mtest'] = OddsProbEV.objects.order_by().values_list('Competição', flat=True).distinct()

    html_template = loader.get_template('layouts/teste.html')
    return HttpResponse(html_template.render(context, request))
def graficos_teste(request):

    context = {'segment': 'graficos_teste'}

    html_template = loader.get_template('layouts/graficos.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def tables(request):

    context = {'segment': 'tables'}

    html_template = loader.get_template('console/odds_prob_ev.html')
    return HttpResponse(html_template.render(context, request))