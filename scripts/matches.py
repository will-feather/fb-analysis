import pandas as pd

def main():

    FILE_DIR = r'C:\Users\willi\OneDrive\Área de Trabalho\Blue Feather\4. Ambientes DEV\1. Desenvolvimento\Football Odds Analysis V2\Análises_AutoVBA_Amostra.xlsm'
    df_base = pd.read_excel(FILE_DIR, sheet_name='Base', header=1)

    # FILTER TO TESTS
    div = ['BSB']
    team = ['CSA AL']
    team = ['Grêmio RS']

    df_bsb_csa = df_base.loc[df_base['Div'].isin(div) & (df_base['HomeTeam'].isin(team) | df_base['AwayTeam'].isin(team))]
    df_bsb = df_base.loc[df_base['Div'].isin(div)]

    return  df_bsb


if __name__ == "__main__":
    main()