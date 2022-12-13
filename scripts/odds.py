import pandas as pd

def main():

    FILE_DIR = r'C:\Users\willi\OneDrive\Área de Trabalho\Blue Feather\4. Ambientes DEV\1. Desenvolvimento\Football Odds Analysis V2\Análises_AutoVBA_Amostra.xlsm'
    df_odds = pd.read_excel(FILE_DIR, sheet_name='Odds')

    return df_odds


if __name__ == "__main__":
    main()