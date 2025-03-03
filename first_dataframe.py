import pandas as pd

data = {'Ad': ['Selim', 'Ahmet', 'Mehmet'],
        'Yaş': [21, 25, 19],
        'Meslek': ['Data Scientist', 'Mühendis', 'Öğrenci']}

df = pd.DataFrame(data)
print(df)
