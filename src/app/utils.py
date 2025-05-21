import pandas as pd

def load_data():
    benin = pd.read_csv('../../data/benin_clean.csv')
    sierra = pd.read_csv('../../data/sierraleone_clean.csv')
    togo = pd.read_csv('../../data/togo_clean.csv')

    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    return pd.concat([benin, sierra, togo], ignore_index=True)

def get_top_regions(df, metric, n=3):
    return df.groupby('Country')[metric].mean().sort_values(ascending=False).head(n).reset_index()
