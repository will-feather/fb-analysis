from django.test import TestCase
import pandas as pd

# Create your tests here.

base_teste = [['BSB', '23-06-2022', '16:00:00', 'CSA AL', 'Grêmio RS', '1', '1', '0', '0', 'D']]
jogo_teste = pd.DataFrame(base_teste, columns=['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HTHG', 'HTAG', 'HTR'])

print(jogo_teste)
