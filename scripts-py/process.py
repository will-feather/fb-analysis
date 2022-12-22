import db
import odds as od
import matches as mt
import numpy as np
import pandas as pd
from datetime import datetime


def processa_lambdas():

    global d_count, h_count, a_count, a_count, am_count
    global over_05, over_15, over_25, over_35, over_45, over_55, over_65

    # Condições Lambda
    d_count = lambda x: x[x == 'D'].count()
    h_count = lambda x: x[x == 'H'].count()
    a_count = lambda x: x[x == 'A'].count()
    am_count = lambda x: x[x == 'S'].count()
    over_05 = lambda x: x[x > 0].count()
    over_15 = lambda x: x[x > 1].count()
    over_25 = lambda x: x[x > 2].count()
    over_35 = lambda x: x[x > 3].count()
    over_45 = lambda x: x[x > 4].count()
    over_55 = lambda x: x[x > 5].count()
    over_65 = lambda x: x[x > 6].count()


# -- DESEMPENHO JOGOS TODOS
def desempenho_jogos_todos(data_frame):
    
    df_gp_jogos_todos = pd.DataFrame()

    # Métricas Principais
    df_gp_jogos_todos['Jogos'] = data_frame.groupby('HomeTeam')['HomeTeam'].count() + data_frame.groupby('AwayTeam')['AwayTeam'].count()
    df_gp_jogos_todos['Gols Marcados'] = data_frame.groupby('HomeTeam')['FTHG'].sum() + data_frame.groupby('AwayTeam')['FTAG'].sum()
    df_gp_jogos_todos['Gols Sofridos'] = data_frame.groupby('HomeTeam')['FTAG'].sum() + data_frame.groupby('AwayTeam')['FTHG'].sum()
    df_gp_jogos_todos['Ambas Marcam'] = data_frame.groupby('HomeTeam')['Ambas Marcam'].apply(am_count) + data_frame.groupby('AwayTeam')['Ambas Marcam'].apply(am_count)
    df_gp_jogos_todos['Gols Marcados HT'] = data_frame.groupby('HomeTeam')['HTHG'].sum() + data_frame.groupby('AwayTeam')['HTAG'].sum()
    df_gp_jogos_todos['Gols Sofridos HT'] = data_frame.groupby('HomeTeam')['HTAG'].sum() + data_frame.groupby('AwayTeam')['HTHG'].sum()
    df_gp_jogos_todos['Over 0,5 HT'] = data_frame.groupby('HomeTeam')['HTG'].apply(over_05) + data_frame.groupby('AwayTeam')['HTG'].apply(over_05)
    df_gp_jogos_todos['Over 1,5 HT'] = data_frame.groupby('HomeTeam')['HTG'].apply(over_15) + data_frame.groupby('AwayTeam')['HTG'].apply(over_15)
    df_gp_jogos_todos['Over 2,5 HT'] = data_frame.groupby('HomeTeam')['HTG'].apply(over_25) + data_frame.groupby('AwayTeam')['HTG'].apply(over_25)
    df_gp_jogos_todos['Over 0,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_05) + data_frame.groupby('AwayTeam')['FTG'].apply(over_05)
    df_gp_jogos_todos['Over 1,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_15) + data_frame.groupby('AwayTeam')['FTG'].apply(over_15)
    df_gp_jogos_todos['Over 2,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_25) + data_frame.groupby('AwayTeam')['FTG'].apply(over_25)
    df_gp_jogos_todos['Over 3,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_35) + data_frame.groupby('AwayTeam')['FTG'].apply(over_35)
    df_gp_jogos_todos['Over 4,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_45) + data_frame.groupby('AwayTeam')['FTG'].apply(over_45)
    df_gp_jogos_todos['Over 5,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_55) + data_frame.groupby('AwayTeam')['FTG'].apply(over_55)
    df_gp_jogos_todos['Over 6,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_65) + data_frame.groupby('AwayTeam')['FTG'].apply(over_65)

    # Métricas de Média
    df_gp_jogos_todos['Gols Marcados Média'] = df_gp_jogos_todos['Gols Marcados'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Gols Sofridos Média'] = df_gp_jogos_todos['Gols Sofridos'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Ambas Marcam Média'] = df_gp_jogos_todos['Ambas Marcam'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Gols Marcados HT Média'] = df_gp_jogos_todos['Gols Marcados HT'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Gols Sofridos HT Média'] = df_gp_jogos_todos['Gols Sofridos HT'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 0,5 HT Média'] = df_gp_jogos_todos['Over 0,5 HT'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 1,5 HT Média'] = df_gp_jogos_todos['Over 1,5 HT'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 2,5 HT Média'] = df_gp_jogos_todos['Over 2,5 HT'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 0,5 Média'] = df_gp_jogos_todos['Over 0,5'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 1,5 Média'] = df_gp_jogos_todos['Over 1,5'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 2,5 Média'] = df_gp_jogos_todos['Over 2,5'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 3,5 Média'] = df_gp_jogos_todos['Over 3,5'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 4,5 Média'] = df_gp_jogos_todos['Over 4,5'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 5,5 Média'] = df_gp_jogos_todos['Over 5,5'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Over 6,5 Média'] = df_gp_jogos_todos['Over 6,5'] / df_gp_jogos_todos['Jogos']

    # Métricas Resultado Final
    df_gp_jogos_todos['Vitorias'] = data_frame.groupby('HomeTeam')['FTR'].apply(h_count) + data_frame.groupby('AwayTeam')['FTR'].apply(a_count)
    df_gp_jogos_todos['Empates'] = data_frame.groupby('HomeTeam')['FTR'].apply(d_count) + data_frame.groupby('AwayTeam')['FTR'].apply(d_count)
    df_gp_jogos_todos['Derrotas'] = data_frame.groupby('HomeTeam')['FTR'].apply(a_count) + data_frame.groupby('AwayTeam')['FTR'].apply(h_count)
    df_gp_jogos_todos['Vitorias Média'] = df_gp_jogos_todos['Vitorias'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Empates Média'] = df_gp_jogos_todos['Empates'] / df_gp_jogos_todos['Jogos']
    df_gp_jogos_todos['Derrotas Média'] = df_gp_jogos_todos['Derrotas'] / df_gp_jogos_todos['Jogos']

    return df_gp_jogos_todos


# -- DESEMPENHO JOGOS CASA HOME
def desempenho_jogos_casa_home(data_frame):
    
    df_gp_jogos_casa_home = pd.DataFrame()

    # Métricas Principais
    df_gp_jogos_casa_home['Jogos'] = data_frame.groupby('HomeTeam')['HomeTeam'].count()
    df_gp_jogos_casa_home['Gols Marcados'] = data_frame.groupby('HomeTeam')['FTHG'].sum()
    df_gp_jogos_casa_home['Gols Sofridos'] = data_frame.groupby('HomeTeam')['FTAG'].sum()
    df_gp_jogos_casa_home['Ambas Marcam'] = data_frame.groupby('HomeTeam')['Ambas Marcam'].apply(am_count)
    df_gp_jogos_casa_home['Gols Marcados HT'] = data_frame.groupby('HomeTeam')['HTHG'].sum()
    df_gp_jogos_casa_home['Gols Sofridos HT'] = data_frame.groupby('HomeTeam')['HTAG'].sum()
    df_gp_jogos_casa_home['Over 0,5 HT'] = data_frame.groupby('HomeTeam')['HTG'].apply(over_05)
    df_gp_jogos_casa_home['Over 1,5 HT'] = data_frame.groupby('HomeTeam')['HTG'].apply(over_15)
    df_gp_jogos_casa_home['Over 2,5 HT'] = data_frame.groupby('HomeTeam')['HTG'].apply(over_25)
    df_gp_jogos_casa_home['Over 0,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_05)
    df_gp_jogos_casa_home['Over 1,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_15)
    df_gp_jogos_casa_home['Over 2,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_25)
    df_gp_jogos_casa_home['Over 3,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_35)
    df_gp_jogos_casa_home['Over 4,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_45)
    df_gp_jogos_casa_home['Over 5,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_55)
    df_gp_jogos_casa_home['Over 6,5'] = data_frame.groupby('HomeTeam')['FTG'].apply(over_65)

    # Métricas de Média
    df_gp_jogos_casa_home['Gols Marcados Média'] = df_gp_jogos_casa_home['Gols Marcados'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Gols Sofridos Média'] = df_gp_jogos_casa_home['Gols Sofridos'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Ambas Marcam Média'] = df_gp_jogos_casa_home['Ambas Marcam'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Gols Marcados HT Média'] = df_gp_jogos_casa_home['Gols Marcados HT'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Gols Sofridos HT Média'] = df_gp_jogos_casa_home['Gols Sofridos HT'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 0,5 HT Média'] = df_gp_jogos_casa_home['Over 0,5 HT'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 1,5 HT Média'] = df_gp_jogos_casa_home['Over 1,5 HT'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 2,5 HT Média'] = df_gp_jogos_casa_home['Over 2,5 HT'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 0,5 Média'] = df_gp_jogos_casa_home['Over 0,5'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 1,5 Média'] = df_gp_jogos_casa_home['Over 1,5'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 2,5 Média'] = df_gp_jogos_casa_home['Over 2,5'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 3,5 Média'] = df_gp_jogos_casa_home['Over 3,5'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 4,5 Média'] = df_gp_jogos_casa_home['Over 4,5'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 5,5 Média'] = df_gp_jogos_casa_home['Over 5,5'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Over 6,5 Média'] = df_gp_jogos_casa_home['Over 6,5'] / df_gp_jogos_casa_home['Jogos']

    # Métricas Resultado Final
    df_gp_jogos_casa_home['Vitorias'] = data_frame.groupby('HomeTeam')['FTR'].apply(h_count)
    df_gp_jogos_casa_home['Empates'] = data_frame.groupby('HomeTeam')['FTR'].apply(d_count)
    df_gp_jogos_casa_home['Derrotas'] = data_frame.groupby('HomeTeam')['FTR'].apply(a_count)
    df_gp_jogos_casa_home['Vitorias Média'] = df_gp_jogos_casa_home['Vitorias'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Empates Média'] = df_gp_jogos_casa_home['Empates'] / df_gp_jogos_casa_home['Jogos']
    df_gp_jogos_casa_home['Derrotas Média'] = df_gp_jogos_casa_home['Derrotas'] / df_gp_jogos_casa_home['Jogos']

    return df_gp_jogos_casa_home


# -- DESEMPENHO JOGOS CASA AWAY
def desempenho_jogos_casa_away(data_frame):
    
    df_gp_jogos_casa_away = pd.DataFrame()

    # Métricas Principais
    df_gp_jogos_casa_away['Jogos'] = data_frame.groupby('AwayTeam')['AwayTeam'].count()
    df_gp_jogos_casa_away['Gols Marcados'] = data_frame.groupby('AwayTeam')['FTHG'].sum()
    df_gp_jogos_casa_away['Gols Sofridos'] = data_frame.groupby('AwayTeam')['FTAG'].sum()
    df_gp_jogos_casa_away['Ambas Marcam'] = data_frame.groupby('AwayTeam')['Ambas Marcam'].apply(am_count)
    df_gp_jogos_casa_away['Gols Marcados HT'] = data_frame.groupby('AwayTeam')['HTHG'].sum()
    df_gp_jogos_casa_away['Gols Sofridos HT'] = data_frame.groupby('AwayTeam')['HTAG'].sum()
    df_gp_jogos_casa_away['Over 0,5 HT'] = data_frame.groupby('AwayTeam')['HTG'].apply(over_05)
    df_gp_jogos_casa_away['Over 1,5 HT'] = data_frame.groupby('AwayTeam')['HTG'].apply(over_15)
    df_gp_jogos_casa_away['Over 2,5 HT'] = data_frame.groupby('AwayTeam')['HTG'].apply(over_25)
    df_gp_jogos_casa_away['Over 0,5'] = data_frame.groupby('AwayTeam')['FTG'].apply(over_05)
    df_gp_jogos_casa_away['Over 1,5'] = data_frame.groupby('AwayTeam')['FTG'].apply(over_15)
    df_gp_jogos_casa_away['Over 2,5'] = data_frame.groupby('AwayTeam')['FTG'].apply(over_25)
    df_gp_jogos_casa_away['Over 3,5'] = data_frame.groupby('AwayTeam')['FTG'].apply(over_35)
    df_gp_jogos_casa_away['Over 4,5'] = data_frame.groupby('AwayTeam')['FTG'].apply(over_45)
    df_gp_jogos_casa_away['Over 5,5'] = data_frame.groupby('AwayTeam')['FTG'].apply(over_55)
    df_gp_jogos_casa_away['Over 6,5'] = data_frame.groupby('AwayTeam')['FTG'].apply(over_65)

    # Métricas de Média
    df_gp_jogos_casa_away['Gols Marcados Média'] = df_gp_jogos_casa_away['Gols Marcados'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Gols Sofridos Média'] = df_gp_jogos_casa_away['Gols Sofridos'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Ambas Marcam Média'] = df_gp_jogos_casa_away['Ambas Marcam'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Gols Marcados HT Média'] = df_gp_jogos_casa_away['Gols Marcados HT'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Gols Sofridos HT Média'] = df_gp_jogos_casa_away['Gols Sofridos HT'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 0,5 HT Média'] = df_gp_jogos_casa_away['Over 0,5 HT'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 1,5 HT Média'] = df_gp_jogos_casa_away['Over 1,5 HT'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 2,5 HT Média'] = df_gp_jogos_casa_away['Over 2,5 HT'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 0,5 Média'] = df_gp_jogos_casa_away['Over 0,5'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 1,5 Média'] = df_gp_jogos_casa_away['Over 1,5'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 2,5 Média'] = df_gp_jogos_casa_away['Over 2,5'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 3,5 Média'] = df_gp_jogos_casa_away['Over 3,5'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 4,5 Média'] = df_gp_jogos_casa_away['Over 4,5'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 5,5 Média'] = df_gp_jogos_casa_away['Over 5,5'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Over 6,5 Média'] = df_gp_jogos_casa_away['Over 6,5'] / df_gp_jogos_casa_away['Jogos']

    # Métricas Resultado Final
    df_gp_jogos_casa_away['Vitorias'] = data_frame.groupby('AwayTeam')['FTR'].apply(h_count)
    df_gp_jogos_casa_away['Empates'] = data_frame.groupby('AwayTeam')['FTR'].apply(d_count)
    df_gp_jogos_casa_away['Derrotas'] = data_frame.groupby('AwayTeam')['FTR'].apply(a_count)
    df_gp_jogos_casa_away['Vitorias Média'] = df_gp_jogos_casa_away['Vitorias'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Empates Média'] = df_gp_jogos_casa_away['Empates'] / df_gp_jogos_casa_away['Jogos']
    df_gp_jogos_casa_away['Derrotas Média'] = df_gp_jogos_casa_away['Derrotas'] / df_gp_jogos_casa_away['Jogos']

    return df_gp_jogos_casa_away


# -- UNIÃO DE TODAS TABELAS DE DESEMPENHO
def inner_table_jogos(df_gp_jogos_todos, df_gp_jogos_casa_home, df_gp_jogos_casa_away):

    df_gp_jogos_casa_away.index.names = ['HomeTeam']
    df_inner_merged_temp_jogos = pd.merge(pd.merge(df_gp_jogos_todos, df_gp_jogos_casa_home, on=["HomeTeam"]), df_gp_jogos_casa_away, on=["HomeTeam"]).round(3)

    df_inner_merged_jogos = df_inner_merged_temp_jogos[['Ambas Marcam Média_x', 'Ambas Marcam Média_y', 'Ambas Marcam Média', 'Vitorias Média_y', 'Empates Média_y', 'Derrotas Média_y', 
                                                        'Vitorias Média_x', 'Empates Média_x', 'Derrotas Média_x', 'Over 0,5 HT Média_x', 'Over 0,5 HT Média_y', 'Over 0,5 HT Média',
                                                        'Over 1,5 HT Média_x', 'Over 1,5 HT Média_y', 'Over 1,5 HT Média', 'Over 2,5 HT Média_x', 'Over 2,5 HT Média_y', 'Over 2,5 HT Média', 
                                                        'Over 0,5 Média_x', 'Over 0,5 Média_y', 'Over 0,5 Média', 'Over 1,5 Média_x', 'Over 1,5 Média_y', 'Over 1,5 Média', 
                                                        'Over 2,5 Média_x', 'Over 2,5 Média_y', 'Over 2,5 Média', 'Over 3,5 Média_x', 'Over 3,5 Média_y', 'Over 3,5 Média', 
                                                        'Over 4,5 Média_x', 'Over 4,5 Média_y', 'Over 4,5 Média', 'Over 5,5 Média_x', 'Over 5,5 Média_y', 'Over 5,5 Média', 
                                                        'Over 6,5 Média_x', 'Over 6,5 Média_y', 'Over 6,5 Média', 'Vitorias Média', 'Empates Média', 'Derrotas Média', ]].copy()

    return df_inner_merged_jogos                                             


# -- UNIÃO TABELAS EVENTOS ODDS E MATCHES
def inner_tables_odds_matches(df_odds, df_inner_merged_jogos):

    df_odds[['Time A','Time B']] = df_odds['Evento'].str.split('x', expand=True)
    df_odds['Time A'] = df_odds['Time A'].str.strip()
    df_odds['Time B'] = df_odds['Time B'].str.strip()

    df_odds_group_team = df_odds[['Evento','Time A','Time B']].drop_duplicates('Evento')

    df_inner_merged_jogos = df_inner_merged_jogos.reset_index(level=0)
    df_events_matches_temp = pd.merge(pd.merge(df_odds_group_team, df_inner_merged_jogos, left_on='Time A', right_on='HomeTeam'), df_inner_merged_jogos, left_on='Time B', right_on='HomeTeam')
    df_events_matches_temp.rename(columns={'Ambas Marcam Média_x_x': 'AM Home Todos', 'Ambas Marcam Média_x_y': 'AM Away Todos', 'Ambas Marcam Média_y_x': 'AM Home', 'Ambas Marcam Média_y': 'AM Away', 
            'Over 0,5 HT Média_x_x': 'Over 05 HT Home Todos', 'Over 0,5 HT Média_x_y': 'Over 05 HT Away Todos', 'Over 0,5 HT Média_y_x': 'Over 05 HT Home', 'Over 0,5 HT Média_y': 'Over 05 HT Away',
            'Over 1,5 HT Média_x_x': 'Over 15 HT Home Todos', 'Over 1,5 HT Média_x_y': 'Over 15 HT Away Todos', 'Over 1,5 HT Média_y_x': 'Over 15 HT Home', 'Over 1,5 HT Média_y': 'Over 15 HT Away',
            'Over 2,5 HT Média_x_x': 'Over 25 HT Home Todos', 'Over 2,5 HT Média_x_y': 'Over 25 HT Away Todos', 'Over 2,5 HT Média_y_x': 'Over 25 HT Home', 'Over 2,5 HT Média_y': 'Over 25 HT Away',
            'Over 0,5 Média_x_x': 'Over 05 Home Todos', 'Over 0,5 Média_x_y': 'Over 05 Away Todos', 'Over 0,5 Média_y_x': 'Over 05 Home', 'Over 0,5 Média_y': 'Over 05 Away',
            'Over 1,5 Média_x_x': 'Over 15 Home Todos', 'Over 1,5 Média_x_y': 'Over 15 Away Todos', 'Over 1,5 Média_y_x': 'Over 15 Home', 'Over 1,5 Média_y': 'Over 15 Away',
            'Over 2,5 Média_x_x': 'Over 25 Home Todos', 'Over 2,5 Média_x_y': 'Over 25 Away Todos', 'Over 2,5 Média_y_x': 'Over 25 Home', 'Over 2,5 Média_y': 'Over 25 Away',
            'Over 3,5 Média_x_x': 'Over 35 Home Todos', 'Over 3,5 Média_x_y': 'Over 35 Away Todos', 'Over 3,5 Média_y_x': 'Over 35 Home', 'Over 3,5 Média_y': 'Over 35 Away',
            'Over 4,5 Média_x_x': 'Over 45 Home Todos', 'Over 4,5 Média_x_y': 'Over 45 Away Todos', 'Over 4,5 Média_y_x': 'Over 45 Home', 'Over 4,5 Média_y': 'Over 45 Away',
            'Over 5,5 Média_x_x': 'Over 55 Home Todos', 'Over 5,5 Média_x_y': 'Over 55 Away Todos', 'Over 5,5 Média_y_x': 'Over 55 Home', 'Over 5,5 Média_y': 'Over 55 Away',
            'Over 6,5 Média_x_x': 'Over 65 Home Todos', 'Over 6,5 Média_x_y': 'Over 65 Away Todos', 'Over 6,5 Média_y_x': 'Over 65 Home', 'Over 6,5 Média_y': 'Over 65 Away',
            'Vitorias Média_x_x': 'Vitorias Home Todos', 'Vitorias Média_y_x': 'Vitorias Home', 'Empates Média_x_x': 'Empates Home Todos', 'Empates Média_y_x': 'Empates Home', 
            'Derrotas Média_x_x': 'Derrotas Home Todos', 'Derrotas Média_y_x': 'Derrotas Home', 'Vitorias Média_x_y': 'Vitorias Away Todos', 'Vitorias Média_y': 'Vitorias Away', 
            'Empates Média_x_y': 'Empates Away Todos', 'Empates Média_y': 'Empates Away', 'Derrotas Média_x_y': 'Derrotas Away Todos', 'Derrotas Média_y': 'Derrotas Away'}, inplace=True)

    df_events_matches = df_events_matches_temp.drop(columns=['Ambas Marcam Média_x', 'Ambas Marcam Média_y_y', 'Vitorias Média_y_y', 'Empates Média_y_y', 'Derrotas Média_y_y', 'Over 0,5 HT Média_x', 
                                            'Over 0,5 HT Média_y_y', 'Over 1,5 HT Média_x', 'Over 1,5 HT Média_y_y', 'Over 2,5 HT Média_x', 'Over 2,5 HT Média_y_y', 'Over 0,5 Média_x', 
                                            'Over 0,5 Média_y_y', 'Over 1,5 Média_x', 'Over 1,5 Média_y_y', 'Over 2,5 Média_x', 'Over 2,5 Média_y_y', 'Over 3,5 Média_x', 'Over 3,5 Média_y_y', 
                                            'Over 4,5 Média_x', 'Over 4,5 Média_y_y', 'Over 5,5 Média_x', 'Over 5,5 Média_y_y', 'Over 6,5 Média_x', 'Over 6,5 Média_y_y', 'Vitorias Média_x', 
                                            'Empates Média_x', 'Derrotas Média_x'])

    return df_events_matches


# -- CÁLCULA PROBABILIDADES
def calculate_probabilities(df_events_matches):

    df_events_matches['% Vitoria'] = round(((df_events_matches['Vitorias Home'] / 100) * 60) + ((df_events_matches['Vitorias Home Todos'] / 100) * 40), 3)
    df_events_matches['% Empate'] = round(((df_events_matches['Empates Home'] / 100) * 60) + ((df_events_matches['Empates Home Todos'] / 100) * 40), 3)
    df_events_matches['% Derrota'] = round(((df_events_matches['Derrotas Home'] / 100) * 60) + ((df_events_matches['Derrotas Home Todos'] / 100) * 40), 3)

    df_events_matches['% AM Sim'] = round(((((df_events_matches['AM Home']/100)*70)+((df_events_matches['AM Away']/100)*30))+((((df_events_matches['AM Home Todos']/100)*70)+((df_events_matches['AM Away Todos']/100)*30))))/2, 3)
    df_events_matches['% AM Não'] = 1 - df_events_matches['% AM Sim']

    df_events_matches['% Over 05 HT'] = round(((((df_events_matches['Over 05 HT Home']/100)*60)+((df_events_matches['Over 05 HT Away']/100)*40))+((((df_events_matches['Over 05 HT Home Todos']/100)*60)+((df_events_matches['Over 05 HT Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 15 HT'] = round(((((df_events_matches['Over 15 HT Home']/100)*60)+((df_events_matches['Over 15 HT Away']/100)*40))+((((df_events_matches['Over 15 HT Home Todos']/100)*60)+((df_events_matches['Over 15 HT Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 25 HT'] = round(((((df_events_matches['Over 25 HT Home']/100)*60)+((df_events_matches['Over 25 HT Away']/100)*40))+((((df_events_matches['Over 25 HT Home Todos']/100)*60)+((df_events_matches['Over 25 HT Away Todos']/100)*40))))/2, 3)

    df_events_matches['% Over 05'] = round(((((df_events_matches['Over 05 Home']/100)*60)+((df_events_matches['Over 05 Away']/100)*40))+((((df_events_matches['Over 05 Home Todos']/100)*60)+((df_events_matches['Over 05 Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 15'] = round(((((df_events_matches['Over 15 Home']/100)*60)+((df_events_matches['Over 15 Away']/100)*40))+((((df_events_matches['Over 15 Home Todos']/100)*60)+((df_events_matches['Over 15 Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 25'] = round(((((df_events_matches['Over 25 Home']/100)*60)+((df_events_matches['Over 25 Away']/100)*40))+((((df_events_matches['Over 25 Home Todos']/100)*60)+((df_events_matches['Over 25 Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 35'] = round(((((df_events_matches['Over 35 Home']/100)*60)+((df_events_matches['Over 35 Away']/100)*40))+((((df_events_matches['Over 35 Home Todos']/100)*60)+((df_events_matches['Over 35 Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 45'] = round(((((df_events_matches['Over 45 Home']/100)*60)+((df_events_matches['Over 45 Away']/100)*40))+((((df_events_matches['Over 45 Home Todos']/100)*60)+((df_events_matches['Over 45 Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 55'] = round(((((df_events_matches['Over 55 Home']/100)*60)+((df_events_matches['Over 55 Away']/100)*40))+((((df_events_matches['Over 55 Home Todos']/100)*60)+((df_events_matches['Over 55 Away Todos']/100)*40))))/2, 3)
    df_events_matches['% Over 65'] = round(((((df_events_matches['Over 65 Home']/100)*60)+((df_events_matches['Over 65 Away']/100)*40))+((((df_events_matches['Over 65 Home Todos']/100)*60)+((df_events_matches['Over 65 Away Todos']/100)*40))))/2, 3)

    df_events_matches['% Under 05'] = 1 - df_events_matches['% Over 05']
    df_events_matches['% Under 15'] = 1 - df_events_matches['% Over 15']
    df_events_matches['% Under 25'] = 1 - df_events_matches['% Over 25']
    df_events_matches['% Under 35'] = 1 - df_events_matches['% Over 35']

    df_events_matches['% Vitoria Away'] = round(((df_events_matches['Vitorias Away'] / 100) * 60) + ((df_events_matches['Vitorias Away Todos'] / 100) * 40), 3)
    df_events_matches['% Empate Away'] = round(((df_events_matches['Empates Away'] / 100) * 60) + ((df_events_matches['Empates Away Todos'] / 100) * 40), 3)
    df_events_matches['% Derrota Away'] = round(((df_events_matches['Derrotas Away'] / 100) * 60) + ((df_events_matches['Derrotas Away Todos'] / 100) * 40), 3)

    df_events_matches['% Media Vitoria'] = round((df_events_matches['% Vitoria']+(1-df_events_matches['% Vitoria Away']))/2, 3)
    df_events_matches['% Media Empate'] = round((df_events_matches['% Empate']+(1-df_events_matches['% Empate Away']))/2, 3)
    df_events_matches['% Media Derrota'] = round((df_events_matches['% Derrota']+(1-df_events_matches['% Derrota Away']))/2, 3)
    df_events_matches['% Media Total'] = round(df_events_matches['% Media Vitoria'] + df_events_matches['% Media Empate'] + df_events_matches['% Media Derrota'], 3)

    df_events_matches['% Media Vitoria'] = df_events_matches['% Media Vitoria'] / df_events_matches['% Media Total']
    df_events_matches['% Media Empate'] = df_events_matches['% Media Empate']  / df_events_matches['% Media Total']
    df_events_matches['% Media Derrota'] = df_events_matches['% Media Derrota'] / df_events_matches['% Media Total']

    cols = ['Evento', 'Time A', 'Time B', '% Media Vitoria', '% Media Empate', '% Media Derrota', '% AM Sim', '% AM Não', '% Over 05 HT', 
            '% Over 15 HT', '% Over 25 HT', '% Over 05', '% Over 15', '% Over 25', '% Over 35', '% Over 45', '% Over 55', '% Over 65',
            '% Under 05', '% Under 15', '% Under 25', '% Under 35']

    df_odds_eventos = df_events_matches[cols].copy()
    df_odds_probabilidades = df_events_matches[cols].copy()

    return df_odds_eventos, df_odds_probabilidades


# -- PREPARA TABELA ODDS EVENTOS
def prepara_odds_events(df_odds_eventos):

    # CÁLCULO DE DIVISÃO

    df_odds_eventos['Div Vitoria'] = round(100/(df_odds_eventos['% Media Vitoria'] * 100), 3)
    df_odds_eventos['Div Empate'] = round(100/(df_odds_eventos['% Media Empate'] * 100), 3)
    df_odds_eventos['Div Derrota'] = round(100/(df_odds_eventos['% Media Derrota'] * 100), 3)

    df_odds_eventos['Div AM Sim'] = round(100/(df_odds_eventos['% AM Sim'] * 100), 3)
    df_odds_eventos['Div AM Não'] = round(100/(df_odds_eventos['% AM Não'] * 100), 3)

    df_odds_eventos['Div Over 05 HT'] = round(100/(df_odds_eventos['% Over 05 HT'] * 100), 3)
    df_odds_eventos['Div Over 15 HT'] = round(100/(df_odds_eventos['% Over 15 HT'] * 100), 3)
    df_odds_eventos['Div Over 25 HT'] = round(100/(df_odds_eventos['% Over 25 HT'] * 100), 3)

    df_odds_eventos['Div Over 05'] = round(100/(df_odds_eventos['% Over 05'] * 100), 3)
    df_odds_eventos['Div Over 15'] = round(100/(df_odds_eventos['% Over 15'] * 100), 3)
    df_odds_eventos['Div Over 25'] = round(100/(df_odds_eventos['% Over 25'] * 100), 3)
    df_odds_eventos['Div Over 35'] = round(100/(df_odds_eventos['% Over 35'] * 100), 3)
    df_odds_eventos['Div Over 45'] = round(100/(df_odds_eventos['% Over 45'] * 100), 3)
    df_odds_eventos['Div Over 55'] = round(100/(df_odds_eventos['% Over 55'] * 100), 3)
    df_odds_eventos['Div Over 65'] = round(100/(df_odds_eventos['% Over 65'] * 100), 3)

    df_odds_eventos['Div Under 05'] = round(100/(df_odds_eventos['% Under 05'] * 100), 2)
    df_odds_eventos['Div Under 15'] = round(100/(df_odds_eventos['% Under 15'] * 100), 2)
    df_odds_eventos['Div Under 25'] = round(100/(df_odds_eventos['% Under 25'] * 100), 2)
    df_odds_eventos['Div Under 35'] = round(100/(df_odds_eventos['% Under 35'] * 100), 2)

    df_odds_eventos.replace([np.inf, -np.inf], 0, inplace=True)

    # CÁLCULO DE EVENTO

    """
    df_odds_eventos['EV Vitoria'] = round(100/(df_odds_prob_eventos['% Media Vitoria'] * 100), 2)
    df_odds_eventos['EV Empate'] = round(100/(df_odds_prob_eventos['% Media Empate'] * 100), 2)
    df_odds_eventos['EV Derrota'] = round(100/(df_odds_prob_eventos['% Media Derrota'] * 100), 2)

    df_odds_eventos['EV AM Sim'] = round(100/(df_odds_prob_eventos['% AM Sim'] * 100), 2)
    df_odds_eventos['EV AM Não'] = round(100/(df_odds_prob_eventos['% AM Não'] * 100), 2)

    df_odds_eventos['EV Over 05 HT'] = round(100/(df_odds_prob_eventos['% Over 05 HT'] * 100), 2)
    df_odds_eventos['EV Over 15 HT'] = round(100/(df_odds_prob_eventos['% Over 15 HT'] * 100), 2)
    df_odds_eventos['EV Over 25 HT'] = round(100/(df_odds_prob_eventos['% Over 25 HT'] * 100), 2)

    df_odds_eventos['EV Over 05'] = round(100/(df_odds_prob_eventos['% Over 05'] * 100), 2)
    df_odds_eventos['EV Over 15'] = round(100/(df_odds_prob_eventos['% Over 15'] * 100), 2)
    df_odds_eventos['EV Over 25'] = round(100/(df_odds_prob_eventos['% Over 25'] * 100), 2)
    df_odds_eventos['EV Over 35'] = round(100/(df_odds_prob_eventos['% Over 35'] * 100), 2)
    df_odds_eventos['EV Over 45'] = round(100/(df_odds_prob_eventos['% Over 45'] * 100), 2)
    df_odds_eventos['EV Over 55'] = round(100/(df_odds_prob_eventos['% Over 55'] * 100), 2)
    df_odds_eventos['EV Over 65'] = round(100/(df_odds_prob_eventos['% Over 65'] * 100), 2)
    """

    return df_odds_eventos


# -- TABULAÇÃO EVENTOS
def cross_table_events(df_odds_eventos):

    df_clear_odds_eventos = df_odds_eventos.drop(columns=['% Media Vitoria', '% Media Empate', '% Media Derrota', '% AM Sim', '% AM Não', 
        '% Over 05 HT', '% Over 15 HT', '% Over 25 HT', '% Over 05', '% Over 15', '% Over 25', '% Over 35', '% Over 45', '% Over 55', 
        '% Over 65', '% Under 05', '% Under 15', '% Under 25', '% Under 35'])

    df_clear_odds_eventos.rename(columns={'Div Vitoria': 'Casa Vitoria', 'Div Empate': 'Casa Empate', 'Div Derrota': 'Casa Derrota', 'Div AM Sim': 'AM Sim', 
        'Div AM Não': 'AM Não', 'Div Over 05 HT': 'Over 05 HT', 'Div Over 15 HT': 'Over 15 HT', 'Div Over 25 HT': 'Over 25 HT', 'Div Over 05': 'Over 05', 
        'Div Over 15': 'Over 15', 'Div Over 25': 'Over 25', 'Div Over 35': 'Over 35', 'Div Over 45': 'Over 45', 'Div Over 55': 'Over 55', 'Div Over 65': 'Over 65',
        'Div Under 05': 'Under 05', 'Div Under 15': 'Under 15', 'Div Under 25': 'Under 25', 'Div Under 35': 'Under 35'}, inplace=True)

    df_cross_table_eventos = df_clear_odds_eventos.melt(id_vars=["Evento", "Time A", "Time B"], var_name="Mercado Divisão", value_name="Divisão")

    # Campo Calculado Mercado ID 
    # Resultado Final - 01, Ambos Marcam - 02, HT Gols - 03, FT Gols - 04

    mercado_conditions = [
        (df_cross_table_eventos['Mercado Divisão'].str[:4].str.upper() == 'CASA'),
        (df_cross_table_eventos['Mercado Divisão'].str[:2].str.upper() == 'AM'),
        (df_cross_table_eventos['Mercado Divisão'].str[-2:].str.upper() == 'HT'),
        (df_cross_table_eventos['Mercado Divisão'].str[:5].str.upper() == 'UNDER')
        ]
    mercado_values = ['01', '02', '03', '05']
    df_cross_table_eventos.loc[:,"Mercado ID"] = np.select(mercado_conditions, mercado_values, default = '04')

    # Campo Calculado Entrada ID 
    # Casa - C1, Empate - E2, Fora - F3, AM Sim - S4, AM Não - N5, OH 05 - OH05, OH 15 - OH15, OH 25 - OH25, 
    # OF 05 - OF05, OF 15 - OF15, OF 25 - OF25, OF 35 - OF35, OF 45 - OF45, OF 55 - OF55, OF 65 - OF65,
    # UF 05 - UF05, UF 15 - UF15, UF 25 - UF25, UF 35 - UF35

    entrada_conditions = [
        (df_cross_table_eventos['Mercado Divisão'].str[-7:].str.upper() == 'VITORIA'),
        (df_cross_table_eventos['Mercado Divisão'].str[-6:].str.upper() == 'EMPATE'),
        (df_cross_table_eventos['Mercado Divisão'].str[-7:].str.upper() == 'DERROTA'),
        (df_cross_table_eventos['Mercado Divisão'].str[-3:].str.upper() == 'SIM'),
        (df_cross_table_eventos['Mercado Divisão'].str[-3:].str.upper() == 'NÃO'),
        (df_cross_table_eventos['Mercado ID'] == '03'),
        (df_cross_table_eventos['Mercado ID'] == '05'),
        ]
    entrada_values = ['C1', 'E2', 'F3', 'S4', 'N5', 'OH' + df_cross_table_eventos['Mercado Divisão'].str[-5:-3], 'UF' + df_cross_table_eventos['Mercado Divisão'].str[-2:], ]
    df_cross_table_eventos.loc[:,"Entrada ID"] = np.select(entrada_conditions, entrada_values, default = 'OF' + df_cross_table_eventos['Mercado Divisão'].str[-2:])


    df_cross_table_eventos['Evento ID'] = df_cross_table_eventos['Evento'] + df_cross_table_eventos['Mercado ID'] + df_cross_table_eventos['Entrada ID']
    df_cross_table_eventos['Evento ID'] = df_cross_table_eventos['Evento ID'].apply(hash)

    return df_cross_table_eventos


# -- TABULAÇÃO PROBABILIDADES
def cross_table_probabilities(df_odds_probabilidades):

    df_odds_probabilidades.rename(columns={'% Media Vitoria': 'Casa Vitoria', '% Media Empate': 'Casa Empate', '% Media Derrota': 'Casa Derrota', 
        '% AM Sim': 'AM Sim', '% AM Não': 'AM Não', '% Over 05 HT': 'Over 05 HT', '% Over 15 HT': 'Over 15 HT', '% Over 25 HT': 'Over 25 HT', 
        '% Over 05': 'Over 05', '% Over 15': 'Over 15', '% Over 25': 'Over 25', '% Over 35': 'Over 35', '% Over 45': 'Over 45', '% Over 55': 'Over 55', 
        '% Over 65': 'Over 65', '% Under 05': 'Under 05', '% Under 15': 'Under 15', '% Under 25': 'Under 25', '% Under 35': 'Under 35'}, inplace=True)

    df_cross_table_probabilidades = df_odds_probabilidades.melt(id_vars=["Evento", "Time A", "Time B"], var_name="Mercado Prob", value_name="Probabilidade")
    df_cross_table_probabilidades['Probabilidade'] = df_cross_table_probabilidades['Probabilidade'].astype(float).map("{:.1%}".format)

    # Campo Calculado Mercado ID 
    # Resultado Final - 01, Ambos Marcam - 02, HT Gols - 03, FT Gols - 04

    mercado_conditions = [
        (df_cross_table_probabilidades['Mercado Prob'].str[:4].str.upper() == 'CASA'),
        (df_cross_table_probabilidades['Mercado Prob'].str[:2].str.upper() == 'AM'),
        (df_cross_table_probabilidades['Mercado Prob'].str[-2:].str.upper() == 'HT'),
        (df_cross_table_probabilidades['Mercado Prob'].str[:5].str.upper() == 'UNDER')
        ]
    mercado_values = ['01', '02', '03', '05']
    df_cross_table_probabilidades.loc[:,"Mercado ID"] = np.select(mercado_conditions, mercado_values, default = '04')

    # Campo Calculado Entrada ID 
    # Casa - C1, Empate - E2, Fora - F3, AM Sim - S4, AM Não - N5, OH 05 - OH05, OH 15 - OH15, OH 25 - OH25, 
    # OF 05 - OF05, OF 15 - OF15, OF 25 - OF25, OF 35 - OF35, OF 45 - OF45, OF 55 - OF55, OF 65 - OF65,
    # UF 05 - UF05, UF 15 - UF15, UF 25 - UF25, UF 35 - UF35

    entrada_conditions = [
        (df_cross_table_probabilidades['Mercado Prob'].str[-7:].str.upper() == 'VITORIA'),
        (df_cross_table_probabilidades['Mercado Prob'].str[-6:].str.upper() == 'EMPATE'),
        (df_cross_table_probabilidades['Mercado Prob'].str[-7:].str.upper() == 'DERROTA'),
        (df_cross_table_probabilidades['Mercado Prob'].str[-3:].str.upper() == 'SIM'),
        (df_cross_table_probabilidades['Mercado Prob'].str[-3:].str.upper() == 'NÃO'),
        (df_cross_table_probabilidades['Mercado ID'] == '03'),
        (df_cross_table_probabilidades['Mercado ID'] == '05'),
        ]
    entrada_values = ['C1', 'E2', 'F3', 'S4', 'N5', 'OH' + df_cross_table_probabilidades['Mercado Prob'].str[-5:-3], 'UF' + df_cross_table_probabilidades['Mercado Prob'].str[-2:], ]
    df_cross_table_probabilidades.loc[:,"Entrada ID"] = np.select(entrada_conditions, entrada_values, default = 'OF' + df_cross_table_probabilidades['Mercado Prob'].str[-2:])


    df_cross_table_probabilidades['Evento ID'] = df_cross_table_probabilidades['Evento'] + df_cross_table_probabilidades['Mercado ID'] + df_cross_table_probabilidades['Entrada ID']
    df_cross_table_probabilidades['Evento ID'] = df_cross_table_probabilidades['Evento ID'].apply(hash)

    return df_cross_table_probabilidades


# -- ODDS IDS
def create_odds_ids(df_odds):

    # Campo Calculado Mercado ID

    mercado_conditions = [
        (df_odds['Mercado'].str[:9].str.upper() == 'RESULTADO'),
        (df_odds['Mercado'].str[:5].str.upper() == 'AMBOS'),
        (df_odds['Mercado'].str[:8].str.upper() == '1º TEMPO'),
        (df_odds['Mercado'].str[:4].str.upper() == 'MAIS') & (df_odds['Seleção'].str[:5].str.upper() == 'MENOS')
        ]
    mercado_values = ['01', '02', '03', '05']
    df_odds.loc[:,"Mercado ID"] = np.select(mercado_conditions, mercado_values, default = '04')

    # Campo Calculado Entrada ID

    entrada_conditions = [
        (df_odds['Seleção'] == df_odds['Time A']),
        (df_odds['Seleção'] == df_odds['Time B']),
        (df_odds['Seleção'].str.upper().str.strip() == 'EMPATE'),
        (df_odds['Seleção'].str.upper().str.strip() == 'SIM'),
        (df_odds['Seleção'].str.upper().str.strip() == 'NÃO'),
        (df_odds['Mercado ID'] == '03'),
        (df_odds['Mercado ID'] == '05')
        ]
    entrada_values = ['C1', 'F3', 'E2', 'S4', 'N5', 'OH' + df_odds['Mercado'].str[-8:-5].str.replace('.', ''), 'UF' + df_odds['Mercado'].str[-8:-5].str.replace(',', ''), ]
    df_odds.loc[:,"Entrada ID"] = np.select(entrada_conditions, entrada_values, default = 'OF' + df_odds['Mercado'].str[-8:-5].str.replace(',', ''))

    # Campo Calculado Mercado
    mercado_conditions = [
        (df_odds['Mercado'].str[:5].str.upper() == 'AMBOS'),
        (df_odds['Mercado'].str[:8].str.upper() == '1º TEMPO'),
        (df_odds['Mercado'].str[:4].str.upper() == 'MAIS')
        ]
    mercado_values = ['Ambos Marcam', 'HT Gols', 'FT Gols']
    df_odds.loc[:,"Mercado AJ"] = np.select(mercado_conditions, mercado_values, default='Resultado Final')

    df_odds['Evento ID'] = df_odds['Evento'] + df_odds['Mercado ID'] + df_odds['Entrada ID']
    df_odds['Evento ID'] = df_odds['Evento ID'].apply(hash)

    df_odds[['Data', 'Hora']] = df_odds['Data'].str.split(pat = ',', expand = True)

    return df_odds


# -- # RESULTADO FINAL
def odds_prob_events_results(df_odds, df_cross_table_eventos, df_cross_table_probabilidades):

    inner_merged_odds_prob_ev = pd.merge(pd.merge(df_odds[['Evento ID', 'Competição', 'Evento', 'Data', 'Hora', 'Time A', 'Time B', 'Mercado AJ', 'Seleção', 'A favor']], 
                                df_cross_table_probabilidades[['Evento ID','Probabilidade']], on=['Evento ID', 'Evento ID']), df_cross_table_eventos[['Evento ID', 'Divisão']], on='Evento ID')

    inner_merged_odds_prob_ev.rename(columns={'Time A': 'Casa', 'Time B': 'Fora', 'Mercado AJ': 'Mercado', 'Seleção': 'Entrada', 'A favor': 'Odd'}, inplace=True)

    inner_merged_odds_prob_ev['EV'] = round(inner_merged_odds_prob_ev['Odd']/inner_merged_odds_prob_ev['Divisão']-1, 3)
    inner_merged_odds_prob_ev['EV'] = inner_merged_odds_prob_ev['EV'].astype(float).map("{:.0%}".format)

    inner_merged_odds_prob_ev = inner_merged_odds_prob_ev.drop(columns=['Divisão', 'Evento ID'])
    inner_merged_odds_prob_ev.index.names = ['id']

    return inner_merged_odds_prob_ev


def main():

    # Banco de Dados
    dml = db.BD()

    # Odds
    df_odds = od.main()
    df_odds_base = df_odds.copy()

    # Base de Jogos
    df_base_matches = mt.main()

    # Campo Condicional Ambas Marcam
    am_conditions = [
        (df_base_matches['FTHG'] > 0 ) & (df_base_matches['FTAG'] > 0), 
        (df_base_matches['FTHG'] == 0) | (df_base_matches['FTAG'] == 0 )
        ]
    sn_val = ['S', 'N']
    df_base_matches.loc[:,"Ambas Marcam"] = np.select(am_conditions, sn_val)

    # Campo Soma Gols Meio Tempo
    df_base_matches.loc[:,"HTG"] = df_base_matches.HTHG + df_base_matches.HTAG

    # Campo Soma Gols Resultado Final
    df_base_matches.loc[:,"FTG"] = df_base_matches.FTHG + df_base_matches.FTAG

    # Conversão de Campos para Inteiro
    df_base_matches = df_base_matches.astype({"HTG": int, "FTG": int, "HTHG": int, "HTAG": int})

    # Cria Funções Lambda
    processa_lambdas()

    # Retorna Métricas Agrupadas Todos Jogos
    df_gp_jogos_todos = desempenho_jogos_todos(df_base_matches)

    # Retorna Métricas Agrupadas Jogos Casa
    df_gp_jogos_casa_home = desempenho_jogos_casa_home(df_base_matches)

    # Retorna Métricas Agrupadas Jogos Fora
    df_gp_jogos_casa_away = desempenho_jogos_casa_away(df_base_matches)

    # Retorna Todas as Métricas das Tabelas
    df_inner_merged_jogos = inner_table_jogos(df_gp_jogos_todos, df_gp_jogos_casa_home, df_gp_jogos_casa_away)

    # Preparação e União de Métricas com Eventos de Odds
    df_events_matches = inner_tables_odds_matches(df_odds, df_inner_merged_jogos)

    # Cálcula Probabilidades
    df_odds_eventos, df_odds_probabilidades = calculate_probabilities(df_events_matches)

    # Cria Cálculos em Eventos
    df_odds_eventos = prepara_odds_events(df_odds_eventos)

    # Tabulação e Criação de IDs em Eventos
    df_cross_table_eventos = cross_table_events(df_odds_eventos)

    # Tabulação e Criação de IDs em Probabilidades
    df_cross_table_probabilidades = cross_table_probabilities(df_odds_probabilidades)

    # Criação de IDs em Odds
    df_odds = create_odds_ids(df_odds)

    # União de Tabelas para Resultado Final
    df_result_odds_prob_ev = odds_prob_events_results(df_odds, df_cross_table_eventos, df_cross_table_probabilidades)

    # Insere Dados Probabilidades + EV no Banco
    dml_insert = dml.inserir_dados(data_frame=df_result_odds_prob_ev, table=f'app_odds_prob_ev')

    # Insere Dados Base no Banco
    df_base_matches.index.names = ['id']
    dml_insert = dml.inserir_dados(data_frame=df_base_matches.rename(columns={'Ambas Marcam': 'ambas_marcam'}, inplace=True), table=f'app_football_matches')

    # Insere Dados Odds no Banco
    df_odds_base.index.names = ['id']
    dml_insert = dml.inserir_dados(data_frame=df_odds_base.rename(columns={'Competição': 'competicao', 'Seleção': 'selecao', 'A favor': 'a_favor'}), table=f'app_odds')
    print(df_odds_base)

    # Atualiza Data
    data_atualizacao = [[1, datetime.today(), None]]
    df_atualizacao = pd.DataFrame(data_atualizacao, columns=['id', 'data', 'texto'])
    dml_insert = dml.inserir_dados(data_frame=df_atualizacao, table=f'app_atualizacao')

    # df_result_odds_prob_ev.to_excel(r"C:\Users\willi\OneDrive\Área de Trabalho\Blue Feather\4. Ambientes DEV\1. Desenvolvimento\Football Odds Analysis V2\teste_re.xlsx")
    # print(df_result_odds_prob_ev)
    print('---- Procesado ----')

    return True


if __name__ == "__main__":

    main()
