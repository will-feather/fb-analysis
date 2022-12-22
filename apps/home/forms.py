# -*- encoding: utf-8 -*-
from django import forms
from .models import OddsProbEV
from django.forms import ModelChoiceField


class OddsProbEVForm(forms.ModelForm):

    evento = forms.ModelChoiceField(
        queryset=OddsProbEV.objects.order_by().values_list('Evento', flat=True).distinct(), empty_label='Selecione',
        widget=forms.Select(
            attrs={
                'class': 'selectpicker',
                'data-live-search': 'true',
                'data-style': 'btn-primary',
                'data-width': '25%',
                'show-tick': 'true'
            }
        )
    )

    competicao = forms.ModelChoiceField(
        queryset=OddsProbEV.objects.order_by().values_list('Competição', flat=True).distinct(), empty_label='Selecione',
        widget=forms.Select(
            attrs={
                'class': 'selectpicker',
                'data-live-search': 'true',
                'data-style': 'btn-primary',
                'data-width': '25%',
                'show-tick': 'true'
            }
        )
    )

    class Meta:
        model = OddsProbEV
        fields = ('competicao', 'evento')